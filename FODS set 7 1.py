import pandas as pd

# Sample data for Series 1
data1 = {'Name': 'John', 'Age': 25, 'City': 'New York'}
series1 = pd.Series(data1, name='Person1')

# Sample data for Series 2
data2 = {'Name': 'Alice', 'Age': 30, 'City': 'San Francisco'}
series2 = pd.Series(data2, name='Person2')

# Combine the two series into a DataFrame
df = pd.DataFrame([series1, series2])

# Display the DataFrame
print(df)
