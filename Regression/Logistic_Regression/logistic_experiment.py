from os.path import dirname

from matplotlib import pyplot
from numpy import mean, std
from pandas import read_csv
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, roc_curve

Diabetes = read_csv(dirname(__file__) + "\\" + "diabetes.csv")

# table1 = mean(Diabetes, axis=0)
# table2 = std(Diabetes, axis=0)

inputData = Diabetes.iloc[:, :8]
outputData = Diabetes.iloc[:, 8]

log_model = LogisticRegression()
log_model.fit(inputData, outputData)
# log_model.score(inputData, outputData)

# trueInput = Diabetes.ix[Diabetes['Outcome'] == 1].iloc[:, :8]
# trueOutput = Diabetes.ix[Diabetes['Outcome'] == 1].iloc[:, 8]

# mean(log_model.predict(trueInput) == trueOutput)

# falseInput = Diabetes.ix[Diabetes['Outcome'] == 0].iloc[:, :8]
# falseOutput = Diabetes.ix[Diabetes['Outcome'] == 0].iloc[:, 8]

# mean(log_model.predict(falseInput) == falseOutput)

# confusion_matrix(log_model.predict(inputData), outputData)

fpr, tpr, _ = roc_curve(log_model.predict(inputData), outputData)

pyplot.plot(fpr, tpr)

pyplot.plot([0, 1], [0, 1])
pyplot.show()
