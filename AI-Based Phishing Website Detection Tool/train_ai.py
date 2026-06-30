import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

# 1. Load the real dataset from your folder
# The file name must match your CSV file exactly
try:
    df = pd.read_csv('Phishing_Legitimate_full.csv')
    print("Dataset loaded successfully!")
except FileNotFoundError:
    print("Error: Could not find Phishing_Legitimate_full.csv. Make sure it is in the same folder.")

# 2. Data Preparation
# 'id' is not needed for training. 'CLASS_LABEL' is the target (1=phishing, 0=safe).
X = df.drop(['id', 'CLASS_LABEL'], axis=1, errors='ignore') 
y = df['CLASS_LABEL']

# 3. Split data: 80% for training, 20% for testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Initialize and Train Random Forest Classifier
# Using 100 trees for high precision
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 5. Check Performance
predictions = model.predict(X_test)
score = accuracy_score(y_test, predictions)
print(f"Model trained with {score * 100:.2f}% Accuracy!")

# 6. Save the trained model to a file
joblib.dump(model, 'phishing_model_professional.pkl')
print("Professional model saved as 'phishing_model_professional.pkl'")