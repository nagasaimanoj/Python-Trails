from matplotlib import pyplot
from numpy import append, array, count_nonzero, unique
from scipy.stats import poisson

# collecting goal_count data per match
FOOTBALL_MATCH_DATA = array([0, 0, 1, 2, 2, 1, 1, 3, 1, 2, 2, 2, 0, 1, 0, 1, 1, 1, 1, 1, 3, 1, 1, 0, 2, 1, 1, 1, 3, 0, 2, 1, 1, 4, 1, 1, 0, 2, 2, 0, 1, 3, 1, 3, 4, 4, 4, 1, 1, 3, 3, 1, 5, 4, 1, 1, 2, 1, 0, 2, 1, 0, 1, 1, 2, 1, 0, 0, 1, 2, 3, 6, 3, 0, 1, 2, 1, 0, 3, 0, 0, 0, 2, 0, 3, 2, 0, 1, 4, 1, 2, 0, 2, 1, 1, 1, 0, 2, 0, 3, 1, 3, 5, 1, 1, 1, 2, 1, 6, 1, 1, 1, 1, 0, 0, 3, 3, 2, 0, 4, 1, 2, 1, 2, 2, 5, 3, 1, 1, 0, 3, 1, 2, 2, 5, 3, 1, 4, 1, 1, 3, 3, 3, 4, 3, 3, 1, 2, 1, 1, 1, 2, 1, 2, 0, 0, 0, 3, 3, 1, 0, 3, 2, 1, 0, 1, 1, 2, 2, 0, 1, 1, 3, 0, 0, 3, 1, 1, 4, 1, 2, 4, 4, 1, 1, 2, 1,
                             0, 2, 1, 3, 2, 0, 2, 3, 0, 3, 1, 2, 2, 1, 3, 0, 1, 0, 4, 0, 3, 4, 1, 2, 0, 2, 2, 1, 1, 2, 2, 2, 3, 1, 0, 1, 1, 1, 0, 2, 0, 1, 0, 3, 0, 6, 2, 1, 1, 2, 1, 0, 2, 2, 2, 2, 0, 1, 0, 2, 1, 2, 0, 3, 1, 2, 1, 1, 2, 4, 3, 3, 3, 1, 2, 3, 3, 0, 0, 3, 1, 0, 3, 3, 2, 2, 2, 1, 4, 1, 0, 3, 2, 1, 1, 2, 0, 1, 2, 2, 3, 0, 0, 1, 2, 0, 1, 2, 1, 2, 3, 2, 4, 2, 3, 1, 1, 3, 0, 1, 4, 0, 1, 4, 0, 3, 2, 3, 0, 3, 2, 4, 1, 2, 0, 1, 4, 2, 2, 0, 0, 1, 4, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 0, 1, 2, 2, 0, 3, 5, 1, 2, 0, 3, 0, 1, 0, 2, 2, 1, 1, 0, 4, 2, 0, 4, 2, 3, 0, 1, 3, 1, 5, 1, 1, 3, 2, 0, 2, 0])


# storing unique goal_counts in x_data and storing predicted values in pred_data
X_DATA = unique(FOOTBALL_MATCH_DATA)
pred_data = poisson.pmf(X_DATA, FOOTBALL_MATCH_DATA.mean())

# counting the No. of times an unique goal_count repeats and storing them in num_count
num_count = []
for i in X_DATA:
    num_count = append(num_count, count_nonzero(FOOTBALL_MATCH_DATA == i))

# replacing count values with their corrosponding occurances in the whole set
num_count = num_count / sum(num_count)

# plotting a graph based on existing data
pyplot.plot(X_DATA, num_count, marker='o')

# plotting a graph based on predected data
pyplot.plot(X_DATA, pred_data, marker='*')

pyplot.show()
