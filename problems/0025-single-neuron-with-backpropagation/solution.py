
import numpy as np

def train_neuron(features: np.ndarray, labels: np.ndarray,
                 initial_weights: np.ndarray, initial_bias: float,
                 learning_rate: float, epochs: int) -> tuple[np.ndarray, float, list[float]]:

    def forward(features, bias, weights):
        z = features @ weights.T + bias
        probabilities = 1.0 / (1.0 + np.exp(-z))
        return probabilities

    def backward(features, labels, probabilities, m):
        error = probabilities - labels
        dw = (2.0 / m) * (error * probabilities * (1 - probabilities)).T @ features
        db = (2.0 / m) * np.sum(error * probabilities * (1 - probabilities))
        return dw, db

    mse_values = []
    m, n = features.shape

    for e in range(epochs):
        probabilities = forward(features, initial_bias, initial_weights)

        mse_values.append(np.mean((labels - probabilities) ** 2))

        dw, db = backward(features, labels, probabilities, m)

        initial_weights = initial_weights - learning_rate * dw
        initial_bias = initial_bias - learning_rate * db

    return initial_weights, initial_bias, mse_values
