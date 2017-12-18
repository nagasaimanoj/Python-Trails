from numpy import genfromtxt


points = genfromtxt(
    "C:\\Users\\saimanoj\\Downloads\\data.csv", delimiter=",")

b, m = 0, 0
num_iterations = 1000
learning_rate = 0.0001

for i in range(num_iterations):
    b_gradient = 0
    m_gradient = 0
    N = float(len(points))

    for i in range(0, len(points)):
        x, y = points[i, 0], points[i, 1]

        avg_change_in_value = (2 / N) * (y - (m * x) + b)

        b_gradient += -avg_change_in_value
        m_gradient += -avg_change_in_value * x

    b -= learning_rate * b_gradient
    m -= learning_rate * m_gradient

total_error = 0
for i in range(0, len(points)):
    x, y = points[i, 0], points[i, 1]
    total_error += (y - (m * x + b)) ** 2

print("b =", b)
print("m =", m)
print("error =", total_error / float(len(points)))
