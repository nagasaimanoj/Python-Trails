from matplotlib.pyplot import plot, show
from numpy import mean, std

height = [58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71,
          72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86]
weight = [115, 117, 120, 123, 126, 129, 132, 135, 139, 142, 146, 150, 154, 159,
          164, 164, 168, 171, 175, 178, 182, 185, 188, 192, 195, 199, 202, 206, 209]

height_mean = mean(height)
height_std = std(height)
height_upper_bound = height_mean + height_std
height_lower_bound = height_mean - height_std

weight_mean = mean(weight)
weight_std = std(weight)
weight_upper_bound = weight_mean + weight_std
weight_lower_bound = weight_mean - weight_std

for i in range(len(height)):
    if((height_lower_bound < height[i] < height_upper_bound)or(weight_lower_bound < weight[i] < weight_upper_bound)):
        plot(height[i], weight[i], 'bo')
    else:
        plot(height[i], weight[i], 'rx')

show()
