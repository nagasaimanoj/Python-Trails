import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn
from scipy.stats import poisson, skellam

epl_1617 = pd.read_csv("http://www.football-data.co.uk/mmz4281/1617/E0.csv")
epl_1617 = epl_1617[['HomeTeam', 'AwayTeam', 'FTHG', 'FTAG']]
epl_1617 = epl_1617.rename(columns={'FTHG': 'HomeGoals', 'FTAG': 'AwayGoals'})
epl_1617.head()
epl_1617 = epl_1617[:-10]
epl_1617.mean()
# construct Poisson  for each mean goals value
poisson_pred = np.column_stack(
    [[poisson.pmf(i, epl_1617.mean()[j]) for i in range(8)] for j in range(2)])

# plot histogram of actual goals
plt.hist(epl_1617[['HomeGoals', 'AwayGoals']].values, range(9),
         alpha=0.7, label=['Home', 'Away'], normed=True, color=["#FFA07A", "#20B2AA"])

# add lines for the Poisson distributions
pois1, = plt.plot([i - 0.5 for i in range(1, 9)], poisson_pred[:, 0],
                  linestyle='-', marker='o', label="Home", color='#CD5C5C')
pois2, = plt.plot([i - 0.5 for i in range(1, 9)], poisson_pred[:, 1],
                  linestyle='-', marker='o', label="Away", color='#006400')

leg = plt.legend(loc='upper right', fontsize=13, ncol=2)
leg.set_title("Poisson           Actual        ",
              prop={'size': '14', 'weight': 'bold'})

plt.xticks([i - 0.5 for i in range(1, 9)], [i for i in range(9)])
plt.xlabel("Goals per Match", size=13)
plt.ylabel("Proportion of Matches", size=13)
plt.title("Number of Goals per Match (EPL 2016/17 Season)",
          size=14, fontweight='bold')
plt.ylim([-0.004, 0.4])
plt.tight_layout()
plt.show()
