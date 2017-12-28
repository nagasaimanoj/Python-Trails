from os.path import dirname

from matplotlib.pyplot import plot, show
from numpy import genfromtxt
from sklearn.svm import OneClassSVM

DATA_SET_1 = genfromtxt(dirname(__file__) + "\\" + "women2.csv", delimiter=",")

DATA_SET_1_PRED = OneClassSVM(nu=0.001, gamma=0.001).fit(
    DATA_SET_1).predict(DATA_SET_1)

NORMAL = DATA_SET_1[DATA_SET_1_PRED == 1]
ABNORMAL = DATA_SET_1[DATA_SET_1_PRED == -1]

plot(NORMAL[:, 0], NORMAL[:, 1], "bx")
plot(ABNORMAL[:, 0], ABNORMAL[:, 1], "ro")
show()
