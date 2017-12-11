import matplotlib.pyplot as plt
from sklearn import linear_model

year = [[2010], [2015], [2016], [2017]]
revenue_amt = [149431603257, 12421.79, 291987535.37, 7059254217.30]

reg = linear_model.LinearRegression()
reg.fit(year, revenue_amt)

plt.plot(year, revenue_amt, marker='o')

for i in range(5):
    year += [[max(year[len(year) - 1]) + 1]]

plt.plot(year, reg.predict(year), marker='o')

plt.show()
