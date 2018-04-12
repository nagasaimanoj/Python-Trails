from matplotlib.pyplot import (grid, legend, plot, scatter, show, title,
                               xlabel, ylabel)

if __name__ == "__main__":
    x = [1, 2, 3, 4, 5, 6]
    y = [20, 3, 40, 5, 60, 7]
    z = [1, 5, 3, 7, 11, 9]

    plot(x, y, color="#003B46", label="x to y")
    scatter(x, z, color="#F52549", label="x to z")

    title("X vs Y & X vs Z")
    xlabel("X data")
    ylabel("Y & Z data")

    legend()
    grid()
    show()
