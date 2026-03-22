import numpy as np
from scipy import stats

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
mean = np.mean(speed)
median = np.median(speed)
mode, mode_count = stats.mode(speed).mode, stats.mode(speed).count

print("Mean is: " + str(mean))
print("Median is: " + str(median))
print("Mode is: " + str(mode) + " (appears " + str(mode_count) + " times)")