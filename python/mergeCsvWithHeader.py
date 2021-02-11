import os
mydir = 'test'
mydir = 'preos_2018_27.1.2021'
filenames = os.listdir(mydir)
with open('out.csv', 'w') as outfile:
    outfile.write('FromSR70;FromName;ToSR70;ToName;SubCount;TrainId;TrainNumber;TrainType;Weight;Length;CarCount;AxisCount;EngineType;SectIdx;DepRealTime;DepILS;ArrRealTime;ArrILS;DepPlanTime;ArrPlanTime;Delay;LengthSect;PredDelay;PredLength;PredSR70;DriverId;TIN\n')
    for fname in filenames:
        with open(mydir + '/' + fname) as infile:
            infile.readline()
            for line in infile:
                outfile.write(line)