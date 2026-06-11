import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

#Load CSV file
data = pd.read_csv("stock_data.csv")

#Display First 5 Records
print("\nFirst 5 Records")
print(data.head())

#Dataset Information
print("\nDataset Information")
data.info()

#Statistical Summary
print("\nStatistical Summary")
print(data.describe())

#Missing Values
print("\nMissing Values")
print(data.isnull().sum())

#Features and Target
X = data[["Open", "High", "Low", "Volume"]]
y = data["Close"]

#Feature Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

#Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
  X_scaled,
  y,
  test_size=0.20,
  random_state = 42
)
print("\nTraining Records: ",len(X_train))
print("Testing Records: ",len(X_test))

#Create Model
model = LinearRegression()

#Train Model
model.fit(X_train, y_train)
print("\nModel training Completed Successfully!")

#Prediction
y_pred = model.predict(X_test)

#Actual Vs Predicted
results = pd.DataFrame({
  "Actual Price": y_test.values,
  "Predicted Price": y_pred
})

print("/nActual VS Predicted Prices")
print(results.head(10))

#Visualisation
plt.figure(figsize=(10,5))
plt.plot(
  y_test.values[:50],
  marker="o",
  label="Actual Price"
)
plt.plot(
  y_pred[:50],
  marker="x",
  label = "Predicted Price"
)

plt.title('Stock Price Prediction using Linear Regression')
plt.xlabel('Test Records')
plt.ylabel('Closing Price')
plt.legend()
plt.grid(True)
plt.show()