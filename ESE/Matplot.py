# Q20: Simple Line Chart Using Matplotlib

import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [10, 12, 15, 20, 25]

# Plot line chart
plt.plot(x, y, marker='o', label = 'Example Label')
plt.title("Simple Line Chart")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()

# simple example to plot the points (8, 10) and (1, 3):
import matplotlib.pyplot as plt

# Coordinates of the points
x = [8, 1]
y = [10, 3]

# Create the scatter plot
plt.scatter(x, y, color='red')

# Adding labels
plt.title('Scatter Plot of Points')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Show the plot
plt.show()