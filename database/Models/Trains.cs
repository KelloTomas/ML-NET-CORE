using System;
using System.Collections.Generic;

namespace Database.Models
{
    public partial class Trains
    {
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
        public DateTime? DepRealTime { get; set; }
        public int? DepIls { get; set; }
        public DateTime? ArrRealTime { get; set; }
        public int? ArrIls { get; set; }
        public int? RealDrivingTime { get; set; }
        public DateTime? DepPlanTime { get; set; }
        public DateTime? ArrPlanTime { get; set; }
        public int? PlanDrivingTime { get; set; }
        public int? Delay { get; set; }
        public int? DelayDeparture { get; set; }
        public int? DelayArrive { get; set; }
        public decimal? LengthSect { get; set; }
        public decimal? PredDelay { get; set; }
        public decimal? PredLength { get; set; }
        public decimal? PredSr70 { get; set; }
        public string DriverId { get; set; }
    }
}
