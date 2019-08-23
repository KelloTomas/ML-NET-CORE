import numpy as np
import matplotlib.pyplot as plt
import pyodbc

# Create plot and data

datanew = ([list(),list()], [list(),list()], [list(),list()])
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

def addPoint(vagony, hmot, dlzka, napravy):
    if (vagony != 0):
        if (hmot != 0):
            datanew[0][0] = np.append(datanew[0][0], vagony)
            datanew[0][1] = np.append(datanew[0][1], hmot)
        if (dlzka != 0):
            datanew[1][0] = np.append(datanew[1][0], vagony)
            datanew[1][1] = np.append(datanew[1][1], dlzka)
        if (napravy != 0):
            datanew[2][0] = np.append(datanew[2][0], vagony)
            datanew[2][1] = np.append(datanew[2][1], napravy)

def addTrend(x, y, color):
    p = np.poly1d(np.polyfit(x, y, 1))
    ax.plot(x, p(x), color)

def dbExecute(query):
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER=dokelu.kst.fri.uniza.sk;DATABASE=TrainsDb19-04-02;UID=kello4;PWD=kello4')
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor

trainType = 'Nex'
#cursor = dbExecute('SELECT MAX(PocVoznov), MAX(Hmot), MAX(Dlzka), MAX(PocNaprav) FROM [TrainsDb19-04-02].[dbo].[Trains] WHERE druh = \'' + trainType + '\' group by vlakid')
cursor = dbExecute('SELECT MAX(PocVoznov), MAX(Hmot), MAX(Dlzka), MAX(PocNaprav) FROM [TrainsDb19-04-02].[dbo].[Trains] WHERE druh = \'Lv\' OR druh = \'Sv\' OR druh = \'Sluz\' OR druh = \'Mn\' OR druh = \'Sp\' OR druh = \'Vlec\' OR druh = \'PMD\' group by vlakid')

step = 1000;
count = 0;
limit = step;
for row in cursor:
    count = count + 1
    addPoint(row[0], row[1], row[2], row[3]);
    if count>=limit:
        limit = limit + step
        print(count)

for data, color, group in zip(datanew, ("red", "green", "blue"), ("weight ("+str(len(datanew[0][0]))+")", "lenght ("+str(len(datanew[1][0]))+")", "number of axles ("+str(len(datanew[2][0]))+")")):
    x, y = data
    ax.scatter(x, y, alpha=0.8, c=color, edgecolors='none', s=30, label=group)

# Create and plot Trend

addTrend(datanew[0][0], datanew[0][1], "r--")
addTrend(datanew[1][0], datanew[1][1], "g--")
addTrend(datanew[2][0], datanew[2][1], "b--")

#plt.title('Relations in selected numeric features \n' + trainType + ' trains')
plt.title('Relations in selected numeric features \nother trains')
plt.legend(loc=2)
plt.xlabel("Number of wagons")
plt.show()

