import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import poisson

match_data = pd.read_csv(
    "C:\\Users\\saimanoj\\Downloads\\E0.csv")[['FTHG', 'FTAG']]

plt.hist(match_data.values, range(10), normed=True,
         color=['#77AA77', '#AAAAAA'], label=['Home', 'Away'])

plt.plot(np.arange(0.5, 10.5, 1), poisson.pmf(range(10), match_data.mean()[0]),
         marker='o', label="Home", color='#FF88c0')

plt.plot(np.arange(0.5, 10.5, 1), poisson.pmf(range(10), match_data.mean()[1]),
         marker='o', label="Away", color='#1e88e5')

plt.title("Number of Goals per Match", size=15, fontweight='bold')
plt.xlabel("Goals per Match")
plt.ylabel("Goal Probability")
plt.legend(loc='upper right', fontsize=13, ncol=2).set_title(
    "Poisson          Actual       ", prop={'size': '14'})

plt.show()
