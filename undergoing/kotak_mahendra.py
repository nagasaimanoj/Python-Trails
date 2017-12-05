import csv

import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

csv_file = open("C:\\Users\\saimanoj\\Downloads\\data.csv")
csv_reader = csv.reader(csv_file)
csv_data = np.array(list(csv_reader))

x_data = np.array(csv_data[..., :1], dtype=int)
y_data = np.array(csv_data[..., 1:], dtype=float)

y_data.shape = (1, 8)
y_data = y_data[0]

regr = linear_model.LinearRegression()
regr.fit(x_data, y_data)

plt.scatter(x_data, y_data)
plt.plot(x_data, regr.predict(x_data))
plt.show()
