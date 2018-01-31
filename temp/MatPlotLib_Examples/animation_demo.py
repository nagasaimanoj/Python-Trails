from matplotlib.pyplot import clim, gcf, imshow, pause, title
from numpy import arange, newaxis

x = arange(6)
y = arange(5)
z = x * y[:, newaxis]

for i in range(10):
    if i == 0:
        p = imshow(z)
        fig = gcf()
        clim()   # clamp the color limits
        title("Boring slide show")
    else:
        z = z + 2
        p.set_data(z)

    print("step", i)
    pause(0.5)
