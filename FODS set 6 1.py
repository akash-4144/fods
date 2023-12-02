import pandas as pd

# Sample data
exam_data = [{'name': 'Anastasia', 'score': 12.5}, {'name': 'Dima', 'score': 9}, {'name': 'Katherine', 'score': 16.5}]

# Create a DataFrame
df = pd.DataFrame(exam_data)

# Iterate over rows using iterrows()
for index, row in df.iterrows():
    print(f"Index: {index}, Name: {row['name']}, Score: {row['score']}")
