from matplotlib.pyplot import grid, plot, show, title, xlabel, ylabel

x = [1, 2, 3, 4, 5, 6]
y = [20, 3, 40, 5, 60, 7]
z = [1, 5, 3, 7, 11, 9]

xlabel("X data")
ylabel("Y data")
title("X vs Y")
grid(True)

plot(x, y)
show()

xlabel("X data")
ylabel("Z data")
title("X vs Z")
grid(True)

plot(x, z)
show()
