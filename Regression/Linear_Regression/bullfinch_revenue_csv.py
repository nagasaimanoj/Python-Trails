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

plt.plot(x_data, y_data, marker='o')

plt.show()
