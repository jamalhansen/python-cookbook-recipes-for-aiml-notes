from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

iris = load_iris()
data = iris.data
target = iris.target

data_train, data_test, target_train, target_test = train_test_split(data, target, test_size=0.2, random_state=42)

model = MLPClassifier(hidden_layer_sizes=(10,), max_iter=1000, random_state=42)
print("Ready to train model")

model.fit(data_train, target_train)
print("Model trained")

predictions = model.predict(data_test)
accuracy = accuracy_score(target_test, predictions)
print(f"Accuracy: {accuracy}")