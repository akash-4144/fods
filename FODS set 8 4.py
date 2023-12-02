import numpy as np
import matplotlib.pyplot as plt
smoking_data = [10, 15, 8, 5, 12]
lung_cancer_data = [2, 5, 1, 3, 4]
correlation_coefficient = np.corrcoef(smoking_data, lung_cancer_data)[0, 1]
print(f"Correlation Coefficient: {correlation_coefficient}")
plt.scatter(smoking_data, lung_cancer_data, color='blue', label='Data points')
plt.title('Correlation Between Smoking and Lung Cancer')
plt.xlabel('Number of Patients Who Smoke')
plt.ylabel('Number of Patients with Lung Cancer')
plt.legend()
plt.show()
