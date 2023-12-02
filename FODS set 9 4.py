import numpy as np
def calculate_mean_temperature(data):
    return np.mean(data, axis=0)
def calculate_std_dev(data):
    return np.std(data, axis=0)
def calculate_temperature_range(data):
    return np.max(data, axis=0) - np.min(data, axis=0)
def find_most_consistent_city(std_dev_values):
    return np.argmin(std_dev_values)
def main():
    dataset = np.array([
        [25, 28, 24, 30, 27, 22, 26, 28, 23, 29],
        [32, 30, 34, 36, 33, 31, 35, 32, 30, 37],
        [20, 25, 22, 24, 23, 21, 26, 24, 22, 27]
    ])
    mean_temperatures = calculate_mean_temperature(dataset)
    std_dev_values = calculate_std_dev(dataset)
    temperature_ranges = calculate_temperature_range(dataset)
    most_consistent_city = find_most_consistent_city(std_dev_values)
    city_with_highest_range = np.argmax(temperature_ranges)
    print("Mean temperatures for each city:", mean_temperatures)
    print("Standard deviation for each city:", std_dev_values)
    print("Temperature ranges for each city:", temperature_ranges)
    print("City with the most consistent temperature:", most_consistent_city)
    print("City with the highest temperature range:", city_with_highest_range)
if __name__ == "__main__":
    main()
