import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import random

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
# style.use('ggplot')
# plt.pie(votes, labels=None)

# Add a legend to the pie chart to associate labels with people's names.
# plt.legend(people, loc='upper left')

# ▪▪▪

## Generate random data for x1 and y1
x1, y1 = np.random.random(100), np.random.random(100)

# Create a figure and scatter plot for x1 and y1
# plt.figure(1)
# plt.scatter(x1, y1)

# Generate a sequence of numbers for x2 and random data for y2
# x2, y2 = np.arange(100), np.random.random(100)

# Create a new figure and line plot for x2 and y2
# plt.figure(2)
# plt.plot(x2, y2)

# ▪▪▪

# Create an array of numbers from 0 to 99 for x
x = np.arange(100)

# Create a 2x2 grid of subplots within a single figure
# fig, axes = plt.subplots(2, 2)

# # Set the title for the entire figure
# fig.suptitle('Four Plots')

# # Plot the sine wave in the top-left subplot
# axes[0, 0].plot(x, np.sin(x))
# axes[0, 0].set_title('Sine Wave')

# # Plot a random function in the top-right subplot
# axes[0, 1].plot(x, np.random.random(100))
# axes[0, 1].set_title('Random Function')

# # Plot the cosine wave in the bottom-left subplot
# axes[1, 0].plot(x, np.cos(x))
# axes[1, 0].set_title('Cosine Wave')

# # Plot the logarithmic function in the bottom-right subplot
# axes[1, 1].plot(x, np.log(x))
# axes[1, 1].set_title('Log Function')

# ▪▪▪
# Create a 3D plot with a set of random data points
# ax = plt.axes(projection='3d')
# x = np.random.random(100)
# y = np.random.random(100)
# z = np.random.random(100)
# ax.scatter(x, y, z)
# ax.set_title('3D Plot')
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')

# Create a 3D line plot with cosine and sine functions
# x = np.arange(0, 100, 0.1)
# y = np.cos(x)
# z = np.sin(x)
# ax.plot(x, y, z)

# Create a 3D surface plot with a sine function in the X-Y plane
# x = np.arange(-10, 10, 0.1)
# y = np.arange(-10, 10, 0.1)
# X, Y = np.meshgrid(x, y)
# Z = np.sin(X) + np.sin(Y)
# ax.plot_surface(X, Y, Z, cmap='Spectral')

# ▪▪▪

# Initialize a list to count the number of 'Heads' and 'Tails'
heads_tails = [0, 0]

# Loop to simulate coin flips and update the count
# for _ in range(100000):
#     heads_tails[random.randint(0, 1)] += 1
#     # Create a bar chart to show the count of 'Heads' and 'Tails'
#     plt.bar(['Heads', 'Tails'], heads_tails, color=['r', 'b'])
#     plt.pause(0.001)  # Pause to display the updated bar chart

# Display the plots
plt.show()