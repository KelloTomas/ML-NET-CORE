from string import ascii_letters
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pyodbc
sns.set(style="white")
dbName = 'Kello'

dbTableNames = ['[SK-CA]']
dbTrainType = ['Ex', 'Lv', 'Mn', 'Nex', 'Os', 'Pn', 'R', 'Sluz', 'Sv']
dbTrainType = ['Ex', 'Lv', 'Mn', 'Nex', 'Os', 'Pn', 'R', 'Sv']

conn = pyodbc.connect('DRIVER={SQL Server};SERVER=dokelu.kst.fri.uniza.sk;DATABASE=' + dbName + ';UID=read;PWD=read')

for dbTableName in dbTableNames:
	a = []
	for trainType in dbTrainType:
		x = pd.read_sql_query('''select [Delay] from ''' + dbTableName + ''' where Delay < 2000 and Delay > -2000 and TrainType = \'''' + trainType + '\'', conn)['Delay'].values.tolist()
		a.append(x)

	d = pd.DataFrame([*zip(*a)], columns=dbTrainType)
	d.plot.box(grid='True')
	plt.show()

	# Set up the matplotlib figure
	#f, ax = plt.subplots(figsize=(11, 9))

	# Generate a custom diverging colormap
	#cmap = sns.diverging_palette(220, 10, as_cmap=True)

	# Draw the heatmap with the mask and correct aspect ratio
	#sns.heatmap(corr, mask=mask, cmap=cmap, center=0,
	            #square=True, linewidths=.5, cbar_kws={"shrink": .5})
	#fig = plt.figure()
	#plt.title('Correlation matrix\n' + dbTableName)
	#plt.show()
	#plt.savefig('C:\\d\\OneDrive - University of Zilina\\skola_FRI_UNIZA\\dizertacka\\data\\' + dbTableName + ' correlation.png')