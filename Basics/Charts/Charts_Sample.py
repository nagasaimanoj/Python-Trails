from matplotlib.pyplot import (grid,  # to have grid in chart
                               legend,  # to show labels of datasets
                               plot,  # to draw lines with datasets
                               scatter,  # to plot dots with datasets
                               show,  # to display populated charts
                               title,  # to show chart's title
                               xlabel,  # to label X-axis
                               ylabel)  # to label Y-axis

# creating x, y, z datasets
x = [1, 2, 3, 4, 5, 6]
y = [20, 3, 40, 5, 60, 7]
z = [1, 5, 3, 7, 11, 9]

# plotting line graph based on x-y & scatter based on x-z
plot(x, y, color="#003B46", label="x to y")
scatter(x, z, color="#F52549", label="x to z")

# naming graph, x-axis & y-axis
title("X vs Y & X vs Z")
xlabel("X data")
ylabel("Y & Z data")

# showing labels, grid and graph
legend()
grid()
show()
