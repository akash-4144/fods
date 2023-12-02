def most_popular_subject(subjects):
    # Create a dictionary to store the frequency of each subject
    subject_frequency = {}

    # Calculate the frequency distribution
    for subject, count in subjects.items():
        subject_frequency[subject] = subject_frequency.get(subject, 0) + count

    # Find the most popular subject
    most_popular_subject = max(subject_frequency, key=subject_frequency.get)

    return most_popular_subject

# Example usage:
subjects_taken = {
    "Math": 50,
    "Science": 40,
    "History": 30,
    "English": 45,
    "Art": 20,
}

popular_subject = most_popular_subject(subjects_taken)
print(f"The most popular subject is: {popular_subject}")
