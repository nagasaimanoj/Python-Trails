from matplotlib import pyplot
from sklearn.linear_model import LinearRegression

years = [[2012], [2013], [2014], [2015], [2016], [2017]]
aum_per_year = [0, 0, 0, 5166063.898, 404537126.8, 3322383541]

reg = LinearRegression()
reg.fit(years, aum_per_year)

pyplot.plot(years, aum_per_year, marker='o')

years += [[2018], [2019], [2020]]

pyplot.plot(years, reg.predict(years), marker='o')
pyplot.show()
