# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

# Create a DataFrame with random data for demonstration
data = pd.DataFrame({
    'Feature1': [1.2, 2.1, 3.5, 4.0, 2.8, 1.9, 3.2, 4.5, 5.1, 2.0],
    'Feature2': [0.5, 1.0, 2.5, 3.0, 1.8, 1.0, 2.1, 3.8, 4.2, 1.5],
    'Feature3': [10, 15, 20, 25, 18, 12, 22, 30, 35, 15],
    'target_column': ['Good', 'Bad', 'Good', 'Bad', 'Good', 'Bad', 'Good', 'Bad', 'Good', 'Bad']
})

# Separate features and target variable
X = data.drop('target_column', axis=1)
y = data['target_column']

# Split the data into training and testing sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the features (important for KNN algorithm)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Create a KNN classifier
k_value = 5  # You can adjust the k value based on your dataset
knn_classifier = KNeighborsClassifier(n_neighbors=k_value)

# Train the model
knn_classifier.fit(X_train_scaled, y_train)

# Make predictions on the test set
y_pred = knn_classifier.predict(X_test_scaled)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, pos_label='Good')
recall = recall_score(y_test, y_pred, pos_label='Good')
f1 = f1_score(y_test, y_pred, pos_label='Good')

# Display the results
print(f"Accuracy: {accuracy:.2f}")
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
print(f"F1 Score: {f1:.2f}")

# Display confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)
print("\nConfusion Matrix:")
print(conf_matrix)
