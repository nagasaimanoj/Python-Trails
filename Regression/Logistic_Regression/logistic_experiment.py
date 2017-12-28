from os.path import dirname

from matplotlib.pyplot import plot, show
from numpy import mean, std
from pandas import read_csv
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, roc_curve

diabetes_data = read_csv(dirname(__file__) + "\\" + "diabetes.csv")

# table1 = mean(diabetes_data, axis=0)
# table2 = std(diabetes_data, axis=0)

inputData = diabetes_data.iloc[:, :8]
outputData = diabetes_data.iloc[:, 8]

log_model = LogisticRegression()
log_model.fit(inputData, outputData)
# log_model.score(inputData, outputData)

# trueInput = diabetes_data.ix[diabetes_data['Outcome'] == 1].iloc[:, :8]
# trueOutput = diabetes_data.ix[diabetes_data['Outcome'] == 1].iloc[:, 8]

# mean(log_model.predict(trueInput) == trueOutput)

# falseInput = diabetes_data.ix[diabetes_data['Outcome'] == 0].iloc[:, :8]
# falseOutput = diabetes_data.ix[diabetes_data['Outcome'] == 0].iloc[:, 8]

# mean(log_model.predict(falseInput) == falseOutput)

# confusion_matrix(log_model.predict(inputData), outputData)

fpr, tpr, _ = roc_curve(log_model.predict(inputData), outputData)

plot(fpr, tpr)

plot([0, 1], [0, 1])
show()
