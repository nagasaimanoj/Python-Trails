from numpy import genfromtxt, array


def compute_error_for_line_given_points(b, m, points):
    total_error = 0
    for i in range(0, len(points)):
        x, y = points[i, 0], points[i, 1]
        total_error += (y - (m * x + b)) ** 2
    return total_error / float(len(points))


def step_gradient(b_current, m_current, points, learningRate):
    b_gradient = 0
    m_gradient = 0
    N = float(len(points))
    for i in range(0, len(points)):
        x, y = points[i, 0], points[i, 1]

        y_pred = (m_current * x) + b_current
        avg_change_in_value = (2 / N) * (y - y_pred)

        b_gradient += -(avg_change_in_value)
        m_gradient += -(avg_change_in_value * x)

    new_b = b_current - (learningRate * b_gradient)
    new_m = m_current - (learningRate * m_gradient)

    return [new_b, new_m]


def gradient_descent_runner(points, starting_b, starting_m, learning_rate, num_iterations):
    b = starting_b
    m = starting_m
    for i in range(num_iterations):
        b, m = step_gradient(b, m, array(points), learning_rate)
    return [b, m]


def run():
    points = genfromtxt(
        "C:\\Users\\saimanoj\\Downloads\\data.csv", delimiter=",")
    learning_rate = 0.0001
    initial_b = 0  # initial y-intercept guess
    initial_m = 0  # initial slope guess
    num_iterations = 1000

    print("Initially..,")
    print("b =", initial_b)
    print("m =", initial_m)
    print("error =", compute_error_for_line_given_points(
        initial_b, initial_m, points))

    print("\nRunning...\n")

    [b, m] = gradient_descent_runner(
        points, initial_b, initial_m, learning_rate, num_iterations)

    print("After", num_iterations, "itterations..,")
    print("b =", b)
    print("m =", m)
    print("error =", compute_error_for_line_given_points(b, m, points))


if __name__ == '__main__':
    run()
