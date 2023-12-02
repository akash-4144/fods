import random
import statistics

def mean_estimation(data):
    return sum(data) / len(data)

def variance_estimation(data, sample=True):
    n = len(data)
    correction_factor = 1 if sample else 0
    mean = mean_estimation(data)
    return sum((x - mean) ** 2 for x in data) / (n - correction_factor)

def simple_random_sampling(data, sample_size):
    return random.sample(data, sample_size)

# Example dataset
data = [12, 15, 18, 22, 25, 30, 35, 40, 45, 50]

# Mean estimation
mean = mean_estimation(data)
print(f"Mean: {mean}")

# Variance estimation
variance = variance_estimation(data)
print(f"Variance: {variance}")

# Simple random sampling
sample_size = 3
sample = simple_random_sampling(data, sample_size)
print(f"Random Sample of size {sample_size}: {sample}")
