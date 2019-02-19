using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Threading;

namespace MLCore
{
	internal class Program
	{

		private static void Main(string[] args)
		{
			DateTime dt = DateTime.Now;

			//IModel model = new TaxiFastTreeNew(); // R2 Score: 0.92	RMS loss: 2.81
			//IModel model = new TaxiFastTreeRegression(); // RSquare 0.885729301000846
			IModel model = new TrainFastTreeNew();

			Console.WriteLine("Program started");
			model.Init();
			model.Train();
			Console.WriteLine("Evaluation!");
			model.Evaluate();
			Console.WriteLine("Finished!");
			model.Output();
			TimeSpan ts = DateTime.Now - dt;
			Console.WriteLine($"\n\n Time to calculate: {ts.ToString(@"hh\:mm\:ss\.ffff")}");
			Console.ReadLine();
		}
		public static void WriteCSV<T>(IEnumerable<T> items, string path)
		{
			Type itemType = typeof(T);
			var props = itemType.GetProperties(BindingFlags.Public | BindingFlags.Instance)
								.OrderBy(p => p.Name);

			using (var writer = new StreamWriter(path))
			{
				writer.WriteLine(string.Join(", ", props.Select(p => p.Name)));

				foreach (var item in items)
				{
					writer.WriteLine(string.Join(", ", props.Select(p => p.GetValue(item))));
				}
			}
		}
	}
}

