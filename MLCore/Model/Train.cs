using Microsoft.ML.Runtime.Api;
using System;

namespace MLCore.Model
{
	public class Train
	{
		public static Train FromCsv(string csvLine)
		{
			string[] values = csvLine.Split(',');
			Train train = new Train();
			train.Bod1Cis = Convert.ToInt32(values[0]);
			train.Bod2Cis = Convert.ToInt32(values[1]);
			train.Bod1Naz = values[2];
			train.Bod2Naz = values[3];
			train.Vlak = Convert.ToInt32(values[4]);
			train.Druh = values[5];
			train.Hmot = Convert.ToInt32(values[6]);
			train.Dlzka = Convert.ToInt32(values[7]);
			train.PocVoznov = Convert.ToInt32(values[8]);
			train.PocNaprav = Convert.ToInt32(values[9]);
			train.Loko = values[10];
			train.Odch = Convert.ToDateTime(values[11]);
			train.Prich = Convert.ToDateTime(values[12]);
			train.GvdOdch = string.IsNullOrWhiteSpace(values[13]) ? Convert.ToDateTime(values[11]) : Convert.ToDateTime(values[13]);
			train.GvdPrich = string.IsNullOrWhiteSpace(values[14]) ? Convert.ToDateTime(values[12]) : Convert.ToDateTime(values[14]);
			train.MeskanieOdchod = (float)(train.GvdOdch - train.Odch).TotalSeconds;
			train.MeskaniePrichod = (float)(train.GvdPrich - train.Prich).TotalSeconds;
			train.CasCesty = (float)(train.GvdPrich - train.GvdOdch).TotalSeconds;
			return train;
		}
		[Column("0")]
		public int Bod1Cis { get; set; }

		[Column("1")]
		public string Bod1Naz;

		[Column("2")]
		public int Bod2Cis { get; set; }

		[Column("3")]
		public string Bod2Naz;

		[Column("4")]
		public float CasCesty { get; set; }

		[Column("5")]
		public float Dlzka { get; set; }

		[Column("6")]
		public string Druh { get; set; }

		[Column("7")]
		public DateTime GvdOdch;

		[Column("8")]
		public DateTime GvdPrich;

		[Column("9")]
		public float Hmot { get; set; }

		[Column("10")]
		public string Loko { get; set; }

		[Column("11")]
		public float MeskanieOdchod { get; set; }

		[Column("12")]
		public float MeskaniePrichod;

		[Column("13")]
		public DateTime Odch;

		[Column("14")]
		public float PocNaprav { get; set; }

		[Column("15")]
		public float PocVoznov { get; set; }

		[Column("16")]
		public DateTime Prich;

		[Column("17")]
		public float Vlak { get; set; }
	}

	public class TrainFarePrediction
	{
		[ColumnName("Score")]
		public float CasCesty;
	}
}
