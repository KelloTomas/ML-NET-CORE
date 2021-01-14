from string import ascii_letters
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pyodbc
sns.set(style="white")
dbName = 'Kello'

dbTableNames = ['[CZPREOSstanica]']
dbTrainType = ['Ex', 'Lv', 'Mn', 'Nex', 'Os', 'Pn', 'R', 'Sluz', 'Sv']
dbTrainType = ['Ex', 'Lv', 'Mn', 'Nex', 'Os', 'Pn', 'R', 'Sv']
dbTrainTypeWithCount = []

conn = pyodbc.connect('DRIVER={SQL Server};SERVER=dokelu.kst.fri.uniza.sk;DATABASE=' + dbName + ';UID=read;PWD=read')

for dbTableName in dbTableNames:
	a = []
	for trainType in dbTrainType:
		q = '''select [Delay] from ''' + dbTableName + ''' where Delay < 2000 and Delay > -2000 and TrainType = \'''' + trainType + '\''
		print(q)
		x = pd.read_sql_query(q, conn)['Delay'].values.tolist()
		dbTrainTypeWithCount.append(trainType + " [" + str(len(x)) + "]")
		a.append(x)

	print(dbTrainTypeWithCount)
	d = pd.DataFrame([*zip(*a)], columns=dbTrainTypeWithCount)
	d.plot.box(grid='True', showfliers=False)
	#plt.title("Meskania v staniciach podla typu vlaku\nDelay <> 0")
	plt.title("Meskania v staniciach podla typu vlaku")
	plt.show()