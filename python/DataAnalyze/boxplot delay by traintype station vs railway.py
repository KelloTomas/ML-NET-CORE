#from string import ascii_letters
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pyodbc
sns.set_style("whitegrid")

dbName = 'Kello'

dbTableName = 'CZPREOS'
dbTrainType = ['Ex', 'Lv', 'Mn', 'Nex', 'Os', 'Pn', 'R', 'Sv']
#dbTrainType = ['Sluz']

conn = pyodbc.connect('DRIVER={SQL Server};SERVER=dokelu.kst.fri.uniza.sk;DATABASE=' + dbName + ';UID=read;PWD=read')

df = pd.DataFrame(columns = ['TrainType', 'Place', 'Delay'])

for trainType in dbTrainType:
	q = '''select TrainType, 'Station' as Place, Delay from ''' + dbTableName + '''stanica where Delay < 2000 and Delay > -2000 and TrainType = \'''' + trainType + '\''
	x = pd.read_sql_query(q, conn)
	df = df.append(x)

	q = '''select TrainType, 'Railway' as Place, Delay from ''' + dbTableName + ''' where Delay < 2000 and Delay > -2000 and TrainType = \'''' + trainType + '\''
	x = pd.read_sql_query(q, conn)
	df = df.append(x)

	print(trainType + " finished")

sns.boxplot(x='TrainType', y='Delay', hue='Place', data=df, showfliers=False)
plt.ylabel('Delay [s]')
plt.show()
