/*
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
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Threading.Tasks;

namespace MLCore
{
	class TrainFastTreeRegression : IModel
	{
		private readonly string _trainDataPath = Path.Combine(Environment.CurrentDirectory, "Data", "train", "jazdne_doby_preos_20181008.csv");
		private readonly string _trainDataNewPath = Path.Combine(Environment.CurrentDirectory, "Data", "train", "jazdne_doby_preos_20181008new.csv");
		private readonly string _testDataPath = Path.Combine(Environment.CurrentDirectory, "Data", "train", "jazdne_doby_preos_20181009.csv");
		private readonly string _modelPath = Path.Combine(Environment.CurrentDirectory, "Data", "train", "FastTreeRegressionModel.zip");

		private PredictionModel<Train, TrainFarePrediction> _model;
		private readonly MLContext _mlContextNew = new MLContext(seed: 0);

		public void Init()
		{
            List<Train> values = File.ReadAllLines(_trainDataPath)
                                           .Skip(1)
                                           .Select(v => Model.Train.FromCsv(v))
                                           .ToList();
			WriteCSV(values, _trainDataNewPath);
		}

		public void Train()
		{
			var x = new Microsoft.ML.Legacy.Data.TextLoader(_trainDataNewPath).CreateFrom<Train>(useHeader: true, separator: ',');
			var pipeline = new LearningPipeline
			{
				x,
				new ColumnCopier(("CasCesty", "Label")),
				new CategoricalOneHotVectorizer("Bod1Naz", "Bod2Naz", "Druh"),
				new ColumnConcatenator("Features", "Bod1Naz", "Bod2Naz", "Druh", "Hmot", "Dlzka", "PocVoznov", "PocNaprav", "Loko", "MeskanieOdchod", "MeskaniePrichod", "CasCesty"),
				new FastTreeRegressor()
			};
			
			new KMeansPlusPlusClusterer();
			_model = pipeline.Train<Train, TrainFarePrediction>();
			_model.WriteAsync(_modelPath).Wait();
		}

		public void Evaluate()
		{
			var testData = new Microsoft.ML.Legacy.Data.TextLoader(_testDataPath).CreateFrom<Train>(useHeader: true, separator: ',');
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
*/