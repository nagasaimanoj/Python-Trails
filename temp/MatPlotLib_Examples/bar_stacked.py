from matplotlib.pyplot import show, bar

menMeans = (20, 35, 30, 35, 27)
menStd = (2, 3, 4, 1, 2)

womenMeans = (25, 32, 34, 20, 25)
womenStd = (3, 5, 2, 3, 3)

ind = (1, 2, 3, 4, 5)
width = 0.35

bar(ind, menMeans, width, yerr=menStd)
bar(ind, womenMeans, width, yerr=womenStd, bottom=menMeans)

show()
