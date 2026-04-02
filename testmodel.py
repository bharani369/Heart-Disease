import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import joblib
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=FutureWarning)
# Load data
data = pd.read_csv("heart_disease_with_troponin_angio.csv")  # Updated filename
print(data)
# Visualize target distribution
sns.countplot(data['HeartDisease'], label="Count")
plt.show()
# Label encode categorical columns
categorical_cols = ['Sex', 'ChestPainType','RestingECG','ExerciseAngina','ST_Slope','HeartMRI','CTScan','Echocardiogram','ChestXray','Smoking']
le = LabelEncoder()
for col in categorical_cols:
    data[col] = le.fit_transform(data[col])

# Features and target
X = data.drop("HeartDisease", axis=1)
y = data["HeartDisease"]

# Clean NaNs and infinite values
X.replace([np.inf, -np.inf], np.nan, inplace=True)
X.dropna(inplace=True)
y = y[X.index]  # Align target with features

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
print(f"Model Accuracy: {accuracy_score(y_test, y_pred):.2f}")
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Save model
joblib.dump(model, "heart_model.pkl")
