from matplotlib.pyplot import legend, plot, show
from numpy import asarray, random
from tensorflow import (Session, Variable, add, global_variables_initializer,
                        multiply, placeholder, pow, reduce_sum, train)

# Parameters
learning_rate = 0.01
training_epochs = 1000
display_step = 50

# Training Data
train_X = asarray([3.3, 4.4, 5.5, 6.71, 6.93, 4.168, 9.779, 6.182, 7.59, 2.167,
                   7.042, 10.791, 5.313, 7.997, 5.654, 9.27, 3.1])
train_Y = asarray([1.7, 2.76, 2.09, 3.19, 1.694, 1.573, 3.366, 2.596, 2.53, 1.221,
                   2.827, 3.465, 1.65, 2.904, 2.42, 2.94, 1.3])
n_samples = train_X.shape[0]

# tf Graph Input
X = placeholder("float")
Y = placeholder("float")

# Set model weights
W = Variable(random.randn(), name="weight")
b = Variable(random.randn(), name="bias")

# Construct a linear model
pred = add(multiply(X, W), b)

# Mean squared error
cost = reduce_sum(pow(pred - Y, 2)) / (2 * n_samples)
# Gradient descent
#  Note, minimize() knows to modify W and b because Variable objects are trainable=True by default
optimizer = train.GradientDescentOptimizer(learning_rate).minimize(cost)

# Initialize the variables (i.e. assign their default value)
init = global_variables_initializer()

# Start training
with Session() as sess:

    # Run the initializer
    sess.run(init)

    # Fit all training data
    for epoch in range(training_epochs):
        for (x, y) in zip(train_X, train_Y):
            sess.run(optimizer, feed_dict={X: x, Y: y})

        # Display logs per epoch step
        if (epoch + 1) % display_step == 0:
            c = sess.run(cost, feed_dict={X: train_X, Y: train_Y})
            print("Epoch:", '%04d' % (epoch + 1), "cost=", "{:.9f}".format(c),
                  "W=", sess.run(W), "b=", sess.run(b))

    print("Optimization Finished!")
    training_cost = sess.run(cost, feed_dict={X: train_X, Y: train_Y})
    print("Training cost=", training_cost, "W=",
          sess.run(W), "b=", sess.run(b), '\n')

    # Graphic display
    plot(train_X, train_Y, 'ro', label='Original data')
    plot(train_X, sess.run(W) * train_X + sess.run(b), label='Fitted line')
    legend()
    show()

    # Testing example, as requested (Issue #2)
    test_X = asarray([6.83, 4.668, 8.9, 7.91, 5.7, 8.7, 3.1, 2.1])
    test_Y = asarray([1.84, 2.273, 3.2, 2.831, 2.92, 3.24, 1.35, 1.03])

    print("Testing... (Mean square loss Comparison)")
    testing_cost = sess.run(
        reduce_sum(pow(pred - Y, 2)) / (2 * test_X.shape[0]),
        feed_dict={X: test_X, Y: test_Y})  # same function as cost above
    print("Testing cost=", testing_cost)
    print("Absolute mean square loss difference:", abs(
        training_cost - testing_cost))

    plot(test_X, test_Y, 'bo', label='Testing data')
    plot(train_X, sess.run(W) * train_X + sess.run(b), label='Fitted line')
    legend()
    show()
