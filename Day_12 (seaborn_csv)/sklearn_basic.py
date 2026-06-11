from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
import numpy as np

#Step 1: Create sample dataset
X = np.array([[1], [2], [3], [4], [5],[6],[7],[8],[9],[10]])
y = np.array([2, 4, 5, 4, 5, 7, 8, 9, 10, 12])

#Step 2: Split into train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,random_state=42)

#Step 3: Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

#Step 4: Train model
model = LinearRegression()
model.fit(X_train_scaled,y_train)

#Step 5: Predict
y_pred=model.predict(X_test_scaled)
print("Actual: ", y_test)
print("Predicted: ", y_pred)