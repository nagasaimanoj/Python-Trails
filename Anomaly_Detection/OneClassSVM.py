from os.path import dirname

from matplotlib.pyplot import plot, show, title
from numpy import genfromtxt
from sklearn.svm import OneClassSVM

DATA_SET_1 = genfromtxt(dirname(__file__) + "\\" + "women.csv", delimiter=",")
DATA_SET_1_LENGTH = len(DATA_SET_1[:, 0])

NU_VAL = 0.05
GAMMA_VAL = 7000000

SVM_MODEL = OneClassSVM(nu=1 / (DATA_SET_1_LENGTH * NU_VAL),
                        gamma=1 / (DATA_SET_1_LENGTH * GAMMA_VAL))

SVM_MODEL.fit(DATA_SET_1)
DATA_SET_1_PRED = SVM_MODEL.predict(DATA_SET_1)

NORMAL = DATA_SET_1[DATA_SET_1_PRED == 1]
ABNORMAL = DATA_SET_1[DATA_SET_1_PRED == -1]

plot(NORMAL[:, 0], NORMAL[:, 1], "bx")
plot(ABNORMAL[:, 0], ABNORMAL[:, 1], "ro")
title("gamma = " + str(SVM_MODEL.gamma) + ", nu = " + str(SVM_MODEL.nu))
show()
