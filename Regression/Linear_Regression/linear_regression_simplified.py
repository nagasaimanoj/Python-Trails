from matplotlib import pyplot
from sklearn.linear_model import LinearRegression

# since height is independent feature, it can be multi dimensional too
height = [[4.0], [4.5], [5.0], [5.2], [5.4], [5.8], [6.1], [6.2], [6.4], [6.8]]
weight = [42, 44, 49, 55, 53, 58, 60, 64, 66, 69]

# taking regresion object from sklearn libary
reg = LinearRegression()

# training the model with our data
reg.fit(height, weight)

# plotting scatter & line graphs using our original data
pyplot.scatter(height, weight)

# plotting a line based on original heights and predicted weights
pyplot.plot(height, reg.predict(height))
pyplot.show()
