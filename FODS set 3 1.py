import numpy as np
import pandas as pd

# Sample data
data = {
    'age': [22, 25, 39, 45, 33],
    'salary': [40000, 45000, 150000, 200000, 120000]
}

# Creating a pandas DataFrame
df = pd.DataFrame(data)

# Calculate covariance matrix
covariance_matrix = np.cov(df['age'], df['salary'], ddof=0)

# Extract the covariance value
covariance_value = covariance_matrix[0, 1]

# Calculate correlation matrix
correlation_matrix = np.corrcoef(df['age'], df['salary'])

# Extract the correlation value
correlation_value = correlation_matrix[0, 1]

print(f'Covariance: {covariance_value}')
print(f'Correlation: {correlation_value}')
