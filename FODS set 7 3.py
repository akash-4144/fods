import numpy as np
import matplotlib.pyplot as plt

# Simulated data (replace this with your actual data)
temperature_data = [25, 28, 30, 22, 26, 29, 31, 24, 27, 23, 25, 28, 30, 22, 26, 29, 31, 24, 27, 23]
rainfall_data = [0.5, 0.2, 0.8, 0.1, 0.3, 0.6, 0.9, 0.4, 0.7, 0.2, 0.5, 0.8, 0.1, 0.3, 0.6, 0.9, 0.4, 0.7, 0.2, 0.5]

# Calculate the correlation coefficient
correlation_coefficient = np.corrcoef(temperature_data, rainfall_data)[0, 1]

# Print the correlation coefficient
print("Correlation Coefficient:", correlation_coefficient)

# Create a scatter plot
plt.scatter(temperature_data, rainfall_data, label=f'Correlation: {correlation_coefficient:.2f}')
plt.xlabel('Temperature (°C)')
plt.ylabel('Rainfall (mm)')
plt.title('Temperature vs Rainfall Scatter Plot')
plt.legend()
plt.grid(True)
plt.show()
