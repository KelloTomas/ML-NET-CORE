import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pyodbc
import missingno as msno

conn = pyodbc.connect('DRIVER={SQL Server};SERVER=dokelu.kst.fri.uniza.sk;DATABASE=TrainsDb19-04-02;UID=kello4;PWD=kello4')

SQL_Query = pd.read_sql_query('''select Bod1Cis FromId, Bod2Cis ToId, Vlak TrainNum, Druh TrainType, Loko TrainEngine, Hmot Weight, Dlzka Length, PocNaprav AxlesCount, PocVoznov WagonsCount, StrojveduciCislo DriverId, MeskanieOdchod TrainDelay, GvdCasCesty ExpectedTime, CasCesty DrivingTime from Trains''', conn)

d = pd.DataFrame(SQL_Query)

for col in d.select_dtypes(exclude=['object']).columns.values:
	d[col].replace(0, np.nan, inplace= True)
for col in d.select_dtypes(include=['object']).columns.values:
	d[col].replace('', np.nan, inplace= True)

msno.matrix(d)

plt.show()
