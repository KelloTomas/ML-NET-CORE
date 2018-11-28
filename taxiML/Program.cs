using Microsoft.ML;
using Microsoft.ML.Core.Data;
using Microsoft.ML.Legacy;
using Microsoft.ML.Legacy.Models;
using Microsoft.ML.Legacy.Trainers;
using Microsoft.ML.Legacy.Transforms;
using Microsoft.ML.Runtime.Data;
using Microsoft.ML.Runtime.EntryPoints;
using Microsoft.ML.Trainers.FastTree;
using System;
using System.IO;
using System.Threading.Tasks;

namespace MLCore
{
	internal class Program
	{
		private static readonly string _trainDataPath = Path.Combine(Environment.CurrentDirectory, "Data", "taxi-fare-train.csv");
		private static readonly string _testDataPath = Path.Combine(Environment.CurrentDirectory, "Data", "taxi-fare-test.csv");
		private static readonly string _modelPath = Path.Combine(Environment.CurrentDirectory, "Data", "oldModel.zip");

		private static PredictionModel<TaxiTrip, TaxiTripFarePrediction> modelOld;
		private static TextLoader _textLoader;
		private static TransformerChain<RegressionPredictionTransformer<FastTreeRegressionPredictor>> modelNew;
		private static MLContext mlContextNew = new MLContext(seed: 0);

		private static void Main(string[] args)
		{
			Console.WriteLine("Program started");
			//MainOld(args).Wait();
			bool useOld = true;
			if (args.Length > 0)
				useOld = args[0] == "old";
			if (useOld)
			{
				Console.WriteLine("Using old program");
				TrainOld().Wait();
			}
			else
			{
				Console.WriteLine("Using new program");
				InitNew();
				TrainNew();
			}
			Console.WriteLine("Evaluation!");

			if (useOld)
			{
				EvaluateOld();
			}
			else
			{
				EvaluateNew();
				TestSinglePredictionNew();
			}
			Console.WriteLine("Finished!");
			Console.ReadLine();
		}

		private static void EvaluateOld()
		{
			var testData = new Microsoft.ML.Legacy.Data.TextLoader(_testDataPath).CreateFrom<TaxiTrip>(useHeader: true, separator: ',');
			var evaluator = new Microsoft.ML.Legacy.Models.RegressionEvaluator();
			RegressionMetrics metrics = evaluator.Evaluate(modelOld, testData);
			Console.WriteLine($"RSquared {metrics.RSquared}");
		}
		
		public static async Task TrainOld()
		{
			var pipeline = new LearningPipeline
			{
				new Microsoft.ML.Legacy.Data.TextLoader(_trainDataPath).CreateFrom<TaxiTrip>(useHeader: true, separator: ','),
				new ColumnCopier(("FareAmount", "Label")),
				new CategoricalOneHotVectorizer("VendorId", "RateCode", "PaymentType"),
				new ColumnConcatenator("Features", "VendorId", "RateCode", "PassengerCount", "TripDistance", "PaymentType"),
				new FastTreeRegressor()
			};
			
			new KMeansPlusPlusClusterer();
			modelOld = pipeline.Train<TaxiTrip, TaxiTripFarePrediction>();
			await modelOld.WriteAsync(_modelPath);
		}

		private static void InitNew()
		{
			_textLoader = mlContextNew.Data.TextReader(new TextLoader.Arguments()
			{
				Separator = ",",
				HasHeader = true,
				Column = new[]
					{
						new TextLoader.Column("VendorId", DataKind.Text, 0),
						new TextLoader.Column("RateCode", DataKind.Text, 1),
						new TextLoader.Column("PassengerCount", DataKind.R4, 2),
						new TextLoader.Column("TripTime", DataKind.R4, 3),
						new TextLoader.Column("TripDistance", DataKind.R4, 4),
						new TextLoader.Column("PaymentType", DataKind.Text, 5),
						new TextLoader.Column("FareAmount", DataKind.R4, 6)
					}
			}
			);
		}
		public static void TrainNew()
		{
			IDataView dataView = _textLoader.Read(_trainDataPath);
			var pipeline = mlContextNew.Transforms.CopyColumns("FareAmount", "Label")
				.Append(mlContextNew.Transforms.Categorical.OneHotEncoding("VendorId"))
				.Append(mlContextNew.Transforms.Categorical.OneHotEncoding("RateCode"))
				.Append(mlContextNew.Transforms.Categorical.OneHotEncoding("PaymentType"))
				.Append(mlContextNew.Transforms.Concatenate("Features", "VendorId", "RateCode", "PassengerCount", "TripTime", "TripDistance", "PaymentType"))
				.Append(mlContextNew.Regression.Trainers.FastTree());

			modelNew = pipeline.Fit(dataView);
			SaveModelAsFileNew(mlContextNew, modelNew);
		}

		private static void SaveModelAsFileNew(MLContext mlContext, TransformerChain<RegressionPredictionTransformer<FastTreeRegressionPredictor>> model)
		{
			using (var fileStream = new FileStream(_modelPath, FileMode.Create, FileAccess.Write, FileShare.Write))
				mlContext.Model.Save(model, fileStream);
			Console.WriteLine("The model is saved to {0}", _modelPath);
		}
		private static void EvaluateNew()
		{
			IDataView dataView = _textLoader.Read(_testDataPath);
			var predictions = modelNew.Transform(dataView);
			var metrics = mlContextNew.Regression.Evaluate(predictions, "Label", "Score");
			Console.WriteLine();
			Console.WriteLine($"*************************************************");
			Console.WriteLine($"*       Model quality metrics evaluation         ");
			Console.WriteLine($"*------------------------------------------------");

			Console.WriteLine($"*       R2 Score:      {metrics.RSquared:0.##}");

			Console.WriteLine($"*       RMS loss:      {metrics.Rms:#.##}");
		}

		private static void TestSinglePredictionNew()
		{
			ITransformer loadedModel;
			using (var stream = new FileStream(_modelPath, FileMode.Open, FileAccess.Read, FileShare.Read))
			{
				loadedModel = mlContextNew.Model.Load(stream);
			}
			var predictionFunction = loadedModel.MakePredictionFunction<TaxiTrip, TaxiTripFarePrediction>(mlContextNew);
			var taxiTripSample = new TaxiTrip()
			{
				VendorId = "VTS",
				RateCode = "1",
				PassengerCount = 1,
				TripTime = 1140,
				TripDistance = 3.75f,
				PaymentType = "CRD",
				FareAmount = 0 // To predict. Actual/Observed = 15.5
			};
			var prediction = predictionFunction.Predict(taxiTripSample);
			Console.WriteLine($"**********************************************************************");
			Console.WriteLine($"Predicted fare: {prediction.FareAmount:0.####}, actual fare: 15.5");
			Console.WriteLine($"**********************************************************************");
		}
	}
}

