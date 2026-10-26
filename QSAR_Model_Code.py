from google.colab import files
uploaded = files.upload()

--------------------------------------
#this program trains the model, calculates the R2, and on the basis of a new input calculates it's pIC50
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Load dataset
df = pd.read_csv("qsar_dataset.csv")

# Descriptors (independent variables)
X = df[["MW","LogP","TPSA","HBD","HBA","RotB"]]

# Target variable
y = df["pIC50"]

# Train QSAR model
model = LinearRegression()
model.fit(X,y)

# Print QSAR equation
print("Intercept:", model.intercept_)
print("Coefficients:", model.coef_)

# Model accuracy
print("R2 score:", model.score(X,y))

print("\n--- Predict IC50 for a new compound ---")

# User input descriptors
MW = float(input("Molecular Weight: "))
LogP = float(input("LogP: "))
TPSA = float(input("TPSA: "))
HBD = float(input("HBD: "))
HBA = float(input("HBA: "))
RotB = float(input("Rotatable Bonds: "))

# Create dataframe for prediction
new_data = pd.DataFrame([[MW,LogP,TPSA,HBD,HBA,RotB]],
columns=["MW","LogP","TPSA","HBD","HBA","RotB"])

# Predict pIC50
predicted_pIC50 = model.predict(new_data)[0]

# Convert pIC50 → IC50
IC50 = 10**(-predicted_pIC50)

print("\nPredicted pIC50:", predicted_pIC50)
print("Predicted IC50 (M):", IC50)
