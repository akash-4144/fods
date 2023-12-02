import pandas as pd
import numpy as np
from scipy import stats
np.random.seed(42)
ratings_data = {'rating': np.random.randint(1, 6, size=100)}
df = pd.DataFrame(ratings_data)
print(df.head())
average_rating = df['rating'].mean()
std_deviation = df['rating'].std()
standard_error = std_deviation / np.sqrt(len(df))
confidence_level = 0.95
margin_of_error = stats.norm.ppf((1 + confidence_level) / 2) * standard_error
confidence_interval = (average_rating - margin_of_error, average_rating + margin_of_error)
print(f"Average Rating: {average_rating:.2f}")
print(f"Standard Deviation: {std_deviation:.2f}")
print(f"Confidence Interval ({confidence_level * 100}%): {confidence_interval}")
