import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import poisson

# collecting goal_count data per match
match_data = np.array(['Zero', 'Zero', 'one', 'two', 'two', 'one', 'one', 'three', 'one', 'two', 'two', 'two', 'Zero', 'one', 'Zero', 'one', 'one', 'one', 'one', 'one', 'three', 'one', 'one', 'Zero', 'two', 'one', 'one', 'one', 'three', 'Zero', 'two', 'one', 'one', 'four', 'one', 'one', 'Zero', 'two', 'two', 'Zero', 'one', 'three', 'one', 'three', 'four', 'four', 'four', 'one', 'one', 'three', 'three', 'one', 'five', 'four', 'one', 'one', 'two', 'one', 'Zero', 'two', 'one', 'Zero', 'one', 'one', 'two', 'one', 'Zero', 'Zero', 'one', 'two', 'three', 'six', 'three', 'Zero', 'one', 'two', 'one', 'Zero', 'three', 'Zero', 'Zero', 'Zero', 'two', 'Zero', 'three', 'two', 'Zero', 'one', 'four', 'one', 'two', 'Zero', 'two', 'one', 'one', 'one', 'Zero', 'two', 'Zero', 'three', 'one', 'three', 'five', 'one', 'one', 'one', 'two', 'one', 'six', 'one', 'one', 'one', 'one', 'Zero', 'Zero', 'three', 'three', 'two', 'Zero', 'four', 'one', 'two', 'one', 'two', 'two', 'five', 'three', 'one', 'one', 'Zero', 'three', 'one', 'two', 'two', 'five', 'three', 'one', 'four', 'one', 'one', 'three', 'three', 'three', 'four', 'three', 'three', 'one', 'two', 'one', 'one', 'one', 'two', 'one', 'two', 'Zero', 'Zero', 'Zero', 'three', 'three', 'one', 'Zero', 'three', 'two', 'one', 'Zero', 'one', 'one', 'two', 'two', 'Zero', 'one', 'one', 'three', 'Zero', 'Zero', 'three', 'one', 'one', 'four', 'one', 'two', 'four', 'four', 'one', 'one', 'two', 'one', 'Zero', 'two', 'one',
                       'three', 'two', 'Zero', 'two', 'three', 'Zero', 'three', 'one', 'two', 'two', 'one', 'three', 'Zero', 'one', 'Zero', 'four', 'Zero', 'three', 'four', 'one', 'two', 'Zero', 'two', 'two', 'one', 'one', 'two', 'two', 'two', 'three', 'one', 'Zero', 'one', 'one', 'one', 'Zero', 'two', 'Zero', 'one', 'Zero', 'three', 'Zero', 'six', 'two', 'one', 'one', 'two', 'one', 'Zero', 'two', 'two', 'two', 'two', 'Zero', 'one', 'Zero', 'two', 'one', 'two', 'Zero', 'three', 'one', 'two', 'one', 'one', 'two', 'four', 'three', 'three', 'three', 'one', 'two', 'three', 'three', 'Zero', 'Zero', 'three', 'one', 'Zero', 'three', 'three', 'two', 'two', 'two', 'one', 'four', 'one', 'Zero', 'three', 'two', 'one', 'one', 'two', 'Zero', 'one', 'two', 'two', 'three', 'Zero', 'Zero', 'one', 'two', 'Zero', 'one', 'two', 'one', 'two', 'three', 'two', 'four', 'two', 'three', 'one', 'one', 'three', 'Zero', 'one', 'four', 'Zero', 'one', 'four', 'Zero', 'three', 'two', 'three', 'Zero', 'three', 'two', 'four', 'one', 'two', 'Zero', 'one', 'four', 'two', 'two', 'Zero', 'Zero', 'one', 'four', 'one', 'Zero', 'one', 'Zero', 'Zero', 'Zero', 'Zero', 'Zero', 'Zero', 'Zero', 'one', 'two', 'two', 'Zero', 'one', 'two', 'two', 'Zero', 'three', 'five', 'one', 'two', 'Zero', 'three', 'Zero', 'one', 'Zero', 'two', 'two', 'one', 'one', 'Zero', 'four', 'two', 'Zero', 'four', 'two', 'three', 'Zero', 'one', 'three', 'one', 'five', 'one', 'one', 'three', 'two', 'Zero', 'two', 'Zero'])

# storing unique goal_counts in x_data and storing predicted values in pred_data
x_data = np.unique(match_data)
# match_data.mean() = 1.59736842105
pred_data = poisson.pmf(x_data, 1.59736842105)

# counting the No. of times an unique goal_count repeats and storing them in num_count
num_count = []
for i in x_data:
    num_count = np.append(num_count, np.count_nonzero(match_data == i))

# replacing count values with their corrosponding occurances in the whole set
num_count = num_count / sum(num_count)

# plotting a graph based on existing data
plt.plot(x_data, num_count, marker='o')

# plotting a graph based on predected data
plt.plot(x_data, pred_data, marker='*')

plt.show()