import csv

import matplotlib.pyplot as plt
from sklearn import linear_model

csv_file = open("C:\\Users\\saimanoj\\Downloads\\revenue.csv")
csv_reader = csv.reader(csv_file)
csv_data = list(csv_reader)

x_data = []
y_data = []

for x in csv_data:
    x_data.append(x[0])
    y_data.append(x[1])

x_label = x_data[0]
y_label = y_data[0]

x_data = x_data[1:]
y_data = y_data[1:]

print(x_data, y_data)

plt.plot(x_data, y_data)

plt.xlabel(x_label)
plt.ylabel(y_label)

plt.show()