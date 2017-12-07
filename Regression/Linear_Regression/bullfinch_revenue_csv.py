import csv
import matplotlib.pyplot as plt
import numpy as np

csv_file = open("C:\\Users\\saimanoj\\Downloads\\revenue.csv")
csv_reader = csv.reader(csv_file)
csv_data = np.array(list(csv_reader))

x_data = csv_data[..., 0]
y_data = csv_data[..., 1]

plt.plot(x_data, y_data, marker='o')

plt.show()
