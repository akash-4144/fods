import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample housing dataset
data = {
    'Price': [300000, 350000, 400000, 280000, 320000],
    'SquareFeet': [2000, 2200, 2500, 1800, 2100],
    'Bedrooms': [3, 4, 4, 2, 3],
    'Bathrooms': [2, 2.5, 3, 1.5, 2],
}

housing_df = pd.DataFrame(data)

# Scatterplot
plt.figure(figsize=(10, 6))
sns.scatterplot(x='SquareFeet', y='Price', data=housing_df, hue='Bedrooms', size='Bathrooms', sizes=(50, 200))
plt.title('Scatterplot of Housing Data')
plt.xlabel('Square Feet')
plt.ylabel('Price')
plt.legend(title='Bedrooms')
plt.show()

# Stacked Bar Chart
plt.figure(figsize=(10, 6))
sns.barplot(x='Bedrooms', y='SquareFeet', data=housing_df, hue='Bathrooms')
plt.title('Stacked Bar Chart of Housing Data')
plt.xlabel('Bedrooms')
plt.ylabel('Square Feet')
plt.legend(title='Bathrooms')
plt.show()
