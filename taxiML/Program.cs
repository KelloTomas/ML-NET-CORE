using Microsoft.ML.Legacy;
using Microsoft.ML.Legacy.Data;
using Microsoft.ML.Legacy.Models;
using Microsoft.ML.Legacy.Trainers;
using Microsoft.ML.Legacy.Transforms;
using System;
using System.IO;
using System.Threading.Tasks;

namespace MLCore
{
	internal class Program
	{
		private static readonly string _datapath = Path.Combine(Environment.CurrentDirectory, "Data", "taxi-fare-train.csv");
		private static readonly string _testdatapath = Path.Combine(Environment.CurrentDirectory, "Data", "taxi-fare-test.csv");
		private static readonly string _modelpath = Path.Combine(Environment.CurrentDirectory, "Data", "Model.zip");

		private static void Main(string[] args)
		{
			Main2(args).Wait();
		}
		private static async Task Main2(string[] args)
		{
			Console.WriteLine("Program started");
			PredictionModel<TaxiTrip, TaxiTripFarePrediction> model = await Train();
			Console.WriteLine("Evaluation!");
			Evaluate(model);
			Console.WriteLine("Finished!");

			Console.ReadLine();
		}

		private static void Evaluate(PredictionModel<TaxiTrip, TaxiTripFarePrediction> model)
		{
			var testData = new TextLoader(_testdatapath).CreateFrom<TaxiTrip>(useHeader: true, separator: ',');
			var evaluator = new RegressionEvaluator();
			RegressionMetrics metrics = evaluator.Evaluate(model, testData);
			Console.WriteLine($"RSquared {metrics.RSquared}");
		}

		public static async Task<PredictionModel<TaxiTrip, TaxiTripFarePrediction>> Train()
		{
			var pipeline = new LearningPipeline
{
	new TextLoader(_datapath).CreateFrom<TaxiTrip>(useHeader: true, separator: ','),
	new ColumnCopier(("FareAmount", "Label")),
	new CategoricalOneHotVectorizer(        "VendorId",     "RateCode",     "PaymentType"),
	new ColumnConcatenator("Features",     "VendorId",     "RateCode",     "PassengerCount",       "TripDistance",     "PaymentType"),
	new FastTreeRegressor()
			};
			/*
			var pipeline = new LearningPipeline
			{
				new ColumnCopier(("FareAmount", "Label")),
				new CategoricalOneHotVectorizer("VendorId", "RateCode", "PaymentType"),
				new ColumnConcatenator("Features", "VendorId", "RateCode", "PassengerCount", "TripDistance", "PaymentType"),
				new FastTreeRegressor()
			};
			*/
			PredictionModel<TaxiTrip, TaxiTripFarePrediction> model = pipeline.Train<TaxiTrip, TaxiTripFarePrediction>();
			await model.WriteAsync(_modelpath);
			return model;
		}
	}
}
