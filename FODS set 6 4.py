import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn import datasets
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression

def load_dataset():
    # For demonstration purposes, I'll load the Iris dataset. Replace this with your own dataset loading logic.
    iris = datasets.load_iris()
    X = iris.data
    y = iris.target

    # Convert labels to binary for binary classification (you can customize this based on your dataset)
    label_encoder = LabelEncoder()
    y = label_encoder.fit_transform(y)

    return X, y

def train_model(X_train, y_train):
    # Increase the number of iterations
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    # Make predictions on the test set
    y_pred = model.predict(X_test)

    # Calculate evaluation metrics
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    return accuracy, precision, recall, f1

def main():
    # Load dataset
    X, y = load_dataset()

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    model = train_model(X_train, y_train)

    # Get user input for feature names and target variable
    feature_names = input("Enter feature names (comma-separated): ").split(',')
    target_variable = input("Enter target variable index: ")

    # Convert feature names to column indices
    feature_indices = [i for i, name in enumerate(feature_names)]

    # Extract selected features and target variable
    X_test_selected = X_test[:, feature_indices]

    try:
        # Convert target variable to integer
        target_variable_index = int(target_variable)
        y_test_selected = y_test if 0 <= target_variable_index < y_test.shape[1] else None
    except ValueError:
        y_test_selected = None

    if y_test_selected is None:
        print("Invalid target variable index.")
        return

    # Evaluate the model
    accuracy, precision, recall, f1 = evaluate_model(model, X_test_selected, y_test_selected)

    # Display evaluation metrics
    print(f"Accuracy: {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall: {recall:.4f}")
    print(f"F1 Score: {f1:.4f}")

if __name__ == "__main__":
    main()
