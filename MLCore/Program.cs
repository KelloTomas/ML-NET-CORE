using Microsoft.ML;
using Microsoft.ML.Core.Data;
using Microsoft.ML.Legacy;
using Microsoft.ML.Legacy.Models;
using Microsoft.ML.Legacy.Trainers;
using Microsoft.ML.Legacy.Transforms;
using Microsoft.ML.Runtime.Data;
using Microsoft.ML.Trainers.FastTree;
using MLCore.Model;
using System;
using System.IO;
using System.Threading.Tasks;

namespace MLCore
{
	internal class Program
	{

		private static void Main(string[] args)
		{
			//IModel model = new FastTreeRegression(); // RSquare 0.885729301000846
			IModel model = new FastTreeNew(); // R2 Score: 0.92	RMS loss: 2.81
			Console.WriteLine("Program started");
			model.Init();
			model.Train();
			Console.WriteLine("Evaluation!");
			model.Evaluate();
			Console.WriteLine("Finished!");
			model.Output();
			Console.ReadLine();
		}
	}
}

