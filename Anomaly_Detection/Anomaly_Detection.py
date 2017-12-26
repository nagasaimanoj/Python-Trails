from matplotlib import pyplot
from numpy import arange, asarray, cov, genfromtxt, mean, nditer, where
from scipy.stats import multivariate_normal
from sklearn import svm
from sklearn.metrics import f1_score
from os.path import dirname

data_set_1 = genfromtxt(dirname(__file__) + "\\" +
                        "tr_server_data.csv", delimiter=",")
data_set_2 = genfromtxt(dirname(__file__) + "\\" +
                        "cv_server_data.csv", delimiter=",")
data_set_3 = genfromtxt(dirname(__file__) + "\\" +
                        "gt_server_data.csv", delimiter=",")

pyplot.plot(data_set_1[:, 0], data_set_1[:, 1], "bx")
pyplot.title("raw data")
pyplot.show()

n_training_samples = data_set_1.shape[0]
n_dim = data_set_1.shape[1]

mu, sigma = mean(data_set_1, axis=0), cov(data_set_1.T)

p = multivariate_normal(mean=mu, cov=sigma).pdf(data_set_1)
p_cv = multivariate_normal(mean=mu, cov=sigma).pdf(data_set_2)

ep, fscore, f = 0, 0, 0
for epsilon in nditer(arange(min(p_cv), max(p_cv), (max(p_cv) - min(p_cv)) / 1000)):
    predictions = (p_cv < epsilon)
    f = f1_score(data_set_3, predictions, average="binary")
    if f > fscore:
        fscore = f
        ep = epsilon

outliers = asarray(where(p < ep))

pyplot.plot(data_set_1[:, 0], data_set_1[:, 1], "bx")
pyplot.plot(data_set_1[outliers, 0], data_set_1[outliers, 1], "ro")
pyplot.title("outliers")
pyplot.show()

clf = svm.OneClassSVM(nu=0.05, kernel="rbf", gamma=0.1)
clf.fit(data_set_1)

pred = clf.predict(data_set_1)

normal = data_set_1[pred == 1]
abnormal = data_set_1[pred == -1]

pyplot.plot(normal[:, 0], normal[:, 1], "bx")
pyplot.plot(abnormal[:, 0], abnormal[:, 1], "ro")
pyplot.title("abnormals")
pyplot.show()
