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
dbTrainType = ['Ex', 'Lv', 'Mn', 'Nex', 'Os', 'Pn', 'R', 'Sv']
dbTrainTypeWithCount = []

conn = pyodbc.connect('DRIVER={SQL Server};SERVER=dokelu.kst.fri.uniza.sk;DATABASE=' + dbName + ';UID=read;PWD=read')

a = []
for trainType in dbTrainType:
	q = '''select [Delay] from ''' + dbTableName + ''' where Delay < 2000 and Delay > -2000 and TrainType = \'''' + trainType + '\''
	print(q)
	x = pd.read_sql_query(q, conn)['Delay'].values.tolist()
	dbTrainTypeWithCount.append(trainType + " [" + str(len(x)) + "]")
	a.append(x)

d = pd.DataFrame(itertools.zip_longest(*a), columns=dbTrainTypeWithCount)
d.plot.box(grid='True', showfliers=False)
plt.title(dbTableName)
plt.xlabel('Train type')
plt.ylabel('Delay [s]')
plt.show()