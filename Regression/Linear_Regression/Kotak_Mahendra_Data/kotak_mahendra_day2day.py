from matplotlib.pyplot import plot, show
from numpy import append, array
from sklearn.linear_model import LinearRegression

from quandl import get

KOTAK_csv_file = list(get("NSE/KOTAKNIFTY",
                          authtoken="qAsk6MJV-VXWMqoWDJQk", returns='numpy'))

KOTAK_x_data = []
KOTAK_y_data = []

for i in range(len(KOTAK_csv_file)):
    KOTAK_x_data.append(KOTAK_csv_file[i][0])
    KOTAK_y_data.append(KOTAK_csv_file[i][7])

min_date = min(KOTAK_x_data)

x_data_2 = array([], dtype=int)

for i in KOTAK_x_data:
    x_data_2 = append(x_data_2, [(i - min_date).days])

x_data_2.shape = (len(x_data_2), 1)

regr = LinearRegression()
regr.fit(x_data_2, KOTAK_y_data)

plot(x_data_2, KOTAK_y_data, marker='o')
plot(x_data_2, regr.predict(x_data_2), marker='o')
show()
