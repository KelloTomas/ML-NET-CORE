import numpy as np
import matplotlib.pyplot as plt

# Create plot and data

datanew = ([list(),list()], [list(),list()], [list(),list()])
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

def addPoint(vagony, hmot, dlzka, napravy):
    datanew[0][0] = np.append(datanew[0][0], vagony)
    datanew[0][1] = np.append(datanew[0][1], hmot)
    datanew[1][0] = np.append(datanew[1][0], vagony)
    datanew[1][1] = np.append(datanew[1][1], dlzka)
    datanew[2][0] = np.append(datanew[2][0], vagony)
    datanew[2][1] = np.append(datanew[2][1], napravy)

def addTrend(x, y, color):
    p = np.poly1d(np.polyfit(x, y, 1))
    ax.plot(x, p(x), color)
    
for i in range(0, 20):
    addPoint(i, i+np.random.rand(1)*3, i*2+np.random.rand(1)*3, i*0.5+np.random.rand(1)*3)


for data, color, group in zip(datanew, ("red", "green", "blue"), ("hmotnost", "dlzka", "pocet naprav")):
    x, y = data
    ax.scatter(x, y, alpha=0.8, c=color, edgecolors='none', s=30, label=group)

# Create and plot Trend

addTrend(datanew[0][0], datanew[0][1], "r--")
addTrend(datanew[1][0], datanew[1][1], "g--")
addTrend(datanew[2][0], datanew[2][1], "b--")

plt.title('Matplot scatter plot')
plt.legend(loc=2)
plt.show()

