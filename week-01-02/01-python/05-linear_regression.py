import matplotlib.pyplot as plt
from scipy import stats

X = [5,7,8,7,2,17,2,9,4,11,12,9,6]
Y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r_value, p_value, std_err = stats.linregress(X, Y)

print(f"r_value: {r_value}, p_value: {p_value}, std_err: {std_err}")

# Bad fit
# if r_value is close to 0, it means the linear model is not a good fit for the data
if abs(r_value) < 0.5:
    print("The linear model is not a good fit for the data.")

linear_equation = lambda x: slope * x + intercept

linear_model = list(map(linear_equation, X))

plt.scatter(X, Y)

# plt.plot(X, [linear_equation(i) for i in X], color='red')
plt.plot(X, linear_model, color='red')

plt.savefig('./charts/linear-regression-plot.png')
# plt.show()

# predicting a value using the linear model
predicted_y = linear_equation(10)
print(f"Predicted value of Y for X=10 is: {predicted_y}")

