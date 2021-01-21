import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pyodbc
import missingno as msno
dbName = 'Kello'
dbTableNames = [
	'[CZPREOS]'#,
	#'[CZ-PREOS_PREOS]',
	#'[CZ-TREKO]',
	#'[CZ-VELIB]',
	#'[SK-BB]',
	#'[SK-CA-MySQL]',
	#'[SK-CA-Oracle]',
	#'[SK-KrasnoNKys-MySQL]',
	#'[SK-KrasnoNKys-Oracle]',
	#'[SK-Kuty-MySQL]',
	#'[SK-Kuty-Oracle]'
	]

conn = pyodbc.connect('DRIVER={SQL Server};SERVER=dokelu.kst.fri.uniza.sk;DATABASE=' + dbName + ';UID=read;PWD=read')
for dbTableName in dbTableNames:
	print('running on table: ' + dbTableName)
	SQL_Query = pd.read_sql_query('''select [FromName],[ToName],[TrainId],[TrainNumber],[TrainType],[Weight],[Length],[CarCount],[AxisCount],[EngineType],[DepRealTime],[DepILS],[ArrRealTime],[ArrILS],[DepPlanTime],[ArrPlanTime],[DriverId] from ''' + dbTableName + " where TrainType ='Ex' or TrainType = 'Os' or TrainType = 'R'", conn)

	d = pd.DataFrame(SQL_Query)
	if d.size == 0:
		print('Table has no data -> skipping')
		continue

	for col in d.select_dtypes(exclude=['object']).columns.values:
		d[col].replace(0, np.nan, inplace= True)
	for col in d.select_dtypes(include=['object']).columns.values:
		d[col].replace('', np.nan, inplace= True)

	msno.matrix(d)

	plt.title(dbTableName + " vlaky Ex Os R")
	print("showing")
	plt.show()
	print("showed")
	plt.savefig('C:\\d\\OneDrive - University of Zilina\\skola_FRI_UNIZA\\dizertacka\\data\\' + dbTableName + ' missing values.png')

