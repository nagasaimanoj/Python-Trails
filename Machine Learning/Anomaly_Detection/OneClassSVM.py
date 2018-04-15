from os.path import dirname

from matplotlib.pyplot import plot, show, title
from numpy import array, genfromtxt
from sklearn.svm import OneClassSVM

if __name__ == "__main__":
    DATA_SET_1 = array(
        genfromtxt(dirname(__file__) + "\\" + "women.csv", delimiter=","))

    NU_VAL = 1 / 25
    GAMMA_VAL = 1 / 3500000000

    SVM_MODEL = OneClassSVM(nu=NU_VAL, gamma=GAMMA_VAL)

    SVM_MODEL.fit(DATA_SET_1)
    DATA_SET_1_PRED = SVM_MODEL.predict(DATA_SET_1)

    NORMAL = DATA_SET_1[DATA_SET_1_PRED == 1]
    ABNORMAL = DATA_SET_1[DATA_SET_1_PRED == -1]

    plot(NORMAL[:, 0], NORMAL[:, 1], "bx")
    plot(ABNORMAL[:, 0], ABNORMAL[:, 1], "ro")
    title("gamma = " + str(SVM_MODEL.gamma) + ", nu = " + str(SVM_MODEL.nu))
    show()
