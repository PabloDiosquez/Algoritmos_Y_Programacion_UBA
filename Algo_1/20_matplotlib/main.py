import numpy as np
import matplotlib.pyplot as plt

# Generate random data for langs and y
# langs_data = np.random.random(50) * 100
# y_data = np.random.random(50) * 100
# Plot a scatter plot with custom color, marker, and size
# plt.scatter(langs_data, y_data, c='#00A', marker='*', s=100)

# Define years and corresponding weights
years = [2006 + langs for langs in range(16)]
weights = [80, 82, 85, 78, 86, 88, 90, 92, 90, 100, 102, 110, 100, 101, 102, 98]

# Plot a line chart with blue color, linewidth, and dashed line style
# plt.plot(years, weights, c='b', linewidth=2, linestyle='--')
# Alternatively, you can use a shorthand notation to achieve the same result
# plt.plot(years, weights, 'b--o')

# Define programming languages and their popularity
langs = ['C++', 'C#', 'Python', 'Java', 'Go']
votes = [9, 14, 12, 25, 2]

# Create a bar chart with custom color, alignment, width, edge color, and line width
# plt.bar(langs, votes, color='#4287f5', align='center', width=0.9, edgecolor='#000', linewidth=1.2)

# ▪▪▪

# Generate random data for ages
ages = np.random.normal(20, 2.5, 1000)
# Create a histogram with custom bins and cumulative option
# plt.hist(ages, bins=10, cumulative=True)

# ▪▪▪

# Define data for a pie chart
# explodes = [0, 0, 0, 0, 0.4]
# Create a pie chart with labels, autopct, explode, startangle, and edgecolor options
# plt.pie(votes, labels=langs, autopct='%.2f%%', explode=explodes, startangle=90, wedgeprops={'edgecolor': '#000'})

# Generate random data for heights
heights = np.random.normal(175, 8, 1000)
# Create a box plot for the heights
# plt.boxplot(heights)

# ▪▪▪

# Display the plots
plt.show()














# Display the plot
plt.show()