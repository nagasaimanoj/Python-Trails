from numpy import genfromtxt, mean

points = genfromtxt("C:\\Users\\saimanoj\\Downloads\\data.csv", delimiter=",")

b, m = 0, 0
num_iterations = len(points) * 10
learning_rate = 1 / (num_iterations * 10)

for i in range(num_iterations):

    avg_change = mean(2 / len(points) *
                      (points[:, 1] - (m * points[:, 0]) + b))

    b += avg_change * learning_rate
    m += (avg_change * sum(points[:, 0])) * learning_rate

print("b =", b)
print("m =", m)
print("error =", mean((points[:, 1] - (m * points[:, 0] + b)) ** 2))
