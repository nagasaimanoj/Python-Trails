import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import confusion_matrix, roc_curve, roc_auc_score
from sklearn.linear_model import LogisticRegression

Diabetes = pd.read_csv("C:\\Users\\saimanoj\\Downloads\\diabetes.csv")

table1 = np.mean(Diabetes, axis=0)
table2 = np.std(Diabetes, axis=0)

inputData = Diabetes.iloc[:, :8]
outputData = Diabetes.iloc[:, 8]

logit1 = LogisticRegression()
logit1.fit(inputData, outputData)
logit1.score(inputData, outputData)

trueInput = Diabetes.ix[Diabetes['Outcome'] == 1].iloc[:, :8]
trueOutput = Diabetes.ix[Diabetes['Outcome'] == 1].iloc[:, 8]

np.mean(logit1.predict(trueInput) == trueOutput)

falseInput = Diabetes.ix[Diabetes['Outcome'] == 0].iloc[:, :8]
falseOutput = Diabetes.ix[Diabetes['Outcome'] == 0].iloc[:, 8]

np.mean(logit1.predict(falseInput) == falseOutput)

confusion_matrix(logit1.predict(inputData), outputData)

fpr, tpr, _ = roc_curve(logit1.predict(inputData),
                        outputData, drop_intermediate=False)

plt.plot(fpr, tpr)

plt.plot([0, 1], [0, 1])
plt.show()

print(roc_auc_score(logit1.predict(inputData), outputData))
