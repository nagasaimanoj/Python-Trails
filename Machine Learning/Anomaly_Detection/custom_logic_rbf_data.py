from os.path import dirname

from matplotlib.pyplot import plot, show
from numpy import array, genfromtxt, mean, std
if __name__ == "__main__":
    DATA_SET = genfromtxt(
        dirname(__file__) + "//" + "women.csv", delimiter=",")

    X_DATA = DATA_SET[:, 0]
    Y_DATA = DATA_SET[:, 1]

    X_MEAN = mean(X_DATA)
    Y_MEAN = mean(Y_DATA)

    X_STD = std(X_DATA)
    Y_STD = std(Y_DATA)

    X_UPPER = X_MEAN + X_STD + X_STD
    X_LOWER = X_MEAN - X_STD - X_STD

    Y_UPPER = Y_MEAN + Y_STD + Y_STD
    Y_LOWER = Y_MEAN - Y_STD - Y_STD

    for i in range(len(X_DATA)):
        if (X_LOWER < X_DATA[i] < X_UPPER and Y_LOWER < Y_DATA[i] < Y_UPPER):
            plot(X_DATA[i], Y_DATA[i], 'bx')
        else:
            plot(X_DATA[i], Y_DATA[i], 'rx')

    POINTS = array([[X_LOWER, Y_LOWER], [X_UPPER, Y_LOWER], [X_UPPER, Y_UPPER],
                    [X_LOWER, Y_UPPER], [X_LOWER, Y_LOWER]])

    BOUNDARY = plot(POINTS[:, 0], POINTS[:, 1], color="red", label='Boundary')

    X_RANGE_LINE = plot([X_MEAN, X_MEAN], [Y_LOWER, Y_UPPER], color="orange")
    Y_RANGE_LINE = plot([X_LOWER, X_UPPER], [Y_MEAN, Y_MEAN], color="orange")

    show()
