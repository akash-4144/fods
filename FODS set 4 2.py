def most_common_weather(weather_data):
    # Calculate the total occurrences of all weather conditions
    total_occurrences = sum(weather_data.values())

    # Calculate the frequency distribution of each weather condition
    frequency_distribution = {weather: occurrences / total_occurrences for weather, occurrences in weather_data.items()}

    # Find the most common weather type
    most_common_weather_type = max(frequency_distribution, key=frequency_distribution.get)

    # Print the results
    print("Frequency Distribution:")
    for weather, frequency in frequency_distribution.items():
        print(f"{weather}: {frequency:.2%}")

    print("\nThe most common weather type is:", most_common_weather_type)

# Example data: Replace this with your actual weather data
weather_data = {
    "Sunny": 120,
    "Cloudy": 80,
    "Rainy": 50,
    "Snowy": 30,
    "Stormy": 10,
}

# Call the function with your weather data
most_common_weather(weather_data)
