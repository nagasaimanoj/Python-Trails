from numpy import genfromtxt


points = genfromtxt(
    "C:\\Users\\saimanoj\\Downloads\\data.csv", delimiter=",")

b, m = 0, 0
num_iterations = 1000
learning_rate = 0.0001

for i in range(num_iterations):
    b_gradient = 0
    m_gradient = 0

    for i in range(0, len(points)):
        x, y = points[i, 0], points[i, 1]

        avg_change = (2 / len(points)) * (y - (m * x) + b)

        b_gradient += -avg_change
        m_gradient += -avg_change * x

    b -= learning_rate * b_gradient
    m -= learning_rate * m_gradient

print("b =", b)
print("m =", m)
print("error =", sum(
    (points[:, 1] - (m * points[:, 0] + b)) ** 2) / float(len(points)))
