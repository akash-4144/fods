from collections import Counter

def calculate_frequency_distribution(accidents):
    # Extracting the causes from the list of accidents
    causes = [accident['cause'] for accident in accidents]

    # Calculating the frequency distribution using Counter
    frequency_distribution = Counter(causes)

    return frequency_distribution

def most_common_cause(frequency_distribution):
    # Finding the most common cause
    common_cause, frequency = frequency_distribution.most_common(1)[0]

    return common_cause

# Example usage:
if __name__ == "__main__":
    # Sample list of accidents with causes
    accidents = [
        {'cause': 'Speeding'},
        {'cause': 'Distracted driving'},
        {'cause': 'Drunk driving'},
        {'cause': 'Speeding'},
        {'cause': 'Distracted driving'},
        # Add more accidents as needed
    ]

    # Calculate the frequency distribution
    distribution = calculate_frequency_distribution(accidents)

    # Find and print the most common cause
    common_cause = most_common_cause(distribution)
    print(f"The most common cause of accidents is: {common_cause}")
