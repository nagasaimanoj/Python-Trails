from csv import reader
from matplotlib import pyplot
from numpy import array, append, arange
from sklearn import linear_model
from os.path import dirname

# reading CSV file from local disk
csv_file = open(dirname(__file__) + "\\" + "data.csv")
csv_reader = reader(csv_file)
csv_data = array(list(csv_reader))

# taking the needed columns. date & amount
x_data = array(csv_data[..., :1], dtype=int)
y_data = array(csv_data[..., 1:], dtype=float).T[0]

# creating regression object & training with existing data
regr = linear_model.LinearRegression()
regr.fit(x_data, y_data)

# plotting a graph using existing data
pyplot.plot(x_data, y_data, marker='o')

# adding 5 years to our date variable to use for predection
x_data = array(append(x_data, arange(
    max(x_data) + 1, max(x_data) + 6)))

# transposing (1, len) array to (len, 1) array
x_data.shape = (len(x_data), 1)

# plotting a graph using predected data
pyplot.plot(x_data, regr.predict(x_data), marker='o')
pyplot.show()
