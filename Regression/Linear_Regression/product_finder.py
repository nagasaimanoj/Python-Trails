import matplotlib.pyplot as plt
from sklearn import linear_model
import numpy as np

training_input = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10],
                  [2, 1], [2, 2], [2, 3], [2, 4], [2, 5], [2, 6], [2, 7], [2, 8], [2, 9], [2, 10],
                  [3, 1], [3, 2], [3, 3], [3, 4], [3, 5], [3, 6], [3, 7], [3, 8], [3, 9], [3, 10],
                  [4, 1], [4, 2], [4, 3], [4, 4], [4, 5], [4, 6], [4, 7], [4, 8], [4, 9], [4, 10],
                  [5, 1], [5, 2], [5, 3], [5, 4], [5, 5], [5, 6], [5, 7], [5, 8], [5, 9], [5, 10]]
training_output = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                   2, 4, 6, 8, 10, 12, 14, 16, 18, 20,
                   3, 6, 9, 12, 15, 18, 21, 24, 27, 30,
                   4, 8, 12, 16, 20, 24, 28, 32, 36, 40,
                   5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

# training the model using linear regression
reg = linear_model.LinearRegression()
reg.fit(training_input, training_output)

# plotting graphs using actual data & our predections
plt.plot(range(len(training_input)), training_output, marker="o")
plt.show()

print(reg.predict([[1, 2]]))
