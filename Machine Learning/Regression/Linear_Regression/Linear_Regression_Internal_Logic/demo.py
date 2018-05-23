from numpy import genfromtxt, mean
from matplotlib.pyplot import plot, scatter, show
from os.path import dirname


def print_details(intercept, slope, error):
    print("intercept =", intercept)
    print("slope =", slope)
    print("error =", error)


current_path = dirname(__file__)
data_set = genfromtxt(current_path + "\\" + "data.csv", delimiter=",")

slope = 0
intercept = 0
initial_error = mean(data_set[:, 1] - (slope * data_set[:, 0] + intercept)**2)

print("\nInitial values :")
print_details(intercept, slope, initial_error)

num_iterations = len(data_set) * 10
learning_rate = 1 / (num_iterations * 10)

for i in range(num_iterations):
    current_predection = (slope * data_set[:, 0]) + intercept
    current_error = data_set[:, 1] - current_predection

    xyz = 2 / len(data_set) * current_error
    avg_change = mean(xyz)

    intercept += avg_change * learning_rate

    slope += (avg_change * sum(data_set[:, 0])) * learning_rate

updated_error = mean(data_set[:, 1] - (slope * data_set[:, 0] + intercept))**2

print("\nValues After", num_iterations, " itterations :")
print_details(intercept, slope, updated_error)

scatter(data_set[:, 0], data_set[:, 1])
plot(data_set[:, 0], slope * data_set[:, 0] + intercept)
show()
