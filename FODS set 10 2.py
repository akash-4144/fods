import pandas as pd
import matplotlib.pyplot as plt
import random
def generate_synthetic_data(num_entries=100):
    shoe_sizes = [random.randint(5, 12) for _ in range(num_entries)]
    quantities = [random.randint(1, 50) for _ in range(num_entries)]
    df = pd.DataFrame({'shoe_size': shoe_sizes, 'quantity': quantities})
    return df
def calculate_frequency_distribution(df):
    frequency_distribution = df.groupby('shoe_size')['quantity'].sum().reset_index()
    print("Frequency Distribution Table:")
    print(frequency_distribution)
    plt.bar(frequency_distribution['shoe_size'], frequency_distribution['quantity'])
    plt.xlabel('Shoe Size')
    plt.ylabel('Quantity Sold')
    plt.title('Shoe Size Frequency Distribution')
    plt.show()
if __name__ == "__main__":
    synthetic_data = generate_synthetic_data()
    calculate_frequency_distribution(synthetic_data)
