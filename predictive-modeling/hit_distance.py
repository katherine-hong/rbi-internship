# This file is for the hit distance modeling (new version)

# Loading the HittingGold CSV

import pandas as pd

# Load the data
df = pd.read_csv('HittingGold.csv', delimiter=';')

# Check the first few rows
print(df.head())

# Select features and target
features = [
    'EBV1', 'EBV2', 'EBV3', 'Velo', 'Elv', 'PitchAngle',
    'SmashFactor', 'SwingEfficiency', 'metric_power', 'metric_swing_speed'
] 
target = 'Dist'

# Handling missing values

# Drop rows with missing values in selected features or target
df_clean = df.dropna(subset=features + [target])

# Create input (X) and output (y)
X = df_clean[features]
y = df_clean[target]

# Split into training + testing sets

from sklearn.model_selection import train_test_split

# Using 80% for training and 20% for testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train linear regression model

from sklearn.linear_model import LinearRegression

# Initialize and train model
model = LinearRegression()
model.fit(X_train, y_train)


# Predicting + evaluating 
from sklearn.metrics import mean_squared_error, r2_score

# Predict distances
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\n")
print(f"Mean Squared Error: {mse:.2f}")
print(f"R^2 Score: {r2:.2f}")

# Analyzing feature importance (coefficients)
coefficients = pd.DataFrame({
    'Feature': X.columns,
    'Coefficient': model.coef_
}).sort_values(by='Coefficient', ascending=False)

print("\n")
print(coefficients)

# Visualize results

import matplotlib.pyplot as plt

plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, alpha=0.5)
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--')  # y = x line
plt.xlabel('Actual Hit Distance')
plt.ylabel('Predicted Hit Distance')
plt.title('Actual vs Predicted Hit Distance')
plt.grid(True)
plt.show()


# Result interpretation:
'''
R^2 of 0.80 means this model explains 80% of variance for hit distance (Dist), this is
considered strong.
'''

'''
Smashfactor:
Very strong positive effect on hit distance. One unit increase in SmashFactor adds ~143 
units of distance (huge).

EBV2:
Exit velocity #2 positively contributes — every 1 mph increase -> +5 units of distance.

metric_swing_speed:	
Faster swing speed adds distance.

EBV3:
Slight positive effect.

PitchAngle:
A steeper pitch might help with distance slightly.

EBV1:
Minimal impact — possibly redundant with EBV2/EBV3.

Elv:
Slight negative effect. Higher elevation might overshoot the ideal launch angle.

Velo:
Small negative effect, maybe this is bat velocity, which alone doesn't 
predict distance well.

SwingEfficiency:
Negative — might be correlation noise or misaligned with distance goals.

metric_power: 
Counterintuitive, possibly due to multicollinearity or outliers in the data.
'''






