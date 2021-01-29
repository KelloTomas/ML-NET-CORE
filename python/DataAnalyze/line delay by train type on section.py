import pandas as pd
import pyodbc
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")

dbName = 'Kello'
dbTableName = '[CZPREOShistory]'
testCount = 15000
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=dokelu.kst.fri.uniza.sk;DATABASE=' + dbName + ';UID=read;PWD=read')


d = pd.read_sql_query('''select 
       [DelayRailway1]
      ,[DelayStation1]
      ,[DelayRailway2]
      ,[DelayStation2]
      ,[DelayRailway3]
      ,[DelayStation3]
      ,[DelayRailway4]
      ,[DelayStation4]
      ,[DelayRailway5]
      ,[DelayStation5]
      ,[DelayRailway6]
      ,[DelayStation6]
      ,[DelayRailway7] from ''' + dbTableName + ''' where (TrainType = 'Os' OR TrainType = 'Ex' OR TrainType = 'R') and
      DelayRailway1 > -100 and DelayRailway1 < 100 and
      DelayStation1 > -100 and DelayStation1 < 100 and
      DelayRailway2 > -100 and DelayRailway2 < 100 and
      DelayStation2 > -100 and DelayStation2 < 100 and
      DelayRailway3 > -100 and DelayRailway3 < 100 and
      DelayStation3 > -100 and DelayStation3 < 100 and
      DelayRailway4 > -100 and DelayRailway4 < 100 and
      DelayStation4 > -100 and DelayStation4 < 100 and
      DelayRailway5 > -100 and DelayRailway5 < 100 and
      DelayStation5 > -100 and DelayStation5 < 100 and
      DelayRailway6 > -100 and DelayRailway6 < 100 and
      DelayStation6 > -100 and DelayStation6 < 100 and
      DelayRailway7 > -100 and DelayRailway7 < 100
      ''', conn)
      # + " where (TrainType = 'Os' OR TrainType = 'Ex' OR TrainType = 'R')"
      # + " where (TrainType = 'Pn' OR TrainType = 'Lv' OR TrainType = 'Nex')"

sns.distplot(d['DelayRailway1'], hist=False, kde=True, label='Prosenice -> Lipnik nad Becv.')
#sns.distplot(d['DelayStation1'], hist=False, kde=True, label='Lipnik nad Becv.')
sns.distplot(d['DelayRailway2'], hist=False, kde=True, label='Lipnik nad Becv. -> Drahotuse')
#sns.distplot(d['DelayStation2'], hist=False, kde=True, label='Drahotuse')
sns.distplot(d['DelayRailway3'], hist=False, kde=True, label='Drahotuse -> Hranice na Mor.')
#sns.distplot(d['DelayStation3'], hist=False, kde=True, label='Hranice na Mor.')
sns.distplot(d['DelayRailway4'], hist=False, kde=True, label='Hranice na Mor. -> Polom')
#sns.distplot(d['DelayStation4'], hist=False, kde=True, label='Polom')
sns.distplot(d['DelayRailway5'], hist=False, kde=True, label='Polom -> Suchdol nad Odr.')
#sns.distplot(d['DelayStation5'], hist=False, kde=True, label='Suchdol nad Odr.')
sns.distplot(d['DelayRailway6'], hist=False, kde=True, label='Suchdol nad Odr. -> Studénka')
#sns.distplot(d['DelayStation6'], hist=False, kde=True, label='Studénka')
ax = sns.distplot(d['DelayRailway7'], hist=False, kde=True, label='Studénka -> Jistebnik')
ax.set(xlabel='Delay [s]', ylabel='Density')
plt.show()















