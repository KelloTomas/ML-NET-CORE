from string import ascii_letters
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pyodbc
import itertools

sns.set(style="white")
dbName = 'Kello'

dbTableName = '[CZPREOShistory]'
dbStationsId = [['34652800', '34042200'], ['34042200', '33472200'], ['33472200', '33722000'], ['33722000', '34544700'], ['34544700', '34804500'], ['34804500', '34694000'], ['34694000', '33654500'], ['33654500', '38314100']]

conn = pyodbc.connect('DRIVER={SQL Server};SERVER=dokelu.kst.fri.uniza.sk;DATABASE=' + dbName + ';UID=read;PWD=read')

q = '''select
	[DelayRailway1],
	[DelayStation1],
	[DelayRailway2],
	[DelayStation2],
	[DelayRailway3],
	[DelayStation3],
	[DelayRailway4],
	[DelayStation4],
	[DelayRailway5],
	[DelayStation5],
	[DelayRailway6],
	[DelayStation6],
	[DelayRailway7]	from ''' + dbTableName + " where (TrainType = 'Pn' OR TrainType = 'Lv' OR TrainType = 'Nex')"
	# + " where (TrainType = 'Os' OR TrainType = 'Ex' OR TrainType = 'R')"
	# + " where (TrainType = 'Pn' OR TrainType = 'Lv' OR TrainType = 'Nex')"
print(q)
x = pd.read_sql_query(q, conn)

d = pd.DataFrame(x)
d.plot.box(grid='True', showfliers=False)
plt.xticks(rotation=10)
#plt.title(dbTableName + ", trains: Os, Ex, R")
plt.title(dbTableName + ", trains: Pn, Lv, Nex")
#plt.title(dbTableName)
plt.xlabel('Location')
plt.ylabel('Delay [s]')
plt.show()