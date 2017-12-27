from os.path import dirname

from matplotlib.pyplot import plot, scatter, show
from numpy import cov, genfromtxt, mean, std

DATA_SET_1 = genfromtxt(dirname(__file__) + "\\" + "file_1.csv", delimiter=",")

X_DATA = DATA_SET_1[:, 0]
Y_DATA = DATA_SET_1[:, 1]

scatter(X_DATA, Y_DATA)

show()

X_DATA_mean = mean(X_DATA)
X_DATA_std = std(X_DATA)

Y_DATA_mean = mean(Y_DATA)
Y_DATA_std = std(Y_DATA)

for i in range(len(X_DATA)):
    if(((X_DATA_mean - X_DATA_std) < X_DATA[i] < (X_DATA_mean + X_DATA_std))or((Y_DATA_mean - Y_DATA_std) < Y_DATA[i] < (Y_DATA_mean + Y_DATA_std))):
        plot(X_DATA[i], Y_DATA[i], 'bx')
    else:
        plot(X_DATA[i], Y_DATA[i], 'ro')

show()

X_DATA_cov = cov(X_DATA)

Y_DATA_cov = cov(Y_DATA)

for i in range(len(X_DATA)):
    if(((X_DATA_mean - X_DATA_cov) < X_DATA[i] < (X_DATA_mean + X_DATA_cov))or((Y_DATA_mean - Y_DATA_cov) < Y_DATA[i] < (Y_DATA_mean + Y_DATA_cov))):
        plot(X_DATA[i], Y_DATA[i], 'bx')
    else:
        plot(X_DATA[i], Y_DATA[i], 'ro')

show()
