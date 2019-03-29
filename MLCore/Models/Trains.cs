using System;
using System.Globalization;

namespace MLCore.Models
{
	public static class Extensions
	{
		public static DateTime? ToDateTimeSafe(this string dateTime)
		{
			if (string.IsNullOrWhiteSpace(dateTime))
				return (DateTime?)null;
			else
				return
					dateTime.ToDateTime();
		}
		public static DateTime ToDateTime(this string dateTime)
		{
			return DateTime.ParseExact(dateTime, "d. M. yyyy H:mm:ss", CultureInfo.InvariantCulture);
		}
	}
	public partial class Trains
	{
		public static Trains FromCsv(string csvLine)
		{
			string[] values = csvLine.Split(';');
			Trains train = new Trains();
			train.Bod1Cis = Convert.ToInt32(values[0]);
			train.Bod2Cis = Convert.ToInt32(values[1]);
			train.Bod1Naz = values[2];
			train.Bod2Naz = values[3];
			train.VlakId = Convert.ToInt32(values[4]);
			train.Vlak = Convert.ToInt32(values[5]);
			train.Druh = values[6];
			train.Hmot = Convert.ToInt32(values[7]);
			train.Dlzka = Convert.ToInt32(values[8]);
			train.PocVoznov = Convert.ToInt32(values[9]);
			train.PocNaprav = Convert.ToInt32(values[10]);
			train.Loko = values[11];
			train.Odch = values[12].ToDateTimeSafe();
			train.Prich = values[13].ToDateTimeSafe();
			train.GvdOdch = values[14].ToDateTimeSafe();
			train.GvdPrich = values[15].ToDateTimeSafe();
			train.StrojveduciCislo = values[16].Trim('"');
			train.MeskanieOdchod = train.GvdOdch.HasValue ? (int)(train.Odch - train.GvdOdch).Value.TotalSeconds : (int?)null;
			train.MeskaniePrichod = train.GvdPrich.HasValue ? (int)(train.Prich - train.GvdPrich).Value.TotalSeconds : (int?)null;
			train.CasCesty = train.Odch.HasValue && train.Prich.HasValue ? (int)(train.Prich - train.Odch).Value.TotalSeconds : (int?)null;
			train.GvdCasCesty = train.GvdOdch.HasValue && train.GvdPrich.HasValue ? (int)(train.GvdPrich - train.GvdOdch).Value.TotalSeconds : (int?)null;

			return train;
		}
		public int Id { get; set; }
		public int Bod1Cis { get; set; }
		public string Bod1Naz { get; set; }
		public int Bod2Cis { get; set; }
		public string Bod2Naz { get; set; }
		public int VlakId { get; set; }
		public int Vlak { get; set; }
		public string Druh { get; set; }
		public string Loko { get; set; }
		public int Hmot { get; set; }
		public int Dlzka { get; set; }
		public int PocNaprav { get; set; }
		public int PocVoznov { get; set; }
		public string StrojveduciCislo { get; set; }
		public DateTime? GvdOdch { get; set; }
		public DateTime? GvdPrich { get; set; }
		public int? GvdCasCesty { get; set; }
		public DateTime? Odch { get; set; }
		public DateTime? Prich { get; set; }
		public int? CasCesty { get; set; }
		public int? MeskanieOdchod { get; set; }
		public int? MeskaniePrichod { get; set; }
	}
}
