using Microsoft.ML;
using Microsoft.ML.Core.Data;
using Microsoft.ML.Legacy;
using Microsoft.ML.Legacy.Models;
using Microsoft.ML.Legacy.Trainers;
using Microsoft.ML.Legacy.Transforms;
using Microsoft.ML.Runtime.Data;
using Microsoft.ML.Runtime.EntryPoints;
using Microsoft.ML.Trainers.FastTree;
using MLCore.Model;
using System;
using System.IO;
using System.Threading.Tasks;

namespace MLCore
{
	class TaxiFastTreeRegression : IModel
	{
		private readonly string _trainDataPath = Path.Combine(Environment.CurrentDirectory, "Data\\taxi", "taxi-fare-train.csv");
		private readonly string _testDataPath = Path.Combine(Environment.CurrentDirectory, "Data\\taxi", "taxi-fare-test.csv");
		private readonly string _modelPath = Path.Combine(Environment.CurrentDirectory, "Data\\taxi", "FastTreeRegressionModel.zip");

		private PredictionModel<TaxiTrip, TrainFarePrediction> _model;
		private readonly MLContext _mlContextNew = new MLContext(seed: 0);

		public void Init()
		{
		}

		public void Train()
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
			_model = pipeline.Train<TaxiTrip, TrainFarePrediction>();
			_model.WriteAsync(_modelPath).Wait();
		}

		public void Evaluate()
		{
			var testData = new Microsoft.ML.Legacy.Data.TextLoader(_testDataPath).CreateFrom<TaxiTrip>(useHeader: true, separator: ',');
			var evaluator = new Microsoft.ML.Legacy.Models.RegressionEvaluator();
			RegressionMetrics metrics = evaluator.Evaluate(_model, testData);
			Console.WriteLine($"RSquared {metrics.RSquared}");
		}
		
		public void Output()
		{
		}

		private void SaveModelAsFileNew(MLContext mlContext, TransformerChain<RegressionPredictionTransformer<FastTreeRegressionPredictor>> model)
		{
			using (var fileStream = new FileStream(_modelPath, FileMode.Create, FileAccess.Write, FileShare.Write))
				mlContext.Model.Save(model, fileStream);
			Console.WriteLine("The model is saved to {0}", _modelPath);
		}



	}
}

