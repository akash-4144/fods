import numpy as np
import matplotlib.pyplot as plt
def calculate_correlation_coefficient(x, y):
    correlation_coefficient = np.corrcoef(x, y)[0, 1]
    return correlation_coefficient
def create_scatter_plot(x, y):
    plt.scatter(x, y, color='blue', alpha=0.5)
    plt.title('Crime Rate vs Poverty Rate')
    plt.xlabel('Poverty Rate')
    plt.ylabel('Crime Rate')
    plt.show()
def main():
    crime_rate = [100, 150, 200, 250, 300]
    poverty_rate = [10, 15, 20, 25, 30]
    correlation_coefficient = calculate_correlation_coefficient(poverty_rate, crime_rate)
    print(f'Correlation Coefficient: {correlation_coefficient}')
    create_scatter_plot(poverty_rate, crime_rate)
if __name__ == "__main__":
    main()
