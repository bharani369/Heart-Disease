import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load dataset
df = pd.read_csv("heart_disease_with_troponin_angio.csv")

# 🔥 Convert categorical → numeric using get_dummies (BEST METHOD)
df = pd.get_dummies(df, drop_first=True)

# Split
X = df.drop("HeartDisease", axis=1)
y = df["HeartDisease"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

print("Accuracy:", model.score(X_test, y_test))

# Save model + columns
joblib.dump(model, "heart_model.pkl")
joblib.dump(X.columns.tolist(), "columns.pkl")

print("✅ Training completed")