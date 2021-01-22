from string import ascii_letters
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pyodbc
sns.set(style="white")

minRecords = 5000
dbName = 'Kello'
dbTableName = '[dbo].[CZPREOSstanica]'


conn = pyodbc.connect('DRIVER={SQL Server};SERVER=dokelu.kst.fri.uniza.sk;DATABASE=' + dbName + ';UID=read;PWD=read')

q = "SELECT Distinct InSR70, InName FROM [" + dbName + "]." + dbTableName
print(q)
x = pd.read_sql_query(q, conn)
stationsDic = {str(x['InSR70'][i]): x['InName'][i] for i in range(len(x['InSR70']))}
print(stationsDic)

a = []
b = []
dbStations = []
for stationId in stationsDic.keys():
	q = '''select Count(*) count from ''' + dbTableName + ''' where (TrainType='Pn' or TrainType='Nex' or TrainType='Lv') and RealWaitTime = 0 and InSR70 = \'''' + stationId + '\''
	print(q)
	x1 = pd.read_sql_query(q, conn)['count'].values[0]

	q = '''select Count(*) count from ''' + dbTableName + ''' where (TrainType='Pn' or TrainType='Nex' or TrainType='Lv') and RealWaitTime <> 0 and InSR70 = \'''' + stationId + '\''
	print(q)
	x2 = pd.read_sql_query(q, conn)['count'].values[0]

	if(x1 + x2 > minRecords):
		a.append(x1)
		b.append(x2)
		dbStations.append(stationsDic[stationId])

print(dbStations)
print(len(a))
print(a)
print(len(b))
print(b)

df = pd.DataFrame({'RealWaitTime = 0': a, 'RealWaitTime <> 0': b}, index=dbStations)
df.plot.bar(grid='True')
plt.xticks(rotation=15)
plt.title("Pocet RealWaitTime = 0 v staniciach\n" + dbName + " " + dbTableName + "\n Pn/Nex/Lv vlaky")
plt.show()