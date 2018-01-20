from matplotlib.patches import Ellipse
from matplotlib.pyplot import show, subplot, xlim, ylim
from numpy import arange

angles = arange(0, 360, 45)
ells = [Ellipse((1, 1), 4, 2, a) for a in angles]

a = subplot(111, aspect='equal')

for e in ells:
    e.set_clip_box(a.bbox)
    e.set_alpha(0.1)
    a.add_artist(e)

xlim(-2, 4)
ylim(-1, 3)

show()
