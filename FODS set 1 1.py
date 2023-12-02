# Import necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create a sample dataset
data = {
    'Age': [22, 25, 39, 45, 33],
    'Salary': [40000, 45000, 150000, 200000, 120000]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Calculate correlation matrix
correlation_matrix = df.corr()

# Calculate covariance matrix
covariance_matrix = df.cov()

# Plot the correlation matrix using seaborn
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
plt.title('Correlation Matrix')
plt.show()

# Plot the scatterplot for Age vs. Salary
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Age', y='Salary', data=df)
plt.title('Scatterplot - Age vs. Salary')
plt.xlabel('Age')
plt.ylabel('Salary')
plt.show()
