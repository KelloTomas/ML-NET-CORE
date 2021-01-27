from string import ascii_letters
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pyodbc
import itertools

sns.set(style="white")
dbName = 'Kello'

dbTableName = '[CZPREOS]'
dbStationsId = [['34652800', '34042200'], ['34042200', '33472200'], ['33472200', '33722000'], ['33722000', '34544700'], ['34544700', '34804500'], ['34804500', '34694000'], ['34694000', '33654500'], ['33654500', '38314100']]

conn = pyodbc.connect('DRIVER={SQL Server};SERVER=dokelu.kst.fri.uniza.sk;DATABASE=' + dbName + ';UID=read;PWD=read')

a = []
dbStationsWithCount = []
for stationId in dbStationsId:
	# railway
	q = '''select [Delay] from ''' + dbTableName + ''' where Delay < 2000 and Delay > -2000 and FromSR70 = \'''' + stationId[0] + '\' and ToSR70 = \'' + stationId[1] + '\''
	q = '''select [Delay] from ''' + dbTableName + ''' where Delay < 2000 and Delay > -2000 and (TrainType = 'Os' OR TrainType = 'R' OR TrainType = 'Ex') and FromSR70 = \'''' + stationId[0] + '\' and ToSR70 = \'' + stationId[1] + '\''
	q = '''select [Delay] from ''' + dbTableName + ''' where Delay < 2000 and Delay > -2000 and (TrainType = 'Nex' OR TrainType = 'Pn' OR TrainType = 'Lv') and FromSR70 = \'''' + stationId[0] + '\' and ToSR70 = \'' + stationId[1] + '\''
	print(q)
	x = pd.read_sql_query(q, conn)['Delay'].values.tolist()
	a.append(x)

	# station
	q = '''select [Delay] from ''' + dbTableName + ''' where Delay < 2000 and Delay > -2000 and InSR70 = \'''' + stationId + '\''
	print(q)
	x = pd.read_sql_query(q, conn)['Delay'].values.tolist()
	a.append(x)

	q = '''select TOP(1) FromName, ToName from ''' + dbTableName + ' where FromSR70 = \'' + stationId[0] + '\' and ToSR70 = \'' + stationId[1] + '\''
	print(q)
	sql = pd.read_sql_query(q, conn);
	dbStationsWithCount.append( sql['FromName'].values[0] + " -> " + sql['ToName'].values[0] + " [" + str(len(x)) + "]")

d = pd.DataFrame(itertools.zip_longest(*a), columns=dbStationsWithCount)
d.plot.box(grid='True', showfliers=False)
plt.xticks(rotation=10)
plt.title(dbTableName + ", trains: Nex, Pn, Lv")
plt.xlabel('Railway [count]')
plt.ylabel('Delay [s]')
plt.show()