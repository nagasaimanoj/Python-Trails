import matplotlib.pyplot as chart
import numpy as np

x = [1, 2, 3, 4, 5, 6]
y = [20, 3, 40, 5, 60, 7]
z = [1, 5, 3, 7, 11, 9]

chart = chart
chart = chart

chart.xlabel("X data")
chart.ylabel("Y data")
chart.title("X vs Y")
chart.grid(True)

chart.plot(x, y)
chart.show()

chart.xlabel("X data")
chart.ylabel("Z data")
chart.title("X vs Z")
chart.grid(True)

chart.plot(x, z)
chart.show()

input("\n\n----------\nHit enter to close\n")