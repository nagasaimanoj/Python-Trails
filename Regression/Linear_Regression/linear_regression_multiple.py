import matplotlib.pyplot as plt
from sklearn import linear_model
import numpy as np

x = np.arange(0, 30)
y = np.arange(10)

x.shape = (10, 3)

reg = linear_model.LinearRegression()
reg.fit(x, y)
plt.plot(range(len(y)), reg.predict(x), marker="o")

x = x.T
y = np.arange(3)
reg_2 = linear_model.LinearRegression()
reg_2.fit(x, y)
plt.plot(range(len(y)), reg_2.predict(x), marker="o")

plt.show()