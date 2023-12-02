import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
sales_data = [100, 150, 200, 250, 300]
advertising_data = [50, 75, 100, 125, 150]
df = pd.DataFrame({'Sales': sales_data, 'Advertising': advertising_data})
correlation_coefficient = df['Sales'].corr(df['Advertising'])
print(f'Correlation Coefficient: {correlation_coefficient}')
plt.scatter(df['Advertising'], df['Sales'])
plt.title('Sales vs Advertising Spend')
plt.xlabel('Advertising Spend')
plt.ylabel('Number of Sales')
plt.show()
