import pandas as pd
import numpy as np
np.random.seed(42)
n = 500

data = pd.DataFrame({
  'Pregnancies' : np.random.randint(0, 15, n),
  'Glucose' : np.random.randint(0, 15, n),
  'BloodPressure' : np.random.randint(50, 120, n),
  'SkinThickness' : np.random.randint(10, 60, n),
  'Insulin' : np.random.randint(0, 300, n),
  'BMI' : np.round(np.random.uniform(18, 45, n), 2),
  'DiabetesPedigreeFunction' : np.round(np.random.uniform(0.05, 2.50, n), 3),
  'Age' : np.random.randint(21, 80, n),
  'Outcome' : np.random.randint(0, 2, n),
  })

data.to_csv("diabetics.csv", index = False)
print("Diabetics Dataset Created Successfully! \n")
print("Dataset Shape: ",data.shape)
print("First 5 records: ")
print(data.head)