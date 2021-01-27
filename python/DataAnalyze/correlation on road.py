from string import ascii_letters
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pyodbc
sns.set(style="white")
dbName = 'Kello'

dbTableName = '[CZPREOShistory]'
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
      ,[DelayRailway7] from ''' + dbTableName + " where (TrainType = 'Os' OR TrainType = 'Ex' OR TrainType = 'R')", conn)
      # + " where (TrainType = 'Os' OR TrainType = 'Ex' OR TrainType = 'R')"
      # + " where (TrainType = 'Pn' OR TrainType = 'Lv' OR TrainType = 'Nex')"

# Compute the correlation matrix
corr = d.corr()
print(corr)

# Generate a mask for the upper triangle
mask = np.zeros_like(corr, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True

# Generate a custom diverging colormap
cmap = sns.diverging_palette(220, 10, as_cmap=True)

# Draw the heatmap with the mask and correct aspect ratio
sns.heatmap(corr, mask=mask, cmap=cmap, center=0, square=True, linewidths=.5, cbar_kws={"shrink": .5})
#fig = plt.figure()
plt.title(dbTableName + ", trains: Pn, Lv, Nex")
#plt.title(dbTableName + ", trains: Os, Ex, R")
#plt.title(dbTableName)
plt.show()
#plt.savefig('C:\\d\\OneDrive - University of Zilina\\skola_FRI_UNIZA\\dizertacka\\data\\' + dbTableName + ' correlation.png')