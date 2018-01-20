"""
Example: simple line plot.
Show how to make a plot that has equal aspect ratio
"""

from matplotlib.pyplot import axes, grid, plot, show
from numpy import arange, cos, pi

t = arange(0.0, 1.0 + 0.01, 0.01)
s = cos(2 * 2 * pi * t)
plot(t, s, '-', lw=2)

grid(True)

axes().set_aspect('equal', 'datalim')

show()
