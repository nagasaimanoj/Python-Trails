import matplotlib.pyplot as plt
plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

plt.rcdefaults()
fig, ax = plt.subplots()

y_data = np.arange(5)
x_data = 3 + 10 * np.random.rand(len(y_data))

ax.barh(y_data, x_data)
plt.show()
