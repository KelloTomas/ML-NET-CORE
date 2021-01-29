#from string import ascii_letters
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pyodbc
#sns.set_style("whitegrid")

dbName = 'Kello'

dbTableName = 'CZPREOS' # + postfix stanica
dbPersonalTrainType = ['Ex', 'Os', 'R']
dbCargoTrainType = ['Lv', 'Nex', 'Pn']

conn = pyodbc.connect('DRIVER={SQL Server};SERVER=dokelu.kst.fri.uniza.sk;DATABASE=' + dbName + ';UID=read;PWD=read')


q = '''select DateName( weekday , DateAdd( day , a.day , -1 ) ) day, a.day x, a.PersonalRailway, b.CargoRailway, c.PersonalStation, d.CargoStation from
(select DATEPART(weekday, DepRealTime) day, avg(Delay) PersonalRailway from {0} where (TrainType = '{1}') group by DATEPART(weekday, DepRealTime)) a join 
(select DATEPART(weekday, DepRealTime) day, avg(Delay) CargoRailway from {0} where (TrainType = '{2}') group by DATEPART(weekday, DepRealTime)) b
on a.day = b.day join
(select DATEPART(weekday, DepRealTime) day, avg(Delay) PersonalStation from {0}stanica where (TrainType = '{1}') group by DATEPART(weekday, DepRealTime)) c
on a.day = c.day join
(select DATEPART(weekday, DepRealTime) day, avg(Delay) CargoStation from {0}stanica where (TrainType = '{2}') group by DATEPART(weekday, DepRealTime)) d
on a.day = d.day order by a.day'''.format(dbTableName, "' OR TrainType = '".join(dbPersonalTrainType), "' OR TrainType = '".join(dbCargoTrainType))
print(q)
x = pd.read_sql_query(q, conn)
del x["x"]

ax = x.plot(kind='line', x='Day')
ax.set_title(dbTableName)
ax.set_ylabel('Delay [s]')
plt.show()
