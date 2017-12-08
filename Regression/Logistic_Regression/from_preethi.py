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

# True positive
trueInput = Diabetes.ix[Diabetes['Outcome'] == 1].iloc[:, :8]
trueOutput = Diabetes.ix[Diabetes['Outcome'] == 1].iloc[:, 8]

# True positive rate
np.mean(logit1.predict(trueInput) == trueOutput)

# True negative
falseInput = Diabetes.ix[Diabetes['Outcome'] == 0].iloc[:, :8]
falseOutput = Diabetes.ix[Diabetes['Outcome'] == 0].iloc[:, 8]

# True negative rate
np.mean(logit1.predict(falseInput) == falseOutput)

confusion_matrix(logit1.predict(inputData), outputData)
# Computing false and true positive rates
fpr, tpr, _ = roc_curve(logit1.predict(inputData),
                        outputData, drop_intermediate=False)

plt.figure()
# Adding the ROC
plt.plot(fpr, tpr, color='red',
         lw=2, label='ROC curve')
# Random FPR and TPR
plt.plot([0, 1], [0, 1], color='blue', lw=2, linestyle='--')
##Title and label
plt.xlabel('FPR')
plt.ylabel('TPR')
plt.title('ROC curve')
plt.show()

roc_auc_score(logit1.predict(inputData), outputData)
plt.figure()


