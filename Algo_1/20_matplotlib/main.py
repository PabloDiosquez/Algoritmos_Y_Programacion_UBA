import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

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
# Create a list of years from 2001 to 2010.
years = [2001 + x for x in range(10)]

# Define a list of income data for each year.
income = [55, 57, 67, 66, 45, 87, 78, 56, 68, 90]

# Define a list of income ticks to use for the y-axis.
income_ticks = [y for y in range(50, 96, 3)]

# ▪▪▪

# Generate random stock data for three companies (Company 1, Company 2, and Company 3).
stock_a = np.random.random(10) * 100
stock_b = np.random.random(10) * 100
stock_c = np.random.random(10) * 100

# Plot the stock data for each company and add labels.
# plt.plot(stock_a, label='Company 1')
# plt.plot(stock_b, label='Company 2')
# plt.plot(stock_c, label='Company 3')

# Create a legend to identify the companies on the plot.
# plt.legend(loc='lower right')

# ▪▪▪

# Define a list of people and the number of votes they received.
people = ['A', 'B', 'C', 'D', 'E']
votes = [10, 12, 5, 7, 9]

# Create a pie chart to visualize the distribution of votes.
plt.pie(votes, labels=None)

# Add a legend to the pie chart to associate labels with people's names.
plt.legend(people, loc='upper left')
# ▪▪▪


# Display the plots
plt.show()