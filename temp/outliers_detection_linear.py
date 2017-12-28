from os.path import dirname

from matplotlib.pyplot import plot, show, title
from numpy import genfromtxt
from sklearn.svm import OneClassSVM

DATA_SET_1 = genfromtxt(dirname(__file__) + "\\" + "women2.csv", delimiter=",")

DATA_SET_1_LENGTH = len(DATA_SET_1[:, 0])

ERROR_PERC = 0.05
GAMMA_VAL = 7000000

ocs = OneClassSVM(nu=1 / (DATA_SET_1_LENGTH * ERROR_PERC),
                  gamma=1 / (DATA_SET_1_LENGTH * GAMMA_VAL))

ocs.fit(DATA_SET_1)
DATA_SET_1_PRED = ocs.predict(DATA_SET_1)

NORMAL = DATA_SET_1[DATA_SET_1_PRED == 1]
ABNORMAL = DATA_SET_1[DATA_SET_1_PRED == -1]

plot(NORMAL[:, 0], NORMAL[:, 1], "bx")
plot(ABNORMAL[:, 0], ABNORMAL[:, 1], "ro")
title("gamma = " + str(GAMMA_VAL) + ", nu = " + str(ERROR_PERC))
show()

print(ocs)
