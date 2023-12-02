import matplotlib.pyplot as plt

# Sample data (replace this with your actual dataset)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
temperature_data = [25, 28, 30, 32, 35, 38, 40, 39, 37, 34, 30, 27]
rainfall_data = [50, 45, 60, 80, 100, 120, 110, 95, 80, 70, 55, 45]

# Scatter plot for rainfall data
plt.figure(figsize=(10, 5))
plt.scatter(months, rainfall_data, color='blue', label='Rainfall', marker='o')
plt.title('Monthly Rainfall Data')
plt.xlabel('Months')
plt.ylabel('Rainfall (mm)')
plt.legend()
plt.grid(True)
plt.show()

# Line plot for rainfall data
plt.figure(figsize=(10, 5))
plt.plot(months, rainfall_data, color='green', label='Rainfall', marker='o')
plt.title('Monthly Rainfall Data (Line Plot)')
plt.xlabel('Months')
plt.ylabel('Rainfall (mm)')
plt.legend()
plt.grid(True)
plt.show()
