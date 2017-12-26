import numpy as np
from random import randint

coin = ['heads', 'tails']

print("coin toss = ", coin[randint(0, 1)])

print("np.random = ", np.random.seed(12))