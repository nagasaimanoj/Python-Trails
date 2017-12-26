# genfromtxt will read csv as array & mean will calculate average
from os.path import dirname

from numpy import genfromtxt, mean

# reading csv file as an array
data_points = genfromtxt(dirname(__file__) + "\\" + "data.csv", delimiter=",")

# initialising intercept and slope values as 0
data_intercept, data_slope = 0, 0

# itteration count to 10 times the length of data set
data_num_iterations = len(data_points) * 10

# learning rate to 100th of data set size
learning_rate = 1 / (data_num_iterations * 10)

# running the loop for 10x the length of data to generate accurate slope and intercept
for i in range(data_num_iterations):
    # calculating average change in values when compared with predected and actual values
    avg_change = mean(2 / len(data_points) *
                      (data_points[:, 1] - (data_slope * data_points[:, 0]) + data_intercept))

    # using that average change to adjust intercept
    data_intercept += avg_change * learning_rate

    # using that average change to adjust slope
    data_slope += (avg_change * sum(data_points[:, 0])) * learning_rate

# printing output values one by one
print("intercept =", data_intercept)
print("m =", data_slope)
print("error =", mean(
    (data_points[:, 1] - (data_slope * data_points[:, 0] + data_intercept)) ** 2))
