import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import numpy as np
np.random.seed(42)
num_samples = 1000
data = pd.DataFrame({
    'engine_size': np.random.uniform(1.0, 5.0, num_samples),
    'horsepower': np.random.uniform(50, 300, num_samples),
    'fuel_efficiency': np.random.uniform(10, 40, num_samples),
    'price': 20000 + 5000 * np.random.randn(num_samples)
})
selected_features = ['engine_size', 'horsepower', 'fuel_efficiency']
target_variable = 'price'
X = data[selected_features]
y = data[target_variable]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f'Mean Squared Error: {mse}')
print(f'R-squared (R2) Score: {r2}')
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Actual Prices vs Predicted Prices")
plt.show()
coefficients = pd.DataFrame({'Feature': selected_features, 'Coefficient': model.coef_})
print(coefficients)
