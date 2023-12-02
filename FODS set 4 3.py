import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_squared_error, accuracy_score
from sklearn.preprocessing import StandardScaler

# Generate synthetic data for linear regression
np.random.seed(42)
X_linear = 2 * np.random.rand(100, 1)
y_linear = 4 + 3 * X_linear + np.random.randn(100, 1)

# Generate synthetic data for logistic regression (binary classification)
X_logistic = 2 * np.random.rand(100, 1)
y_logistic = (X_logistic > 1).astype(int).flatten()

# Split the data for both tasks
X_train_linear, X_test_linear, y_train_linear, y_test_linear = train_test_split(X_linear, y_linear, test_size=0.2, random_state=42)
X_train_logistic, X_test_logistic, y_train_logistic, y_test_logistic = train_test_split(X_logistic, y_logistic, test_size=0.2, random_state=42)

# Linear Regression
linear_model = LinearRegression()
linear_model.fit(X_train_linear, y_train_linear)
linear_predictions = linear_model.predict(X_test_linear)

# Logistic Regression
logistic_model = LogisticRegression()
logistic_model.fit(X_train_logistic, y_train_logistic)
logistic_predictions = logistic_model.predict(X_test_logistic)

# Visualize Linear Regression
plt.scatter(X_test_linear, y_test_linear, color='black')
plt.plot(X_test_linear, linear_predictions, color='blue', linewidth=3)
plt.title('Linear Regression')
plt.xlabel('X')
plt.ylabel('y')
plt.show()

# Visualize Logistic Regression (for binary classification)
plt.scatter(X_test_logistic, y_test_logistic, color='black')
plt.scatter(X_test_logistic, logistic_predictions, color='red', marker='x', linewidth=3)
plt.title('Logistic Regression')
plt.xlabel('X')
plt.ylabel('y (binary)')
plt.show()

# Evaluate models
linear_mse = mean_squared_error(y_test_linear, linear_predictions)
logistic_accuracy = accuracy_score(y_test_logistic, logistic_predictions)

print(f'Linear Regression Mean Squared Error: {linear_mse}')
print(f'Logistic Regression Accuracy: {logistic_accuracy}')
