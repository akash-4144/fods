import numpy as np

# Sample fuel efficiency data (replace this with your actual data)
fuel_efficiency = np.array([25, 30, 22, 28, 26])

# Calculate average fuel efficiency
average_fuel_efficiency = np.mean(fuel_efficiency)

# Choose two car models for comparison (replace these indices with the actual indices of your models)
model1_index = 0
model2_index = 1

# Get fuel efficiency values for the selected models
fuel_efficiency_model1 = fuel_efficiency[model1_index]
fuel_efficiency_model2 = fuel_efficiency[model2_index]

# Calculate percentage improvement
percentage_improvement = ((fuel_efficiency_model2 - fuel_efficiency_model1) / fuel_efficiency_model1) * 100

# Display results with corrected syntax
print("Average Fuel Efficiency:", average_fuel_efficiency)
print("Percentage Improvement between Model:", percentage_improvement)
