import matplotlib.pyplot as plt

# Hypothetical dataset (replace this with your actual data)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales = [15000, 18000, 22000, 12000, 25000, 20000, 18000, 21000, 19000, 22000, 24000, 28000]

# Line plot
plt.figure(figsize=(10, 6))
plt.plot(months, sales, marker='o', linestyle='-', color='b', label='Monthly Sales')
plt.title('Monthly Sales Data')
plt.xlabel('Month')
plt.ylabel('Sales ($)')
plt.legend()
plt.grid(True)
plt.show()

# Bar chart
plt.figure(figsize=(10, 6))
plt.bar(months, sales, color='orange', label='Monthly Sales')
plt.title('Monthly Sales Data (Bar Chart)')
plt.xlabel('Month')
plt.ylabel('Sales ($)')
plt.legend()
plt.grid(axis='y')
plt.show()
