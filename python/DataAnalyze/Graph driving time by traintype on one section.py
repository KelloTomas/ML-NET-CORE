import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import pyodbc

import seaborn as sns

numOfLines = 6
trainTypes = {
	'Ex': 0,
	'R': 1,
	'Os': 2,
	'Sp': 2,
	'Sv': 2,

	'Nex': 3,
	'Pn': 4,


	'Lv': 5,
	'Sluz': 5,
	'Mn': 5,
	'Vlec': 5,
	'PMD': 5}
lineNames = ['']*numOfLines
for x in range(0,numOfLines-1):
	lineNames[x] = [k for k,v in trainTypes.items() if v == x]
data = [list(), list(), list(), list(), list(), list(), list(), list(), list(), list(), list(), list()]
# 33722000 -> 33472200 -> 34042200
fromId = '33472200'
toId = '33722000'

def addPoint(index, value):
	data[index] = np.append(data[index], value)

def dbExecute(query):
	conn = pyodbc.connect('DRIVER={SQL Server};SERVER=dokelu.kst.fri.uniza.sk;DATABASE=TrainsDb19-04-02;UID=kello4;PWD=kello4')
	cursor = conn.cursor()
	cursor.execute(query)
	return cursor
	
fromName = dbExecute('SELECT top(1) bod1naz FROM [TrainsDb19-04-02].[dbo].[Trains] WHERE bod1cis = ' + fromId).fetchone()[0]
toName = dbExecute('SELECT top(1) bod2naz FROM [TrainsDb19-04-02].[dbo].[Trains] WHERE bod2cis = ' + toId).fetchone()[0]
cursor = dbExecute('SELECT top(200) druh, CasCesty FROM [TrainsDb19-04-02].[dbo].[Trains] WHERE bod1cis = ' + fromId + ' and bod2cis = ' + toId)

step = 1000;
count = 0;
limit = step;
for row in cursor:
	addPoint(trainTypes[row[0]], row[1])
	count += 1
	if count >= limit:
		limit = limit + step
		print(count)

num_bins = 50
fig, ax = plt.subplots()
#ax.hist(data, num_bins, alpha=1, density=1)
#ax.hist(y, num_bins, alpha=0.5, density=1)
for x in range(0,numOfLines-1):
	sns.kdeplot(data[x], label="Trains " + ', '.join(lineNames[x]))
#	sns.distplot(d, hist=True, kde=True, bins=num_bins, hist_kws={'edgecolor':'black'}, kde_kws={'linewidth': 4})
#sns.kdeplot(data[0], dashes=False)
#sns.kdeplot(data[1], dashes=False)
#sns.kdeplot(data[3], dashes=False)
#sns.distplot(data[0], hist=True, kde=True, bins=num_bins, hist_kws={'edgecolor':'black'}, kde_kws={'linewidth': 4})
#sns.distplot(data[1], hist=True, kde=True, bins=num_bins, hist_kws={'edgecolor':'black'}, kde_kws={'linewidth': 4})
#sns.distplot(data[2], hist=True, kde=True, bins=num_bins, hist_kws={'edgecolor':'black'}, kde_kws={'linewidth': 4})
#sns.distplot(data[3], hist=True, kde=True, bins=num_bins, hist_kws={'edgecolor':'black'}, kde_kws={'linewidth': 4})
#sns.distplot(data[4], hist=True, kde=True, bins=num_bins, hist_kws={'edgecolor':'black'}, kde_kws={'linewidth': 4})
#sns.distplot(data[5], hist=True, kde=True, bins=num_bins, hist_kws={'edgecolor':'black'}, kde_kws={'linewidth': 4})
#sns.distplot(data[6], hist=True, kde=True, bins=num_bins, hist_kws={'edgecolor':'black'}, kde_kws={'linewidth': 4})
#sns.distplot(data[7], hist=True, kde=True, bins=num_bins, hist_kws={'edgecolor':'black'}, kde_kws={'linewidth': 4})
#sns.distplot(data[8], hist=True, kde=True, bins=num_bins, hist_kws={'edgecolor':'black'}, kde_kws={'linewidth': 4})
#sns.distplot(data[9], hist=True, kde=True, bins=num_bins, hist_kws={'edgecolor':'black'}, kde_kws={'linewidth': 4})
#sns.distplot(data[10], hist=True, kde=True, bins=num_bins, hist_kws={'edgecolor':'black'}, kde_kws={'linewidth': 4})
#sns.distplot(data[11], hist=True, kde=True, bins=num_bins, hist_kws={'edgecolor':'black'}, kde_kws={'linewidth': 4})
ax.set_xlabel('Time')
ax.set_ylabel('Number of trains')
plt.legend()
ax.set_title('Relation between train type and driving time\n' + fromName + ' -> ' + toName)
fig.tight_layout()
plt.show()