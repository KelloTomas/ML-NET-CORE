using FileHelpers;
using System;

namespace Database.Models
{
	[DelimitedRecord(";"), IgnoreFirst(1)]
	public partial class CzPreosPreos
	{
		[FieldHidden]
		[System.ComponentModel.DataAnnotations.Key]
		public int Id { get; set; }
		public int FromSr70 { get; set; }
		public string FromName { get; set; }
		public int ToSr70 { get; set; }
		public string ToName { get; set; }
		public int SubCount { get; set; }
		public int TrainId { get; set; }
		public int TrainNumber { get; set; }
		public string TrainType { get; set; }
		public int Weight { get; set; }
		public int Length { get; set; }
		public int CarCount { get; set; }
		public int AxisCount { get; set; }
		public string EngineType { get; set; }
		public int SectIdx { get; set; }
		[FieldConverter(ConverterKind.Date, DateFormat._myDateTimeFormat)]
		public DateTime? DepRealTime { get; set; }
		public int? DepIls { get; set; }
		[FieldConverter(ConverterKind.Date, DateFormat._myDateTimeFormat)]
		public DateTime? ArrRealTime { get; set; }
		public int? ArrIls { get; set; }
		[FieldHidden]
		public int? RealDrivingTime { get; set; }
		[FieldConverter(ConverterKind.Date, DateFormat._myDateTimeFormat)]
		public DateTime? DepPlanTime { get; set; }
		[FieldConverter(ConverterKind.Date, DateFormat._myDateTimeFormat)]
		public DateTime? ArrPlanTime { get; set; }
		[FieldHidden]
		public int? PlanDrivingTime { get; set; }
		public decimal? Delay { get; set; }
		[FieldHidden]
		public int? DelayDeparture { get; set; }
		[FieldHidden]
		public int? DelayArrive { get; set; }
		public decimal? LengthSect { get; set; }
		public decimal? PredDelay { get; set; }
		public decimal? PredLength { get; set; }
		public decimal? PredSr70 { get; set; }
		public string DriverId { get; set; }
	}
}
