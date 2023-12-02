from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
import numpy as np

def get_user_input():
    symptoms = []
    num_symptoms = int(input("Enter the number of symptoms: "))
    for i in range(num_symptoms):
        symptom_value = float(input(f"Enter value for symptom {i + 1}: "))
        symptoms.append(symptom_value)
    return np.array(symptoms).reshape(1, -1)

np.random.seed(42)
X = np.random.rand(100, 5)
y = np.random.randint(2, size=100)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

new_patient_features = get_user_input()
k_neighbors = int(input("Enter the value of k (number of neighbors): "))

knn_classifier = KNeighborsClassifier(n_neighbors=k_neighbors)
knn_classifier.fit(X_train_scaled, y_train)

prediction = knn_classifier.predict(scaler.transform(new_patient_features))

if prediction[0] == 0:
    print("The model predicts that the patient does not have the medical condition.")
else:
    print("The model predicts that the patient has the medical condition.")
