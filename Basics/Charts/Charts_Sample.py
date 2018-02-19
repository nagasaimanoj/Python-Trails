from matplotlib.pyplot import (legend, plot, scatter, show, title,
                               xlabel, ylabel)

x = [1, 2, 3, 4, 5, 6]
y = [20, 3, 40, 5, 60, 7]
z = [1, 5, 3, 7, 11, 9]

plot(x, y, label="x to y", color="green")
scatter(x, z, label="x to z", color="red")

title("X vs Y & X vs Z")
xlabel("X data")
ylabel("Y & Z data")

legend()
show()
