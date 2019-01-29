using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Reflection;

namespace MLCore
{
	internal class Program
	{

		private static void Main(string[] args)
		{
			IModel model = new TaxiFastTreeNew(); // R2 Score: 0.92	RMS loss: 2.81
			//IModel model = new TaxiFastTreeRegression(); // RSquare 0.885729301000846
			//IModel model = new TrainFastTreeNew(); // R2 Score: 0.92	RMS loss: 2.81
			//IModel model = new TrainFastTreeRegression(); // 
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

