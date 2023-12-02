import scipy.stats as stats

# Sample data (replace these with your actual data)
conversion_rates_A = [0.12, 0.15, 0.18, 0.14, 0.17]  # Replace with actual data for design A
conversion_rates_B = [0.10, 0.13, 0.16, 0.11, 0.14]  # Replace with actual data for design B

# Perform t-test
t_statistic, p_value = stats.ttest_ind(conversion_rates_A, conversion_rates_B)

# Choose significance level
alpha = 0.05

# Compare p-value to alpha
if p_value < alpha:
    print(f"Reject the null hypothesis. There is a statistically significant difference.")
else:
    print("Fail to reject the null hypothesis. There is no statistically significant difference.")

# Print t-statistic and p-value for reference
print(f"T-statistic: {t_statistic}")
print(f"P-value: {p_value}")
