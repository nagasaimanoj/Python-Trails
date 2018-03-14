from os.path import dirname
from numpy import (genfromtxt, mean)

DATA_POINTS = genfromtxt(dirname(__file__) + "\\" + "data.csv", delimiter=",")

data_intercept, data_slope = 0, 0

data_num_iterations = len(DATA_POINTS) * 10

learning_rate = 1 / data_num_iterations / 10

for i in range(data_num_iterations):
    avg_change = mean(2 / len(DATA_POINTS) *
                      (DATA_POINTS[:, 1] - data_slope * DATA_POINTS[:, 0] + data_intercept))

    data_intercept += avg_change * learning_rate

    data_slope += sum(DATA_POINTS[:, 0]) * avg_change * learning_rate

print("intercept =", data_intercept)
print("slope =", data_slope)
print("average error =", mean(
    (DATA_POINTS[:, 1] - (data_slope * DATA_POINTS[:, 0] + data_intercept)) ** 2))
