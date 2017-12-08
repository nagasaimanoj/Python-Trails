import matplotlib.pyplot as plt
from sklearn import linear_model

x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
y = [1, 2, 3]

reg = linear_model.LinearRegression()
reg.fit(x, y)

plt.plot(range(len(y)), reg.predict(x), marker="o")

print(reg.predict([[10, 11, 12]]))
print(reg.predict([[13, 14, 15]]))

plt.show()
