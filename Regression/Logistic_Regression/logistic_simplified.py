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