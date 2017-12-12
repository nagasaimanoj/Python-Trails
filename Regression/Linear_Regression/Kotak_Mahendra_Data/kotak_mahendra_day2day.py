from matplotlib import pyplot
from numpy import array, append
from sklearn import linear_model

import quandl

csv_file = list(quandl.get("NSE/KOTAKNIFTY",
                           authtoken="qAsk6MJV-VXWMqoWDJQk", returns='numpy'))

x_data = []
y_data = []

for i in range(len(csv_file)):
    x_data.append(csv_file[i][0])
    y_data.append(csv_file[i][7])

min_date = min(x_data)

x_data_2 = array([], dtype=int)

for i in x_data:
    x_data_2 = append(x_data_2, [(i - min_date).days])

x_data_2.shape = (len(x_data_2), 1)

regr = linear_model.LinearRegression()
regr.fit(x_data_2, y_data)

pyplot.plot(x_data_2, y_data, marker='o')
pyplot.plot(x_data_2, regr.predict(x_data_2), marker='o')
pyplot.show()
