from matplotlib.pyplot import (plot,  # to draw lines with datasets
                               scatter,  # to plot dots with datasets
                               show)  # to display populated charts
from sklearn.linear_model import LinearRegression  # linear regression model

# since height is independent feature, it can be multi dimensional too
height = [[4.0], [4.5], [5.0], [5.2], [5.4], [5.8], [6.1], [6.2], [6.4], [6.8]]
weight = [42, 44, 49, 55, 53, 58, 60, 64, 66, 69]

# taking regresion object from sklearn libary
reg = LinearRegression()

# training the model with our data
reg.fit(height, weight)

# plotting scatter & line graphs using our original data
scatter(height, weight)

# plotting a line based on original heights and predicted weights
plot(height, reg.predict(height))
show()
