import matplotlib.pyplot as plt
from sklearn import linear_model

height = [[2010], [2015], [2016], [2017]]
weight = [149431603257, 12421.79, 291987535.37, 7059254217.30]

reg = linear_model.LinearRegression()

reg.fit(height, weight)

m = reg.coef_[0]
b = reg.intercept_

print("slope = ", m, ", intercept = ", b)

plt.scatter(height, weight)

predicted_values = [reg.coef_ * i + reg.intercept_ for i in height]

plt.plot(height, predicted_values, 'b')
plt.show()

print(reg.predict(X=2018))