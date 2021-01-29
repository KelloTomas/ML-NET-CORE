import pandas as pd
import pyodbc
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

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
      ,[DelayRailway7] from ''' + dbTableName + " where (TrainType = 'Os' OR TrainType = 'Ex' OR TrainType = 'R')", conn)
      # + " where (TrainType = 'Os' OR TrainType = 'Ex' OR TrainType = 'R')"
      # + " where (TrainType = 'Pn' OR TrainType = 'Lv' OR TrainType = 'Nex')"
l = len(d)
print('imported ' + str(l) + ' records')

X = d[[
      'DelayRailway1',
      'DelayStation1',
      'DelayRailway2',
      'DelayStation2',
      'DelayRailway3',
      'DelayStation3',
      'DelayRailway4',
      'DelayStation4',
      'DelayRailway5',
      'DelayStation5',
      'DelayRailway6',
      'DelayStation6'
]]

y = d['DelayRailway7']
x_test = X.tail(testCount)

regr = linear_model.LinearRegression()
regr.fit(X.head(l-testCount), y.head(l-testCount))
print(regr.coef_)


y_pred = regr.predict(x_test)
y_test = y.tail(testCount)

print('Mean squared error: %.2f'
      % mean_squared_error(y_test, y_pred))

print('Coefficient of determination: %.2f'
      % r2_score(y_test, y_pred))


print('Mean squared original error: %.2f'
      % mean_squared_error(y_test, np.zeros(len(y_pred))))

print('Coefficient of original determination: %.2f'
      % r2_score(y_test, np.zeros(len(y_pred))))

# Plot outputs nefunguje, asi podporuje len jednorozmerne pole vstupu
#plt.scatter(x_test, y_test,  color='black')
#plt.plot(x_test, y_pred, color='blue', linewidth=3)

#plt.xticks(())
#plt.yticks(())

#plt.show()
