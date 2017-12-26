from numpy import mean
from pandas import read_csv
from sklearn.linear_model import LogisticRegression
from os.path import dirname

Diabetes = read_csv(dirname(__file__) + "\\" + "diabetes.csv")

inputData = Diabetes.iloc[:, :8]
outputData = Diabetes.iloc[:, 8]

log_model = LogisticRegression()
log_model.fit(inputData, outputData)

training_data_accuracy = mean(log_model.predict(inputData) == outputData)

print("training data accuracy =", training_data_accuracy)
