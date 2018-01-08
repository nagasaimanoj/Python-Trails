# dirname gives current file path
from os.path import dirname

# genfromtxt will read csv as array & mean will calculate average
from numpy import genfromtxt, mean

# reading csv file as an array
DATA_POINTS = genfromtxt(dirname(__file__) + "\\" + "data.csv", delimiter=",")

# initialising intercept and slope values as 0
data_intercept, data_slope = 0, 0

# itteration count to 10 times the length of data set
data_num_iterations = len(DATA_POINTS) * 10

# learning rate to 100th of data set size
learning_rate = 1 / data_num_iterations / 10

# running the loop for 10x the length of data to generate accurate slope and intercept
for i in range(data_num_iterations):
    # calculating average change in values when compared with predected and actual values
    avg_change = mean(2 / len(DATA_POINTS) *
                      (DATA_POINTS[:, 1] - data_slope * DATA_POINTS[:, 0] + data_intercept))

    # using that average change to adjust intercept
    data_intercept += avg_change * learning_rate

    # using that average change to adjust slope
    data_slope += sum(DATA_POINTS[:, 0]) * avg_change * learning_rate

# printing output values one by one
print("intercept =", data_intercept)
print("slope =", data_slope)
print("average error =", mean(
    (DATA_POINTS[:, 1] - (data_slope * DATA_POINTS[:, 0] + data_intercept)) ** 2))
