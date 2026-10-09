
from sklearn.linear_model import LinearRegression

# Training data
X = [[500], [1000], [1500]]
y = [10, 20, 30]

# Create and train model
model = LinearRegression()
model.fit(X, y)

# Get house size
size = int(input("Enter house size in sq.ft: "))

# Predict house price
prediction = model.predict([[size]])

print("Predicted price:", round(prediction[0], 2), "lakh")
