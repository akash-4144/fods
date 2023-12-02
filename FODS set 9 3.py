import numpy as np
import matplotlib.pyplot as plt
patients_smoke = [50, 60, 70, 80, 90]
patients_lung_cancer = [5, 8, 12, 15, 20]
correlation_coefficient = np.corrcoef(patients_smoke, patients_lung_cancer)[0, 1]
plt.scatter(patients_smoke, patients_lung_cancer, color='blue', label='Data Points')
plt.title('Correlation between Smoking and Lung Cancer')
plt.xlabel('Number of Patients who Smoke')
plt.ylabel('Number of Patients with Lung Cancer')
plt.legend()
plt.text(60, 15, f'Correlation Coefficient: {correlation_coefficient:.2f}', color='red')
plt.show()
