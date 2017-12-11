import csv

import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

# reading CSV file from local disk
csv_file = open("C:\\Users\\saimanoj\\Downloads\\NSE-KOTAKNIFTY.csv")
csv_reader = csv.reader(csv_file)
csv_data = np.array(list(csv_reader))

# taking the needed columns. date & amount
x_data = np.array(csv_data[1:, 1:7], dtype=float)
y_data = np.array(csv_data[1:, 7:], dtype=float).T[0]

# creating regression object & training with existing data
regr = linear_model.LinearRegression()
regr.fit(x_data, y_data)

# plotting a graph using predected data
plt.plot(range(len(x_data)), regr.predict(x_data))
plt.show()