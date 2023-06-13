import numpy as np
from sklearn.linear_model import LogisticRegression

# Generate random data
X = np.random.randint(0, 100, (1000, 2))
y = np.random.randint(0, 2, 1000)

# Split the data into training and test sets
X_train = X[:750]
y_train = y[:750]
X_test = X[750:]
y_test = y[750:]

# Create the classifier
clf = LogisticRegression()

# Train the classifier
clf.fit(X_train, y_train)

# Predict the labels of the test set
y_pred = clf.predict(X_test)

# Evaluate the accuracy of the classifier
accuracy = np.mean(y_pred == y_test)
print("Accuracy:", accuracy)
