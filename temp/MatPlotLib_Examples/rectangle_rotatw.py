from matplotlib.patches import Rectangle
from matplotlib.pyplot import figure, grid, show, xlim, ylim
from matplotlib.transforms import Affine2D

ax = figure().add_subplot(111)

r1 = Rectangle((0, 0), 20, 40, color="blue")
r2 = Rectangle((0, 0), 20, 40, color="red")

r2.set_transform(Affine2D().rotate_deg(-45) + ax.transData)

ax.add_patch(r1)
ax.add_patch(r2)

xlim(-20, 60)
ylim(-20, 60)

grid(True)
show()
