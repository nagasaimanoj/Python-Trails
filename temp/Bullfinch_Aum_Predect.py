from sklearn import linear_model
import matplotlib.pyplot as plt

input_data = [[2012, 5869.4, -117], [2013, 4925, -84], [2014, 64, -51],
              [2015, 9921, -18], [2016, 72, 15], [2017, 199, 48]]

output_data = [123, 365, 365, 365, 320, 273]


lm = linear_model.LinearRegression()
lm.fit(input_data, output_data)

pred_out = lm.predict(input_data)

plt.plot(range(len(output_data)), output_data)
plt.plot(range(len(pred_out)), pred_out, marker='o')
plt.show()
