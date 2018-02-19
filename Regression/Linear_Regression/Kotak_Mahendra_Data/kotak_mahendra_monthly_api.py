from matplotlib.pyplot import (plot,  # to draw lines with datasets
                               show)  # to display populated charts
from numpy import (append,  # to append an array with another
                   array)  # to create a numpy array
from sklearn.linear_model import LinearRegression  # linear regression model

from quandl import get  # to get some dataset from quandl source

csv_file = list(get("NSE/KOTAKNIFTY",
                    authtoken="qAsk6MJV-VXWMqoWDJQk", returns='numpy'))

x_data = []
y_data = []

for i in range(len(csv_file)):
    x_data.append(csv_file[i][0])
    y_data.append(csv_file[i][7])

min_year = min(x_data).year

x_data_2 = array([])

for i in x_data:
    x_data_2 = append(x_data_2, [i.month + (12 * (i.year - min_year))])

x_data_2.shape = (len(x_data_2), 1)

regr = LinearRegression()
regr.fit(x_data_2, y_data)

plot(x_data_2, y_data, marker='o')
plot(x_data_2, regr.predict(x_data_2), marker='o')
show()
