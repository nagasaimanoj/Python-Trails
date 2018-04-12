from csv import reader
from os.path import dirname

from matplotlib.pyplot import plot, show
from numpy import array

if __name__ == "__main__":
    revenue_csv_file = open(dirname(__file__) + "\\" + "revenue.csv")
    revenue_csv_reader = reader(revenue_csv_file)
    revenue_csv_data = array(list(revenue_csv_reader))

    x_data = revenue_csv_data[..., 0]
    y_data = revenue_csv_data[..., 1]

    plot(x_data, y_data, marker='o')

    show()
