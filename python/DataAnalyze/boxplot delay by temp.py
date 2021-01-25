from string import ascii_letters
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pyodbc
sns.set(style="white")
dbName = 'Kello'

dbTableNames = ['[SKCA]']

conn = pyodbc.connect('DRIVER={SQL Server};SERVER=dokelu.kst.fri.uniza.sk;DATABASE=' + dbName + ';UID=read;PWD=read')

for dbTableName in dbTableNames:
	a = []

	for temp in range(-28, 34):
		#q = '''select [Delay] from ''' + dbTableName + ''' where (TrainType = 'Nex' or TrainType = 'Pn' or TrainType = 'Lv') and Delay < 2000 and Delay > -2000 and ROUND(Temp, 0) = ''' + str(temp)
		q = '''select [Delay] from ''' + dbTableName + ''' where Delay < 2000 and Delay > -2000 and ROUND(Temp, 0) = ''' + str(temp)
		x = pd.read_sql_query(q, conn)['Delay'].values.tolist()
		a.append(x)

	d = pd.DataFrame([*zip(*a)], columns=range(-28, 34))
	d.plot.box(grid='True', showfliers=False)
	plt.xlabel('Temp [°C]')
	plt.ylabel('Delay [s]')
	plt.show()