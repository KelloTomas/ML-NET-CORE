import pyodbc
import pandas as pd

dbName = 'TrainsDb20-01-23'
dbTableName = 'SK-Kuty'
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=dokelu.kst.fri.uniza.sk;DATABASE=' + dbName + ';UID=read;PWD=read')


q = "SELECT Distinct FromSR70, FromName FROM [" + dbTableName + "]"
print(q)
x = pd.read_sql_query(q, conn)
stationNames = x['FromSR70']

prologue = "insert into [" + dbTableName + "stanica] SELECT a1.[FromSR70],a1.[FromName],a1.[ToSR70] InSR70,a1.[ToName] InName,b1.[ToSR70],b1.[ToName],a1.[SubCount],a1.[TrainId],a1.[TrainNumber],a1.[TrainType],a1.[Weight],a1.[Length],a1.[CarCount],a1.[AxisCount],a1.[EngineType],a1.[ArrRealTime],a1.[ArrILS],b1.[DepRealTime],b1.[DepILS],a1.[ArrPlanTime],b1.[DepPlanTime],NULL [RealWaitTime],NULL [PlanWaitTime],NULL [DelayWait],a1.[DelayArrive],b1.[DelayDeparture],a1.[DriverId] FROM [" + dbTableName + "] a1 join [" + dbTableName + "] b1 on a1.TrainId = b1.TrainId and a1.ToSR70 = b1.FromSR70 and b1.FromSR70 = '"
for x in range(0,len(stationNames)):
	print(prologue.replace('a1', 'a'+str(x)).replace('b1', 'b'+str(x)) + str(stationNames[x]) + "'")

print("UPDATE [" + dbTableName + "stanica] SET [RealWaitTime]=DATEDIFF(SECOND, ArrRealTime, DepRealTime), [PlanWaitTime]=DATEDIFF(SECOND, ArrPlanTime, DepPlanTime), [DelayArrive]=DATEDIFF(SECOND,ArrPlanTime, ArrRealTime), [DelayDeparture]=DATEDIFF(SECOND,DepPlanTime, DepRealTime)")
print("UPDATE [" + dbTableName + "stanica] SET [Delay]=RealWaitTime-PlanWaitTime")
