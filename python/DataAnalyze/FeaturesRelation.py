import numpy as np
import matplotlib.pyplot as plt

# Create data

#N = 60
#g1 = (0.6 + 0.6 * np.random.rand(N), np.random.rand(N))
#g2 = (0.4+0.3 * np.random.rand(N), 0.5*np.random.rand(N))
#g3 = (0.3*np.random.rand(N),0.3*np.random.rand(N))
#data = (g1, g2, g3)

datanew = ([list(),list()], [list(),list()], [list(),list()])
for i in range(0, 20):
    datanew[0][0] = np.append(datanew[0][0], i)
    datanew[0][1] = np.append(datanew[0][1], float(i)+np.random.rand(1)*3)
    datanew[1][0] = np.append(datanew[1][0], i)
    datanew[1][1] = np.append(datanew[1][1], i*2+np.random.rand(1)*3)
    datanew[2][0] = np.append(datanew[2][0], i)
    datanew[2][1] = np.append(datanew[2][1], i*0.5+np.random.rand(1)*3)

# Create plot

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)


for data, color, group in zip(datanew, ("red", "green", "blue"), ("coffee", "tea", "water")):
    x, y = data
    ax.scatter(x, y, alpha=0.8, c=color, edgecolors='none', s=30, label=group)


p0 = np.poly1d(np.polyfit(datanew[0][0], datanew[0][1], 1))
ax.plot(datanew[0][0], p0(datanew[0][0]), "r--")
p1 = np.poly1d(np.polyfit(datanew[1][0], datanew[1][1], 1))
ax.plot(datanew[1][0], p1(datanew[1][0]), "g--")
p2 = np.poly1d(np.polyfit(datanew[2][0], datanew[2][1], 1))
ax.plot(datanew[2][0], p2(datanew[2][0]), "b--")

plt.title('Matplot scatter plot')
plt.legend(loc=2)
plt.show()

