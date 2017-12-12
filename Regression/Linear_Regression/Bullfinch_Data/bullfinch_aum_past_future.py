from matplotlib import pyplot
from sklearn import linear_model

years = [[2012], [2013], [2014], [2015], [2016], [2017]]
aum_per_year = [0, 0, 0, 5166063.898, 404537126.8, 3322383541]

reg = linear_model.LinearRegression()

for i in range(1, 6):
    next_year = [[int(max(years)[0]) + 1]]
    reg.fit(years, aum_per_year)

    years += next_year
    aum_per_year += list(reg.predict(next_year))

pyplot.plot(years, aum_per_year, marker='o')
pyplot.show()
