from os.path import dirname

from matplotlib import pyplot
from numpy import arange, asarray, cov, genfromtxt, mean, nditer, where
from scipy.stats import multivariate_normal
from sklearn import svm
from sklearn.metrics import f1_score

DATA_SET_1 = genfromtxt(dirname(__file__) + "\\" +
                        "tr_server_data.csv", delimiter=",")
DATA_SET_2 = genfromtxt(dirname(__file__) + "\\" +
                        "cv_server_data.csv", delimiter=",")
DATA_SET_3 = genfromtxt(dirname(__file__) + "\\" +
                        "gt_server_data.csv", delimiter=",")

pyplot.plot(DATA_SET_1[:, 0], DATA_SET_1[:, 1], "bx")
pyplot.title("raw data")
pyplot.show()

N_TRAINING_SAMPLES = DATA_SET_1.shape[0]
N_DIM = DATA_SET_1.shape[1]

MU, SIGMA = mean(DATA_SET_1, axis=0), cov(DATA_SET_1.T)

DATA_SET_1_P = multivariate_normal(mean=MU, cov=SIGMA).pdf(DATA_SET_1)
DATA_SET_1_P_CV = multivariate_normal(mean=MU, cov=SIGMA).pdf(DATA_SET_2)

ep, fscore, f = 0, 0, 0
for epsilon in nditer(arange(min(DATA_SET_1_P_CV), max(DATA_SET_1_P_CV), (max(DATA_SET_1_P_CV) - min(DATA_SET_1_P_CV)) / 1000)):
    predictions = (DATA_SET_1_P_CV < epsilon)
    f = f1_score(DATA_SET_3, predictions, average="binary")
    if f > fscore:
        fscore = f
        ep = epsilon

OUTLIERS = asarray(where(DATA_SET_1_P < ep))

pyplot.plot(DATA_SET_1[:, 0], DATA_SET_1[:, 1], "bx")
pyplot.plot(DATA_SET_1[OUTLIERS, 0], DATA_SET_1[OUTLIERS, 1], "ro")
pyplot.title("outliers")
pyplot.show()

CLF = svm.OneClassSVM(nu=0.05, kernel="rbf", gamma=0.1)
CLF.fit(DATA_SET_1)

DATA_SET_1_PRED = CLF.predict(DATA_SET_1)

NORMAL = DATA_SET_1[DATA_SET_1_PRED == 1]
ABNORMAL = DATA_SET_1[DATA_SET_1_PRED == -1]

pyplot.plot(NORMAL[:, 0], NORMAL[:, 1], "bx")
pyplot.plot(ABNORMAL[:, 0], ABNORMAL[:, 1], "ro")
pyplot.title("abnormals")
pyplot.show()
