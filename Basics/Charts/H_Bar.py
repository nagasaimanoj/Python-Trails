from matplotlib import plot, show, subplots

from numpy import random, arange


fig, ax = subplots()

y_data = arange(5)
x_data = 3 + 10 * random.rand(len(y_data))

ax.barh(y_data, x_data)
show()
