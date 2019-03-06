using MLCore.Models;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Text;

namespace MLCore
{
	internal class Program
	{

		private static void Main(string[] args)
		{
			var db = new Models.TrainsDbContext();
			DirectoryInfo d = new DirectoryInfo(@"D:\data_20190226");//Assuming Test is your Folder
			FileInfo[] Files = d.GetFiles("*.csv"); //Getting Text files
			foreach (FileInfo file in Files)
			{
				using (var sr = new StreamReader(file.FullName, Encoding.GetEncoding("ISO-8859-1")))
				{

					sr.ReadLine();
					using (var sw = new StreamWriter(@"D:\merge.csv", true))
						sw.Write(sr.ReadToEnd());
					Console.Write(".");
					continue;
					int count = 0;
					string line;
					while ((line = sr.ReadLine()) != null)
					{
						count++;
						var train = Trains.FromCsv(line);
						db.Trains.Add(train);
					}
					db.SaveChanges();
					Console.WriteLine($"Importet file: {file.Name}");
					Console.WriteLine($"Records: {count}");
				}
			}

			Console.WriteLine("finished");
			Console.ReadLine();
			return;
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

