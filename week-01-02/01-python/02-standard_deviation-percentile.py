import numpy as np

speed1 = [86,87,88,86,87,85,86]
speed2 = [32,111,138,28,59,77,97]

std1 = np.std(speed1)
std2 = np.std(speed2)
mean1 = np.mean(speed1)
mean2 = np.mean(speed2)

print("Standard Deviation of speed1 is: " + str(std1) + " (mean: " + str(mean1) + ")")
print("Standard Deviation of speed2 is: " + str(std2) + " (mean: " + str(mean2) + ")")

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
percentile_75 = np.percentile(ages, 75)
percentile_90 = np.percentile(ages, 90)
print(f"75th Percentile of ages is: {percentile_75} (75% of ages are below this value {percentile_75})")
print(f"90th Percentile of ages is: {percentile_90} (90% of ages are below this value {percentile_90})")