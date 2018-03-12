from os.path import dirname

from matplotlib.pyplot import hist, legend, plot, show, title, xlabel, ylabel
from numpy import arange
from pandas import read_csv
from scipy.stats import poisson

football_match_data = read_csv(
    dirname(__file__) + "\\" + "E0.csv")[['FTHG', 'FTAG']]

hist(football_match_data.values, range(10), normed=True,
     color=['#77AA77', '#AAAAAA'], label=['Home', 'Away'])

football_match_x_axis = arange(0.5, 10.5, 1)

plot(football_match_x_axis, poisson.pmf(range(10), football_match_data.mean()[0]),
     marker='o', label="Home", color='#FF88c0')

plot(football_match_x_axis, poisson.pmf(range(10), football_match_data.mean()[1]),
     marker='o', label="Away", color='#1e88e5')

title("Number of Goals per Match", size=15, fontweight='bold')
xlabel("Goals per Match")
ylabel("Goal Probability")
legend(loc='upper right', fontsize=13, ncol=2).set_title(
    "Poisson          Actual       ", prop={'size': '14'})

show()
