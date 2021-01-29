import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pyodbc

dbName = 'Kello'

dbTableName = 'CZPREOS' # + postfix stanica
dbPersonalTrainType = ['Ex', 'Os', 'R']
dbCargoTrainType = ['Lv', 'Nex', 'Pn']

conn = pyodbc.connect('DRIVER={SQL Server};SERVER=dokelu.kst.fri.uniza.sk;DATABASE=' + dbName + ';UID=read;PWD=read')


q = '''select DateName( hour , DateAdd( hour , a.hour , -1 ) ) hour, a.hour x, a.PersonalRailway, b.CargoRailway, c.PersonalStation, d.CargoStation from
(select DATEPART(hour, DepRealTime) hour, avg(Delay) PersonalRailway from {0} where (TrainType = '{1}') group by DATEPART(hour, DepRealTime)) a join 
(select DATEPART(hour, DepRealTime) hour, avg(Delay) CargoRailway from {0} where (TrainType = '{2}') group by DATEPART(hour, DepRealTime)) b
on a.hour = b.hour join
(select DATEPART(hour, DepRealTime) hour, avg(Delay) PersonalStation from {0}stanica where (TrainType = '{1}') group by DATEPART(hour, DepRealTime)) c
on a.hour = c.hour join
(select DATEPART(hour, DepRealTime) hour, avg(Delay) CargoStation from {0}stanica where (TrainType = '{2}') group by DATEPART(hour, DepRealTime)) d
on a.hour = d.hour order by a.hour'''.format(dbTableName, "' OR TrainType = '".join(dbPersonalTrainType), "' OR TrainType = '".join(dbCargoTrainType))
print(q)
x = pd.read_sql_query(q, conn)
del x["x"]

ax = x.plot(kind='line', x='hour', grid=True)
ax.set_title(dbTableName)
ax.set_ylabel('Delay [s]')
ax.set_xlabel('Hour of day')
plt.show()
