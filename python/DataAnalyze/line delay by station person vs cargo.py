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


q = '''select DateName( month , DateAdd( month , a.month , -1 ) ) month, a.month x, a.PersonalRailway, b.CargoRailway, c.PersonalStation, d.CargoStation from
(select DATEPART(MONTH, DepRealTime) month, avg(Delay) PersonalRailway from {0} where (TrainType = '{1}') group by DATEPART(MONTH, DepRealTime)) a join 
(select DATEPART(MONTH, DepRealTime) month, avg(Delay) CargoRailway from {0} where (TrainType = '{2}') group by DATEPART(MONTH, DepRealTime)) b
on a.month = b.month join
(select DATEPART(MONTH, DepRealTime) month, avg(Delay) PersonalStation from {0}stanica where (TrainType = '{1}') group by DATEPART(MONTH, DepRealTime)) c
on a.month = c.month join
(select DATEPART(MONTH, DepRealTime) month, avg(Delay) CargoStation from {0}stanica where (TrainType = '{2}') group by DATEPART(MONTH, DepRealTime)) d
on a.month = d.month order by a.month'''.format(dbTableName, "' OR TrainType = '".join(dbPersonalTrainType), "' OR TrainType = '".join(dbCargoTrainType))
print(q)
x = pd.read_sql_query(q, conn)
del x["x"]

ax = x.plot(kind='line', x='month')
ax.set_title(dbTableName)
ax.set_ylabel('Delay [s]')
plt.show()
