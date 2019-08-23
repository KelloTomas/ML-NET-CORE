import matplotlib
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(19680801)

# example data
mu = 100  # mean of distribution
sigma = 15  # standard deviation of distribution
x = mu + sigma * np.random.randn(437)

x = [1,2,2,3,4,4,4,4,4,5,6,7,8]
y = [1,2,6,5,8,7,6,8,5,5,6,7,8]

num_bins = 50

fig, ax = plt.subplots()

# the histogram of the data
ax.hist([x,y], num_bins, alpha=1, density=1)
#ax.hist(y, num_bins, alpha=0.5, density=1)
ax.set_xlabel('Smarts')
ax.set_ylabel('Probability density')
ax.set_title(r'Histogram of IQ: $\mu=100$, $\sigma=15$')
fig.tight_layout()
plt.show()
