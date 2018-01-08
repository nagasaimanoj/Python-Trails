# matplotlib is for plotting graphs
from matplotlib.pyplot import plot, show

# sklearn is for LinearRegression training model
from sklearn.linear_model import LinearRegression

# training input data
years = [[2012], [2013], [2014], [2015], [2016], [2017]]

# training output data
aum_per_year = [0, 0, 0, 5166063.898, 404537126.8, 3322383541]

# getting a linear model for training
reg = LinearRegression()

# predecting aum_values for next 6 years, based on incremental changes, rather then training all & predecting at once
for i in range(1, 6):
    next_year = [[int(max(years)[0]) + 1]]
    reg.fit(years, aum_per_year)

    years += next_year
    aum_per_year += list(reg.predict(next_year))

# plotting actual points & predected future points
plot(years, aum_per_year, marker='o')
show()
