import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, classification_report
import joblib

# -----------------------------
# 1. Load dataset
# -----------------------------
df = pd.read_csv("PHQ9_GAD7_df.csv", sep=";")

# Inspect dataset
print(df.head())

# -----------------------------
# 2. Features & Target
# -----------------------------
X = df.drop("CONDITION", axis=1)   # PHQ1..PHQ9 + GAD1..GAD7
y = df["CONDITION"]                # Labels: e.g. H (Healthy), D (Depressed)

# -----------------------------
# 3. Train/Test Split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# -----------------------------
# 4. Train Model
# -----------------------------
model = RandomForestClassifier(
    n_estimators=200, max_depth=12, random_state=42
)
model.fit(X_train, y_train)

# -----------------------------
# 5. Evaluate Model
# -----------------------------
y_pred = model.predict(X_test)

acc = accuracy_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred, average="weighted")

print(f"Accuracy: {acc:.2f}")
print(f"F1 Score: {f1:.2f}")
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# -----------------------------
# 6. Save Model
# -----------------------------
joblib.dump(model, "mental_health_model.pkl")
