from collections import Counter

def most_popular_product(sales_data):
    # Calculate the frequency distribution of products sold
    product_frequency = Counter(sales_data)

    # Find the most popular product
    most_popular_product, frequency = product_frequency.most_common(1)[0]

    # Print the result
    print(f"The most popular product is '{most_popular_product}' with {frequency} sales.")

# Example usage
if __name__ == "__main__":
    # Replace this with the actual sales data
    sales_data = ["ProductA", "ProductB", "ProductA", "ProductC", "ProductB", "ProductA", "ProductB", "ProductC"]

    most_popular_product(sales_data)
