import pandas as pd
import matplotlib.pyplot as plt

# Assuming you have a DataFrame named 'diabetes_data' with a 'glucose_level' column
# Replace this with the actual column names and dataset you have.

# Example Data (Replace this with your actual dataset)
data = {'glucose_level': [100, 120, 150, 180, 200, 130, 160, 140, 170, 190]}
diabetes_data = pd.DataFrame(data)

# Plotting using Bar Graph
plt.figure(figsize=(8, 6))
plt.bar(diabetes_data.index, diabetes_data['glucose_level'], color='blue')
plt.xlabel('Patient ID')
plt.ylabel('Glucose Level')
plt.title('Distribution of Glucose Levels in Diabetic Dataset (Bar Graph)')
plt.show()

# Plotting using Line Chart
plt.figure(figsize=(8, 6))
plt.plot(diabetes_data.index, diabetes_data['glucose_level'], marker='o', linestyle='-', color='green')
plt.xlabel('Patient ID')
plt.ylabel('Glucose Level')
plt.title('Distribution of Glucose Levels in Diabetic Dataset (Line Chart)')
plt.show()
