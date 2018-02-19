from random import randint  # to get random from a given range

from numpy.random import seed

coin = ['heads', 'tails']

print("coin toss = ", coin[randint(0, 1)])

print("np.random = ", seed(12))
