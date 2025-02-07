
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Load the dataset
data = pd.read_csv('/content/Housing.csv')

# Selecting only 'area', 'bedrooms', 'bathrooms', and 'price' columns
data = data[['area', 'bedrooms', 'bathrooms', 'price']]

# Initial exploration
print("Rows and Columns of the dataset:", data.shape)
print(data.info())
print(data.describe())

# Split into features (X) and label (y)
X = data.drop('price', axis=1)
y = data['price']

# Split into train and test sets
np.random.seed(0)
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, test_size=0.3, random_state=100)

# Scale numerical features
scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Fit linear regression model
linear_regression = LinearRegression()
linear_regression.fit(X_train_scaled, y_train)

# Evaluate model
train_score = linear_regression.score(X_train_scaled, y_train)
test_score = linear_regression.score(X_test_scaled, y_test)
print(f"Training R-squared: {train_score:.3f}")
print(f"Testing R-squared: {test_score:.3f}")

# Predictions
predictions = linear_regression.predict(X_test_scaled)
r2 = r2_score(y_test, predictions)
print(f"R-squared on test set: {r2:.3f}")

# Plot actual vs predicted
plt.figure(figsize=(8, 6))
plt.scatter(y_test, predictions)
plt.title('Actual vs Predicted Prices')
plt.xlabel('Actual Price')
plt.ylabel('Predicted Price')
plt.show()
