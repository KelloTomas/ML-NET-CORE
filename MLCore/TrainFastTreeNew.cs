using Microsoft.ML;
using Microsoft.ML.Runtime.Data;
using Microsoft.ML.Trainers.FastTree;
using MLCore.Model;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace MLCore
{
	internal class TrainFastTreeNew : IModel
	{
		private string _dataPath(string date)
		{
			return Path.Combine(Environment.CurrentDirectory, "Data", "train", $"jazdne_doby_preos_{date}.csv");
		}
		private readonly string _trainDataNewPath = Path.Combine(Environment.CurrentDirectory, "Data", "train", "jazdne_doby_preos_train.csv");
		private readonly string _testDataNewPath = Path.Combine(Environment.CurrentDirectory, "Data", "train", "jazdne_doby_preos_test.csv");
		private readonly string _modelPath = Path.Combine(Environment.CurrentDirectory, "Data", "train", "FastTreeRegressionModel.zip");

		private TextLoader _textLoader;
		private TransformerChain<RegressionPredictionTransformer<FastTreeRegressionPredictor>> _model;
		private MLContext _mlContext = new MLContext(seed: 0);




		public void Init()
		{
			/*
			to convert raw data to train and test data
			*/
			List<Train> values = new List<Train>();
			values.AddRange(File.ReadAllLines(_dataPath("20181008")).Skip(1).Select(v => Model.Train.FromCsv(v)).ToList());
			values.AddRange(File.ReadAllLines(_dataPath("20181009")).Skip(1).Select(v => Model.Train.FromCsv(v)).ToList());
			/*
			values.AddRange(File.ReadAllLines(_dataPath("20181010")).Skip(1).Select(v => Model.Train.FromCsv(v)).ToList());
			values.AddRange(File.ReadAllLines(_dataPath("20181011")).Skip(1).Select(v => Model.Train.FromCsv(v)).ToList());
			values.AddRange(File.ReadAllLines(_dataPath("20181012")).Skip(1).Select(v => Model.Train.FromCsv(v)).ToList());
			values.AddRange(File.ReadAllLines(_dataPath("20181013")).Skip(1).Select(v => Model.Train.FromCsv(v)).ToList());
			 */
			
			Program.WriteCSV(values, _trainDataNewPath);

			values = File.ReadAllLines(_dataPath("20181010")).Skip(1).Select(v => Model.Train.FromCsv(v)).ToList();
			Program.WriteCSV(values, _testDataNewPath);

			_textLoader = _mlContext.Data.TextReader(new TextLoader.Arguments()
			{
				Separator = ",",
				HasHeader = true,
				Column = new[]
					{
					/*
					I1= sbyte
					U1= byte
					I2= short
					U2= ushort
					I4= int
					U4= uint
					I8= long
					U8= ulong
					R4= Single
					R8= Double
					TX, TXT, Text = ReadOnlyMemory<char> || string
					BL= bool
					TS= TimeSpan
					DT= DateTime
					DZ= DateTimeOffset
					UG= UInt128
					*/
					new TextLoader.Column("Bod1Cis", DataKind.I4, 0),
					new TextLoader.Column("Bod2Cis", DataKind.I4, 1),
					new TextLoader.Column("CasCesty", DataKind.R4, 2),
					new TextLoader.Column("Dlzka", DataKind.R4, 3),
					new TextLoader.Column("Druh", DataKind.TXT,4),
					new TextLoader.Column("Hmot", DataKind.R4, 5),
					new TextLoader.Column("Loko", DataKind.R4, 6),
					new TextLoader.Column("MeskanieOdchod", DataKind.R4,7),
					new TextLoader.Column("PocNaprav", DataKind.R4, 8),
					new TextLoader.Column("PocVoznov", DataKind.R4, 9),
					new TextLoader.Column("Vlak", DataKind.R4, 10),
					}
			}
			);
		}
		public void Train()
		{
			IDataView dataView = _textLoader.Read(_trainDataNewPath);
			var pipeline = _mlContext.Transforms.CopyColumns("CasCesty", "Label")
				.Append(_mlContext.Transforms.Categorical.OneHotEncoding("Bod1Cis"))
				.Append(_mlContext.Transforms.Categorical.OneHotEncoding("Bod2Cis"))
				.Append(_mlContext.Transforms.Categorical.OneHotEncoding("Druh"))
				.Append(_mlContext.Transforms.Categorical.OneHotEncoding("Loko"))
				.Append(_mlContext.Transforms.Categorical.OneHotEncoding("Vlak"))
				.Append(_mlContext.Transforms.Concatenate("Features", "Bod1Cis", "Bod2Cis", "Dlzka", "Druh", "Hmot", "Loko", "MeskanieOdchod", "PocNaprav", "PocVoznov", "Vlak"))
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
			IDataView dataView = _textLoader.Read(_testDataNewPath);
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