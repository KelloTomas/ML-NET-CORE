from string import ascii_letters
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pyodbc
import itertools
import statistics

sns.set(style="white")
dbName = 'Kello'

dbTableName = '[SKCA]'

conn = pyodbc.connect('DRIVER={SQL Server};SERVER=dokelu.kst.fri.uniza.sk;DATABASE=' + dbName + ';UID=read;PWD=read')
data = []
r = range(-28, 34)

for temp in r:
	#q = '''select [Delay] from ''' + dbTableName + ''' where (TrainType = 'Nex' or TrainType = 'Pn' or TrainType = 'Lv') and Delay < 2000 and Delay > -2000 and ROUND(Temp, 0) = ''' + str(temp)
	q = '''select [Delay] from ''' + dbTableName + ''' where (TrainType = 'Os' or TrainType = 'R' or TrainType = 'Ex') and Delay < 2000 and Delay > -2000 and ROUND(Temp, 0) = ''' + str(temp)
	#q = '''select [Delay] from ''' + dbTableName + ''' where Delay < 2000 and Delay > -2000 and ROUND(Temp, 0) = ''' + str(temp)
	x = pd.read_sql_query(q, conn)['Delay'].values.tolist()
	data.append(x)



d = pd.DataFrame(itertools.zip_longest(*data), columns=r)
d.plot.box(grid='True', showfliers=False)
plt.xlabel('Temp [°C]')
plt.ylabel('Delay [s]')
#plt.legend(['Nex, Pn, Lv trains'])
plt.legend(['Os, R, Ex trains'])
plt.show()