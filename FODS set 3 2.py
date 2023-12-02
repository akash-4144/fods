import seaborn as sns
import matplotlib.pyplot as plt

# Load the built-in mpg dataset from seaborn
mpg = sns.load_dataset('mpg')

# Display the first few rows of the dataset to understand its structure
print(mpg.head())

# Multivariate Scatterplot
sns.scatterplot(x='horsepower', y='mpg', hue='origin', data=mpg)
plt.title('Multivariate Scatterplot')
plt.show()

# Scatter Plot Matrix
sns.pairplot(mpg, hue='origin')
plt.suptitle('Scatter Plot Matrix', y=1.02)
plt.show()
