from string import ascii_letters
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pyodbc
sns.set(style="white")

conn = pyodbc.connect('DRIVER={SQL Server};SERVER=dokelu.kst.fri.uniza.sk;DATABASE=TrainsDb19-04-02;UID=kello4;PWD=kello4')

SQL_Query = pd.read_sql_query('''select Bod1Cis FromId, Bod2Cis ToId, Vlak TrainNum, Druh TrainType, Loko TrainEngine, Hmot Weight, Dlzka Length, PocNaprav AxlesCount, PocVoznov WagonsCount, StrojveduciCislo DriverId, MeskanieOdchod TrainDelay, GvdCasCesty ExpectedTime, CasCesty DrivingTime from trains''', conn)

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
plt.title('Correlation matrix')
plt.show()
