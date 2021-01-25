from string import ascii_letters
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pyodbc
sns.set(style="white")

minRecords = 5000
dbName = 'Kello'
dbTableName = '[SKCA]'

conn = pyodbc.connect('DRIVER={SQL Server};SERVER=dokelu.kst.fri.uniza.sk;DATABASE=' + dbName + ';UID=read;PWD=read')
q = '''SELECT ROUND(Temp, 0) Temp,
Count(case TrainType when 'Os' then 1 else null end) CountOs,
Count(case TrainType when 'R' then 1 else null end) CountR,
Count(case TrainType when 'Ex' then 1 else null end) CountEx,
Count(case TrainType when 'Nex' then 1 else null end) CountNex,
Count(case TrainType when 'PN' then 1 else null end) CountPn,
Count(case TrainType when 'Lv' then 1 else null end) CountLv
FROM [SKCA] where Temp is not null group by ROUND(Temp, 0)'''
x1 = pd.read_sql_query(q, conn)

df = pd.DataFrame({
	'Os': x1['CountOs'].values,
	'R': x1['CountR'].values,
	'Ex': x1['CountEx'].values,
	'Nex': x1['CountNex'].values,
	'Pn': x1['CountPn'].values,
	'Lv': x1['CountLv'].values
	}, index=x1['Temp'].astype('int32').values)
df.plot.bar(stacked=True, grid='True')
plt.xlabel('Temp [°C]')
plt.ylabel('Count')
plt.show()
