from matplotlib.pyplot import (plot,  # to draw lines with datasets
                               scatter,  # to plot dots with datasets
                               show)  # to display populated charts
from sklearn.linear_model import LinearRegression  # linear regression model

# training data set
training_input = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11], [12, 13, 14],
                  [15, 16, 17], [18, 19, 20], [21, 22, 23], [24, 25, 26], [27, 28, 29]]
training_output = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# linear regression model
reg = LinearRegression()

# training the model using training data set
reg.fit(training_input, training_output)

# generating a test data set
test_input = training_input + [[30, 31, 32], [33, 34, 35], [36, 37, 38]]

# plotting graphs using actual data & predected data
scatter(range(len(training_input)), training_output)
plot(range(len(test_input)), reg.predict(test_input), marker="*")
show()
