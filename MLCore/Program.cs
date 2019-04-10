using Database;
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
			/*
			var db = new TrainsDbContext();
			DirectoryInfo d = new DirectoryInfo(@"C:\vlaky");//Assuming Test is your Folder
			FileInfo[] Files = d.GetFiles("*.csv");
			foreach (FileInfo file in Files)
			{
				FileHelpers.FileHelperEngine<Trains> engine = new FileHelpers.FileHelperEngine<Trains>(Encoding.GetEncoding("ISO-8859-1"));
				engine.HeaderText = engine.GetFileHeader().Remove(0,3);
				Trains[] trains = engine.ReadFile(file.FullName);
				int count = 0;
				foreach (var train in trains)
				{
					count++;
					db.Trains.Add(train);
				}
				db.SaveChanges();
				Console.WriteLine($"Importet file: {file.Name}");
				Console.WriteLine($"Records: {count}");
				//ReadFileLineByLine(db, file);
			}

			Console.WriteLine("finished");
			Console.ReadLine();
			return;
			*/
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

		private static void ReadFileLineByLine(TrainsDbContext db, FileInfo file)
		{
			using (var sr = new StreamReader(file.FullName, Encoding.GetEncoding("ISO-8859-1")))
			{
				sr.ReadLine();
				if (false)
				{
					using (var sw = new StreamWriter(@"D:\merge.csv", true))
						sw.Write(sr.ReadToEnd());
					Console.Write(".");
				}
				else
				{
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

