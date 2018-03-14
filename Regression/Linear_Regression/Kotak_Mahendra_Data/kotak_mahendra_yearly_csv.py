from csv import reader
from os.path import dirname

from matplotlib.pyplot import (plot, show)
from numpy import (append, arange, array)
from sklearn.linear_model import LinearRegression

csv_file = open(dirname(__file__) + "\\" + "data.csv")
csv_reader = reader(csv_file)
csv_data = array(list(csv_reader))

x_data = array(csv_data[..., :1], dtype=int)
y_data = array(csv_data[..., 1:], dtype=float).T[0]

regr = LinearRegression()
regr.fit(x_data, y_data)

plot(x_data, y_data, marker='o')

x_data = array(append(x_data, arange(
    max(x_data) + 1, max(x_data) + 6)))

x_data.shape = (len(x_data), 1)

plot(x_data, regr.predict(x_data), marker='o')
show()
