import numpy as np
import matplotlib.pyplot as plt
import pyodbc

trainTypes = ['Pn']

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
    yCentered = [i-p[0] for i in y]
    p = np.poly1d(np.polyfit(x, yCentered, 1))
    ax.plot(x, p(x), color)
    return 'y = {0:.2f}x'.format(p[1])

def dbExecute(query):
    print(query)
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER=dokelu.kst.fri.uniza.sk;DATABASE=TrainsDb19-04-02;UID=kello4;PWD=kello4')
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor

if len(trainTypes) == 0:
	cursor = dbExecute('SELECT MAX(PocVoznov), MAX(Hmot), MAX(Dlzka), MAX(PocNaprav) FROM [TrainsDb19-04-02].[dbo].[Trains] group by vlakid')
else:
	cursor = dbExecute('SELECT MAX(PocVoznov), MAX(Hmot), MAX(Dlzka), MAX(PocNaprav) FROM [TrainsDb19-04-02].[dbo].[Trains] WHERE druh = \'' + '\' OR druh = \''.join(trainTypes) + '\' group by vlakid')

step = 1000;
count = 0;
limit = step;
for row in cursor:
    addPoint(row[0], row[1], row[2], row[3]);
    count = count + 1
    if count>=limit:
        limit = limit + step
        print(count)

for data, color, group in zip(datanew, ("red", "green", "blue"),("weight (" + addTrend(datanew[0][0], datanew[0][1], "r--") + ")", "lenght (" + addTrend(datanew[1][0], datanew[1][1], "g--") + ")", "number of axles (" + addTrend(datanew[2][0], datanew[2][1], "b--") + ")")):
    x, y = data
    ax.scatter(x, y, alpha=0.8, c=color, edgecolors='none', s=30, label=group)

if len(trainTypes) == 0:
	plt.title('Relations in selected numeric features\n' + str(len(datanew[0][0])) + ' records')
else:
	plt.title('Relations in selected numeric features \n' + ', '.join(trainTypes) + ' trains\n' + str(len(datanew[0][0])) + ' records')
plt.legend(loc=2)
plt.xlabel("Number of wagons")
plt.show()
