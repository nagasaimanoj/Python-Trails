import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import confusion_matrix, roc_curve
from sklearn.linear_model import LogisticRegression

Diabetes = pd.read_csv("C:\\Users\\saimanoj\\Downloads\\diabetes.csv")

# table1 = np.mean(Diabetes, axis=0)
# table2 = np.std(Diabetes, axis=0)

inputData = Diabetes.iloc[:, :8]
outputData = Diabetes.iloc[:, 8]

log_model = LogisticRegression()
log_model.fit(inputData, outputData)
# log_model.score(inputData, outputData)

# trueInput = Diabetes.ix[Diabetes['Outcome'] == 1].iloc[:, :8]
# trueOutput = Diabetes.ix[Diabetes['Outcome'] == 1].iloc[:, 8]

# np.mean(log_model.predict(trueInput) == trueOutput)

# falseInput = Diabetes.ix[Diabetes['Outcome'] == 0].iloc[:, :8]
# falseOutput = Diabetes.ix[Diabetes['Outcome'] == 0].iloc[:, 8]

# np.mean(log_model.predict(falseInput) == falseOutput)

# confusion_matrix(log_model.predict(inputData), outputData)

fpr, tpr, _ = roc_curve(log_model.predict(inputData), outputData)

plt.plot(fpr, tpr)

plt.plot([0, 1], [0, 1])
plt.show()
