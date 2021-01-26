from string import ascii_letters
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pyodbc
import itertools

sns.set(style="white")
dbName = 'Kello'

dbTableNames = ['[SKCA]']

conn = pyodbc.connect('DRIVER={SQL Server};SERVER=dokelu.kst.fri.uniza.sk;DATABASE=' + dbName + ';UID=read;PWD=read')

for dbTableName in dbTableNames:
	a = []
	r = []
	step = 5
	for wind in np.arange(0, 66, step):
		#q = '''select [Delay] from ''' + dbTableName + ''' where (TrainType = 'Nex' or TrainType = 'Pn' or TrainType = 'Lv') and Delay < 2000 and Delay > -2000 and ROUND(Temp, 0) = ''' + str(temp)
		q = '''select [Delay] from ''' + dbTableName + ''' where Delay < 200 and Delay > -200 and wind >= ''' + str(wind/10) + " and wind < "+str((wind+step)/10)
		print(q)
		x = pd.read_sql_query(q, conn)['Delay'].values.tolist()
		if (len(x) == 0):
			x.append(0)
		a.append(x)
		r.append(str(wind/10) + "-" + str((wind+step)/10))
		
	d = pd.DataFrame(itertools.zip_longest(*a), columns=r)
	d.plot.box(grid='True', showfliers=False)
	plt.xlabel('Wind [m/s]')
	plt.ylabel('Delay [s]')
	plt.show()