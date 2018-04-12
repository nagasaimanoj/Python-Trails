from matplotlib.patches import Ellipse
from matplotlib.pyplot import figure, show

ells = Ellipse(angle=130, width=5, height=3, xy=[5.0, 2.0])

ax = figure(0).add_subplot(111)

ax.add_artist(ells)
ells.set_clip_box(ax.bbox)

ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

show()
