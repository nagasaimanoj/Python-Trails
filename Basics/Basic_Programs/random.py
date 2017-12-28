from random import randint

from numpy.random import seed

coin = ['heads', 'tails']

print("coin toss = ", coin[randint(0, 1)])

print("np.random = ", seed(12))
