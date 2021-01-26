from string import ascii_letters
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pyodbc
import itertools

sns.set(style="white")
dbName = 'Kello'

dbTableName = '[CZPREOSstanica]'
dbStationsId = ['34164400', '34662700', '38062600', '38274700', '34804500', '34544700', '34694000', '38314100', '33654500', '33722000', '34042200', '33472200', '34652800', ]

conn = pyodbc.connect('DRIVER={SQL Server};SERVER=dokelu.kst.fri.uniza.sk;DATABASE=' + dbName + ';UID=read;PWD=read')

a = []
dbStationsWithCount = []
for stationId in dbStationsId:
	q = '''select [Delay] from ''' + dbTableName + ''' where Delay < 2000 and Delay > -2000 and InSR70 = \'''' + stationId + '\''
	print(q)
	x = pd.read_sql_query(q, conn)['Delay'].values.tolist()
	a.append(x)

	q = '''select TOP(1) InName from ''' + dbTableName + ' where InSR70 = \'' + stationId + '\''
	dbStationsWithCount.append( pd.read_sql_query(q, conn)['InName'].values[0] + " [" + str(len(x)) + "]")

d = pd.DataFrame(itertools.zip_longest(*a), columns=dbStationsWithCount)
d.plot.box(grid='True', showfliers=False)
plt.xticks(rotation=35)
plt.title(dbTableName)
plt.xlabel('Station name')
plt.ylabel('Delay [s]')
plt.show()