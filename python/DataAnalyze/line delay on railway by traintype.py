import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pyodbc

dbName = 'Kello'

dbTableName = 'CZPREOS'

conn = pyodbc.connect('DRIVER={SQL Server};SERVER=dokelu.kst.fri.uniza.sk;DATABASE=' + dbName + ';UID=read;PWD=read')

q = '''select a.T Lines,
avg(a.part1) part1,
avg(a.part2) part2,
avg(a.part3) part3,
avg(a.part4) part4,
avg(a.part5) part5,
avg(a.part6) part6,
avg(a.part7) part7
from
(select
case when TrainType = 'Pn' OR TrainType = 'Lv' OR TrainType = 'Nex' Then 'CargoRailway' ELSE 'PersonRailway' END T,
DelayRailway1 part1,
DelayRailway2 part2,
DelayRailway3 part3,
DelayRailway4 part4,
DelayRailway5 part5,
DelayRailway6 part6,
DelayRailway7 part7
from CZPREOShistory where 
(TrainType = 'Pn' OR TrainType = 'Lv' OR TrainType = 'Nex' OR TrainType = 'Os' OR TrainType = 'Ex' OR TrainType = 'R')) a
group by a.T
UNION
select a.T,
avg(a.part1) part1,
avg(a.part2) part2,
avg(a.part3) part3,
avg(a.part4) part4,
avg(a.part5) part5,
avg(a.part6) part6,
avg(a.part7) part7
from
(select
case when TrainType = 'Pn' OR TrainType = 'Lv' OR TrainType = 'Nex' Then 'CargoStation' ELSE 'PersonStation' END T,
DelayStation1 part1,
DelayStation2 part2,
DelayStation3 part3,
DelayStation4 part4,
DelayStation5 part5,
DelayStation6 part6,
DelayStation7 part7
from CZPREOShistory where 
(TrainType = 'Pn' OR TrainType = 'Lv' OR TrainType = 'Nex' OR TrainType = 'Os' OR TrainType = 'Ex' OR TrainType = 'R')) a
group by a.T'''

print(q)
x = pd.read_sql_query(q, conn)

x = x.set_index('Lines').T
print(x)
x = x.rename(index={
	'part1': 'Lipnik nad Becv.',
	'part2': 'Drahotuse',
	'part3': 'Hranice na Mor.',
	'part4': 'Polom',
	'part5': 'Suchdol nad Odr.',
	'part6': 'Studénka',
	'part7': 'Jistebnik',
	})
ax = x.plot(grid=True)
ax.set_ylabel('Delay [s]')
ax.set_xlabel('Stations')
plt.show()
