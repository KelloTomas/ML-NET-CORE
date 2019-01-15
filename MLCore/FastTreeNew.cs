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
	internal class FastTreeNew : IModel
	{
		private readonly string _trainDataPath = Path.Combine(Environment.CurrentDirectory, "Data\\taxi", "taxi-fare-train.csv");
		private readonly string _testDataPath = Path.Combine(Environment.CurrentDirectory, "Data\\taxi", "taxi-fare-test.csv");
		private readonly string _modelPath = Path.Combine(Environment.CurrentDirectory, "Data\\taxi", "fastTreeNewModel.zip");

		private TextLoader _textLoader;
		private TransformerChain<RegressionPredictionTransformer<FastTreeRegressionPredictor>> _model;
		private MLContext _mlContext = new MLContext(seed: 0);




		public void Init()
		{
			_textLoader = _mlContext.Data.TextReader(new TextLoader.Arguments()
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
		public void Train()
		{
			IDataView dataView = _textLoader.Read(_trainDataPath);
			var pipeline = _mlContext.Transforms.CopyColumns("FareAmount", "Label")
				.Append(_mlContext.Transforms.Categorical.OneHotEncoding("VendorId"))
				.Append(_mlContext.Transforms.Categorical.OneHotEncoding("RateCode"))
				.Append(_mlContext.Transforms.Categorical.OneHotEncoding("PaymentType"))
				.Append(_mlContext.Transforms.Concatenate("Features", "VendorId", "RateCode", "PassengerCount", "TripTime", "TripDistance", "PaymentType"))
				.Append(_mlContext.Regression.Trainers.FastTree());

			_model = pipeline.Fit(dataView);
			SaveModelAsFileNew(_mlContext, _model);
		}

		private void SaveModelAsFileNew(MLContext mlContext, TransformerChain<RegressionPredictionTransformer<FastTreeRegressionPredictor>> model)
		{
			using (var fileStream = new FileStream(_modelPath, FileMode.Create, FileAccess.Write, FileShare.Write))
				mlContext.Model.Save(model, fileStream);
			Console.WriteLine("The model is saved to {0}", _modelPath);
		}
		public void Evaluate()
		{
			IDataView dataView = _textLoader.Read(_testDataPath);
			var predictions = _model.Transform(dataView);
			var metrics = _mlContext.Regression.Evaluate(predictions, "Label", "Score");
			Console.WriteLine();
			Console.WriteLine($"*************************************************");
			Console.WriteLine($"*       Model quality metrics evaluation         ");
			Console.WriteLine($"*------------------------------------------------");

			Console.WriteLine($"*       R2 Score:      {metrics.RSquared:0.##}");

			Console.WriteLine($"*       RMS loss:      {metrics.Rms:#.##}");
		}

		public void Output()
		{
		}
	}
}

