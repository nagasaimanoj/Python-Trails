import csv
import datetime as dt

import matplotlib.pyplot as plt
import numpy as np
import pandas
from sklearn import linear_model

import quandl

csv_file = list(quandl.get("NSE/KOTAKNIFTY",
                           authtoken="qAsk6MJV-VXWMqoWDJQk", returns='numpy'))

x_data = []
y_data = []

for i in range(len(csv_file)):
    x_data.append(csv_file[i][0])
    y_data.append(csv_file[i][7])

min_year = min(x_data).year

x_data_2 = np.array([])

for i in x_data:
    x_data_2 = np.append(x_data_2, [i.month + (12 * (i.year - min_year))])

x_data_2.shape = (len(x_data_2), 1)

regr = linear_model.LinearRegression()
regr.fit(x_data_2, y_data)

plt.plot(x_data_2, y_data, marker='o')

plt.plot(x_data_2, regr.predict(x_data_2), marker='o')
plt.show()
