import numpy as np

# Assuming you have the sales data stored in a NumPy array named sales_data
# For example, let's say sales_data represents quarterly sales for the year
sales_data = np.array([100000, 120000, 90000, 150000])

# Calculate total sales for the year
total_sales = np.sum(sales_data)

# Determine the percentage increase from the first quarter to the fourth quarter
percentage_increase = ((sales_data[3] - sales_data[0]) / sales_data[0]) * 100

# Print the results
print(f"Total sales for the year: {total_sales}")
print(f"Percentage increase from Q1 to Q4: {percentage_increase:.2f}%")
