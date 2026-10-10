import numpy as np

def linear_regression_gradient_descent(X: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> np.ndarray:
    """
    Perform linear regression using gradient descent.

    Args:
        X: Feature matrix of shape (m, n) where first column is all ones (for intercept)
        y: Target vector of shape (m,)
        alpha: Learning rate
        iterations: Number of gradient descent iterations
    
    Returns:
        Learned weights as a 1D array of shape (n,)
    """
    m, n = X.shape
    y = y.reshape(-1, 1)  # Ensure y is a column vector
    theta = np.zeros((n, 1))  # Initialize weights to zeros

    X=np.asarray(X)
    y=np.asarray(y)

    def forward(X,y,theta):
        p= np.matmul(X, theta)

        return p
    
    def backward(p,y,X):
        dw= (1.0/(m))*(np.matmul(X.T,(p-y)))
        return dw
    
    for _ in range(iterations):
        p=forward(X,y,theta)
        dw= backward(p,y,X)

        theta= theta - alpha*(dw)
    return theta.flatten()


    # Your code here: implement gradient descent

    return theta.flatten()