import pandas as pd
from scipy.stats import pearsonr, spearmanr
df = {
    'age': [22, 25, 39, 45, 33],
    'salary': [40000, 45000, 150000, 200000, 120000]
}
# Assuming df is your DataFrame with columns "age" and "salary"
# Replace df['age'] and df['salary'] with the actual column names in your dataset

# Pearson Correlation Coefficient
pearson_corr, _ = pearsonr(df['age'], df['salary'])
print(f"Pearson Correlation Coefficient: {pearson_corr}")

# Spearman's Rank Correlation Coefficient
spearman_corr, _ = spearmanr(df['age'], df['salary'])
print(f"Spearman's Rank Correlation Coefficient: {spearman_corr}")
