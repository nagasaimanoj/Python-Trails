import matplotlib.pyplot as plt
from sklearn import linear_model
import quadl

height = [[2012], [2013], [2014], [2015], [2016], [2017]]
weight = [0, 0, 0, 5166063.898, 404537126.8, 3322383541]

reg = linear_model.LinearRegression()

reg.fit(height, weight)

plt.scatter(height, weight)

height += [[2018], [2019], [2020]]

predicted_values = reg.predict(height)

plt.scatter(height, predicted_values, color = "red")
plt.plot(height, predicted_values, 'b')
plt.show()