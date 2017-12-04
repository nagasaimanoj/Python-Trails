import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

x_data = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])
y_data = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])

print(x_data, y_data)

plt.scatter(x_data, y_data)
plt.plot(x_data, y_data)

plt.show()

regr = linear_model.LinearRegression()

regr.fit(x_data, y_data)

x_test = np.array([[11, 12, 13, 14, 15]])

y_pred = regr.predict(x_test)

print(x_test, y_pred)
