import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import poisson

match_data = pd.read_csv(
    "C:\\Users\\saimanoj\\Downloads\\E0.csv")[['FTHG']]

plt.hist(match_data.values, range(10), normed=True)

plt.plot(np.arange(0.5, 10.5, 1), poisson.pmf(
    range(10), match_data.mean()[0]), marker='o')

plt.show()
