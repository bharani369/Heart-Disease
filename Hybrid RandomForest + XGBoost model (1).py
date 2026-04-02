import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.metrics import accuracy_score, classification_report
from xgboost import XGBClassifier

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("dataset.csv")

# -----------------------------
# Encode Categorical Columns
# -----------------------------
for col in df.columns:
    if df[col].dtype == "object":
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])

# -----------------------------
# Features & Target
# -----------------------------
X = df.drop("target", axis=1)
y = df["target"]

# -----------------------------
# Train-Test Split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -----------------------------
# Models
# -----------------------------
rf = RandomForestClassifier(
    n_estimators=200,
    max_depth=10,
    random_state=42
)

xgb = XGBClassifier(
    n_estimators=200,
    learning_rate=0.05,
    max_depth=6,
    eval_metric="logloss"
)

# -----------------------------
# HYBRID MODEL (Voting)
# -----------------------------
hybrid_model = VotingClassifier(
    estimators=[
        ('rf', rf),
        ('xgb', xgb)
    ],
    voting='soft'   # 🔥 important
)

# -----------------------------
# Train
# -----------------------------
hybrid_model.fit(X_train, y_train)

# -----------------------------
# Predict
# -----------------------------
y_pred = hybrid_model.predict(X_test)

# -----------------------------
# Evaluation
# -----------------------------
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nReport:\n", classification_report(y_test, y_pred))

# -----------------------------
# Save Model
# -----------------------------
joblib.dump(hybrid_model, "hybrid_rf_xgb.pkl")

print("✅ Hybrid Model Saved!")