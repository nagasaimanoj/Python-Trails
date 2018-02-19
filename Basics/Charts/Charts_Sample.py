from matplotlib.pyplot import (grid, legend, plot, scatter, show, title,
                               xlabel, ylabel)

x = [1, 2, 3, 4, 5, 6]
y = [20, 3, 40, 5, 60, 7]
z = [1, 5, 3, 7, 11, 9]

plot(x, y, label="x to y")
plot(x, z, label="x to z")
scatter(x, z, label="x to z")

title("X vs Z")
xlabel("X data")
ylabel("Z data")

grid(True)
legend()

show()