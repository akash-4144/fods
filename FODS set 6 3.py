def find_most_common_disease(disease_list):
    # Create a dictionary to store the frequency of each disease
    disease_frequency = {}

    # Populate the dictionary with disease frequencies
    for disease, count in disease_list:
        if disease in disease_frequency:
            disease_frequency[disease] += count
        else:
            disease_frequency[disease] = count

    # Find the most common disease
    most_common_disease = max(disease_frequency, key=disease_frequency.get)

    # Print the results
    print("Frequency Distribution of Diseases:")
    for disease, count in disease_frequency.items():
        print(f"{disease}: {count} patients")

    print("\nThe most common disease is:", most_common_disease, "with", disease_frequency[most_common_disease], "patients.")

# Example usage
if __name__ == "__main__":
    # Example list of diseases and patient counts
    disease_data = [("Flu", 30), ("Diabetes", 15), ("Flu", 20), ("Heart Disease", 10), ("Diabetes", 25)]

    # Call the function with the example data
    find_most_common_disease(disease_data)
