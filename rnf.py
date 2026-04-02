import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib  # To save the trained model

# Load dataset (assuming 'heart.csv' is the dataset)
data = pd.read_csv('Heart/Heartnew.csv')

# Replace or remove NaN values
data = data.replace([np.inf, -np.inf], np.nan)  # Replace inf and -inf with NaN
data.fillna(data.mean(), inplace=True)  # Replace NaN with the mean of each column

# Alternatively, you can remove rows with NaN or infinite values:
# data = data.dropna()  # Drop rows with NaN values

# Check for NaN or infinite values (optional)
print("Check for NaN or infinite values in the dataset:")
print(data.isna().sum())  # Show the number of missing values per column

# Features (X) and target (y)
X = data.drop(columns=['active'])  # Drop the target column
y = data['active']  # Target variable

# Split the dataset into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the Random Forest model
rf_model = RandomForestClassifier(n_estimators=300, random_state=42)
rf_model.fit(X_train, y_train)
joblib.dump(rf_model, 'heart_disease_model.pkl')

# Predict on the test data
y_pred = rf_model.predict(X_test)

# Evaluate the model
print("Accuracy Score: ", accuracy_score(y_test, y_pred))
print("Classification Report: \n", classification_report(y_test, y_pred))
