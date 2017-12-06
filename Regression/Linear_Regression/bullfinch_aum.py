import matplotlib.pyplot as plt
from sklearn import linear_model

years = [[2012], [2013], [2014], [2015], [2016], [2017]]
aum_per_year = [0, 0, 0, 5166063.898, 404537126.8, 3322383541]

reg = linear_model.LinearRegression()
reg.fit(years, aum_per_year)

plt.plot(years, aum_per_year, marker='o')

years += [[2018], [2019], [2020]]

plt.plot(years, reg.predict(years), marker='o')
plt.show()
