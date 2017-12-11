import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression

Diabetes = pd.read_csv("C:\\Users\\saimanoj\\Downloads\\diabetes.csv")

inputData = Diabetes.iloc[:, :8]
outputData = Diabetes.iloc[:, 8]

log_model = LogisticRegression()
log_model.fit(inputData, outputData)

training_data_accuracy = np.mean(log_model.predict(inputData) == outputData)

print("training data accuracy =", training_data_accuracy)

test_input = [[1, 189, 60, 23, 846, 30.1, 0.398, 59],
              [5, 166, 72, 19, 175, 25.8, 0.587, 51],
              [3, 126, 88, 41, 235, 39.3, 0.704, 27],
              [8, 99, 84, 0, 0, 35.4, 0.388, 50],
              [1, 97, 66, 15, 140, 23.2, 0.487, 22]]
test_output = [1, 1, 0, 0, 0]

pred_results = log_model.predict(test_input)

test_data_accuracy = np.mean(test_output == pred_results)

print("test data accuracy =", test_data_accuracy)
