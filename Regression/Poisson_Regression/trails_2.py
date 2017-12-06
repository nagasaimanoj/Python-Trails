import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import poisson

match_data = pd.read_csv(
    "http://www.football-data.co.uk/mmz4281/1617/E0.csv")[['FTHG', 'FTAG']]

plt.hist(match_data.values, range(9), normed=True,
         color=['#77AA77', '#AAAAAA'], label=['Home', 'Away'])

predicted_data = np.array([])

for i in range(8):
    for j in range(2):
        predicted_data = np.append(
            predicted_data, poisson.pmf(i, match_data.mean()[j]))

predicted_data.shape = (8, 2)

goal_number = [i + 0.5 for i in range(8)]

plt.plot(goal_number, predicted_data[:, 0],
         marker='o', label="Home", color='#FF88c0')
plt.plot(goal_number, predicted_data[:, 1],
         marker='o', label="Away", color='#1e88e5')

leg = plt.legend(loc='upper right', fontsize=13, ncol=2)
leg.set_title("Poisson           Actual        ",
              prop={'size': '14'})

plt.xlabel("Goals per Match")
plt.ylabel("Goal Probability")

plt.title("Number of Goals per Match", size=15, fontweight='bold')

plt.show()
