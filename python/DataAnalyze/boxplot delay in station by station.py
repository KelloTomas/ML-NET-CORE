from string import ascii_letters
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pyodbc
sns.set(style="white")
dbName = 'Kello'

dbTableNames = ['[CZPREOSstanica]']
dbStationsId = ['34164400', '34662700', '38062600', '38274700', '34804500', '34544700', '34694000', '38314100', '33654500', '33722000', '34042200', '33472200', '34652800', ]

conn = pyodbc.connect('DRIVER={SQL Server};SERVER=dokelu.kst.fri.uniza.sk;DATABASE=' + dbName + ';UID=read;PWD=read')

for dbTableName in dbTableNames:
	a = []
	dbStationsWithCount = []
	for stationId in dbStationsId:
		q = '''select [Delay] from ''' + dbTableName + ''' where Delay < 2000 and Delay > -2000 and InSR70 = \'''' + stationId + '\''
		print(q)
		x = pd.read_sql_query(q, conn)['Delay'].values.tolist()
		a.append(x)

		q = '''select TOP(1) InName from ''' + dbTableName + ' where InSR70 = \'' + stationId + '\''
		dbStationsWithCount.append( pd.read_sql_query(q, conn)['InName'].values[0] + " [" + str(len(x)) + "]")

	print(dbStationsWithCount)
	d = pd.DataFrame([*zip(*a)], columns=dbStationsWithCount)
	d.plot.box(grid='True', showfliers=False)
	plt.xticks(rotation=35)
	#plt.title("Meskania v staniciach podla stanice\nDelay <> 0")
	plt.title("Meskania v staniciach podla stanice")
	plt.show()