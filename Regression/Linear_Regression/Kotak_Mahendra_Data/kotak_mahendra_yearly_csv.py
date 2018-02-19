from csv import reader  # to read CSV files
from os.path import dirname  # to get current python file's path

from matplotlib.pyplot import (plot,  # to draw lines with datasets
                               show)  # to display populated charts
from numpy import (append,  # to append an array with another
                   arange,  # to generate array with series of numbers
                   array)  # to create a numpy array
from sklearn.linear_model import LinearRegression  # linear regression model

# reading CSV file from local disk
csv_file = open(dirname(__file__) + "\\" + "data.csv")
csv_reader = reader(csv_file)
csv_data = array(list(csv_reader))

# taking the needed columns. date & amount
x_data = array(csv_data[..., :1], dtype=int)
y_data = array(csv_data[..., 1:], dtype=float).T[0]

# creating regression object & training with existing data
regr = LinearRegression()
regr.fit(x_data, y_data)

# plotting a graph using existing data
plot(x_data, y_data, marker='o')

# adding 5 years to our date variable to use for predection
x_data = array(append(x_data, arange(
    max(x_data) + 1, max(x_data) + 6)))

# transposing (1, len) array to (len, 1) array
x_data.shape = (len(x_data), 1)

# plotting a graph using predected data
plot(x_data, regr.predict(x_data), marker='o')
show()
