from pandas import read_csv
from matplotlib import pyplot
from numpy import arange
from scipy.stats import poisson

# collecting foot ball match data from a CSV file
match_data = read_csv(
    "C:\\Users\\saimanoj\\Downloads\\E0.csv")[['FTHG', 'FTAG']]

# plotting a histogram based on actual data
pyplot.hist(match_data.values, range(10), normed=True,
            color=['#77AA77', '#AAAAAA'], label=['Home', 'Away'])

# generating an array of values for x-axis
x_axis = arange(0.5, 10.5, 1)

# plotting a line chart for predected home runs based on actual data
pyplot.plot(x_axis, poisson.pmf(range(10), match_data.mean()[0]),
            marker='o', label="Home", color='#FF88c0')

# plotting a line chart for predected away runs based on actual data
pyplot.plot(x_axis, poisson.pmf(range(10), match_data.mean()[1]),
            marker='o', label="Away", color='#1e88e5')

# decorating the chart with title and dimension details
pyplot.title("Number of Goals per Match", size=15, fontweight='bold')
pyplot.xlabel("Goals per Match")
pyplot.ylabel("Goal Probability")
pyplot.legend(loc='upper right', fontsize=13, ncol=2).set_title(
    "Poisson          Actual       ", prop={'size': '14'})

pyplot.show()
