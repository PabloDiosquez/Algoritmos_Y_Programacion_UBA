import numpy as np
import matplotlib.pyplot as plt

# Generate random data for x and y
# x_data = np.random.random(50) * 100
# y_data = np.random.random(50) * 100
# Plot a scatter plot with custom color, marker, and size
# plt.scatter(x_data, y_data, c='#00A', marker='*', s=100)

# Define years and corresponding weights
years = [2006 + x for x in range(16)]
weights = [80, 82, 85, 78, 86, 88, 90, 92, 90, 100, 102, 110, 100, 101, 102, 98]

# Plot a line chart with blue color, linewidth, and dashed line style
# plt.plot(years, weights, c='b', linewidth=2, linestyle='--')
# Alternatively, you can use a shorthand notation to achieve the same result
# plt.plot(years, weights, 'b--o')

# Define programming languages and their popularity
x = ['C++', 'C#', 'Python', 'Java', 'Go']
y = [9, 14, 12, 25, 15]

# Create a bar chart with custom color, alignment, width, edge color, and line width
# plt.bar(x, y, color='#4287f5', align='center', width=0.9, edgecolor='#000', linewidth=1.2)

# Display the plot
plt.show()