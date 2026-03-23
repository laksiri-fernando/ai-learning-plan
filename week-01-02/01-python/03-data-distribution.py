import numpy
import matplotlib.pyplot as plt
import sys

# x = numpy.random.uniform(0.0, 5.0, 250)
uniformx = numpy.random.uniform(0.0, 5.0, 100000)

print(uniformx)

# plt.hist(x, 5)
plt.hist(uniformx, 100)

# Save chart to a PNG file so it works in terminal / non-GUI environments
plt.savefig('./charts/data_distribution.png')
print('Saved chart as data_distribution.png')

# Also display chart when a GUI backend is available
plt.show()

normalx = numpy.random.normal(5.0, 1.0, 100000)
plt.hist(normalx, 100)
plt.savefig('./charts/normal_distribution.png')
print('Saved chart as normal_distribution.png')
plt.show()