from matplotlib.pyplot import plot, show
from numpy import array
from sklearn.linear_model import LinearRegression

input_data = array([[2012, 5869.4, -117], [2013, 4925, -84], [2014, 64, -51],
                    [2015, 9921, -18], [2016, 72, 15], [2017, 199, 48]])

output_data = [123, 365, 365, 365, 320, 273]

lm = LinearRegression()
lm.fit(input_data, output_data)

pred_out = lm.predict(input_data)

plot(input_data[:, 0], output_data)
plot(input_data[:, 0], pred_out, marker='*')
show()
