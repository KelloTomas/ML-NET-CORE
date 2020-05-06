from string import ascii_letters
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pyodbc
sns.set(style="white")
dbName = 'TrainsDb20-01-23'

dbTableNames = ['[SK-CA-copy]']
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=dokelu.kst.fri.uniza.sk;DATABASE=' + dbName + ';UID=read;PWD=read')

for dbTableName in dbTableNames:

	SQL_Query = pd.read_sql_query('''SELECT
       [TrainType]
      ,[Weight]
	  ,[DepRealTime]
	  ,ROUND([Temp], 0) as Temp
	  ,ROUND([Wind], 0) as Wind
	  ,ROUND([WindDirection], 0) as WindDirection
	  ,ROUND([Precipitation], 0) as Precipitation
	  ,ROUND([Snow], 0) as Snow
      ,[Delay]
  FROM [TrainsDb20-01-23].[dbo].''' +
  dbTableName +
  ''' LEFT JOIN [TrainsDb20-01-23].[dbo].[SK-CA-weather] on DepRealTime > dateFrom and DepRealTime < dateTo''', conn)

	d = pd.DataFrame(SQL_Query)

	# Convert categorical columns to numeric

	for col in d.select_dtypes(include=['object']).columns.values:
	    d[col] = pd.Categorical(d[col]).codes


	# Compute the correlation matrix
	corr = d.corr()

	# Generate a mask for the upper triangle
	mask = np.zeros_like(corr, dtype=np.bool)
	mask[np.triu_indices_from(mask)] = True

	# Set up the matplotlib figure
	f, ax = plt.subplots(figsize=(11, 9))

	# Generate a custom diverging colormap
	cmap = sns.diverging_palette(220, 10, as_cmap=True)

	# Draw the heatmap with the mask and correct aspect ratio
	sns.heatmap(corr, mask=mask, cmap=cmap, center=0,
	            square=True, linewidths=.5, cbar_kws={"shrink": .5})
	#fig = plt.figure()
	plt.title('Correlation matrix\n' + dbTableName)
	#plt.show()
	plt.savefig('C:\\d\\OneDrive - University of Zilina\\skola_FRI_UNIZA\\dizertacka\\data\\' + dbTableName + ' correlation.png')
