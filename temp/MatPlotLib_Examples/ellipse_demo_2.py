from matplotlib.collections import EllipseCollection
from matplotlib.pyplot import colorbar, show, subplots
from numpy import arange, hstack, meshgrid, newaxis

x = arange(10)
y = arange(15)
X, Y = meshgrid(x, y)

XY = hstack((X.ravel()[:, newaxis], Y.ravel()[:, newaxis]))

ww = X / 10.0
hh = Y / 15.0
aa = X * 9

fig, ax = subplots()

ec = EllipseCollection(ww, hh, aa, units='x', offsets=XY,
                       transOffset=ax.transData)
ec.set_array((X + Y).ravel())
ax.add_collection(ec)
ax.autoscale_view()
cbar = colorbar(ec)

show()
