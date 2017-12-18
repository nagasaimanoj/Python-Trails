
import numpy as np  # Note: there is a typo on this line in the video


def nonlin(x, deriv=False):  # Note: there is a typo on this line in the video
    if(deriv == True):
        return (x * (1 - x))

    # Note: there is a typo on this line in the video
    return 1 / (1 + np.exp(-x))


# input data
X = np.array([[0, 0, 1],  # Note: there is a typo on this line in the video
              [0, 1, 1],
              [1, 0, 1],
              [1, 1, 1]])


# output data
y = np.array([[0],
              [1],
              [1],
              [0]])

np.random.seed(1)


# synapses
# 3x4 matrix of weights ((2 inputs + 1 bias) x 4 nodes in the hidden layer)
syn0 = 2 * np.random.random((3, 4)) - 1
# 4x1 matrix of weights. (4 nodes x 1 output) - no bias term in the hidden layer.
syn1 = 2 * np.random.random((4, 1)) - 1


for j in range(60000):

    # Calculate forward through the network.
    l0 = X
    l1 = nonlin(np.dot(l0, syn0))
    l2 = nonlin(np.dot(l1, syn1))

    # Back propagation of errors using the chain rule.
    l2_error = y - l2
    # Only print the error every 10000 steps, to save time and limit the amount of output.
    if(j % 10000) == 0:
        print("Error: " + str(np.mean(np.abs(l2_error))))

    l2_delta = l2_error * nonlin(l2, deriv=True)

    l1_error = l2_delta.dot(syn1.T)

    l1_delta = l1_error * nonlin(l1, deriv=True)

    # update weights (no learning rate term)
    syn1 += l1.T.dot(l2_delta)
    syn0 += l0.T.dot(l1_delta)

print("Output after training")
print(l2)
