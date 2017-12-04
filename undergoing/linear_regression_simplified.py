import matplotlib.pyplot as plt
from sklearn import linear_model

#since height is independent feature, it can be multi dimensional too
height = [[4.0], [4.5], [5.0], [5.2], [5.4], [5.8], [6.1], [6.2], [6.4], [6.8]]
weight = [42, 44, 49, 55, 53, 58, 60, 64, 66, 69]

#taking regresion object from sklearn
reg = linear_model.LinearRegression()

#training the model with our data
reg.fit(height, weight)

#after training, we'll get slope variable m & co-efficeint b
#in case of multiple independent variables, we'll get multiple m values, but only one b value
m = reg.coef_[0]
b = reg.intercept_

print("slope = ", m, ", intercept = ", b)

#plotting scatter graph using our original data
plt.scatter(height, weight)

#generating weight values based on our formula and heights
predicted_values = [reg.coef_ * i + reg.intercept_ for i in height]

#plotting a line based on original height and calculated weight
plt.plot(height, predicted_values, 'b')
plt.show()

#predecting weight for random height 8.0
print(reg.predict(X=8.0))