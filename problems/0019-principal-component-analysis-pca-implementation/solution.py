
import numpy as np

def pca(data: np.ndarray, k: int) -> np.ndarray:
    """
    Perform PCA and return the top k principal components.

    Returns:
        Array of shape (n_features, k), rounded to 4 decimals.
    """
    # 1. Standardize the data
    mean = np.mean(data, axis=0)
    std = np.std(data, axis=0)

    # Avoid division by zero for constant features
    std[std == 0] = 1

    data = (data - mean) / std

    m, n = data.shape

    # 2. Compute covariance matrix
    cov = (data.T @ data) / (m - 1)

    # 3. Eigendecomposition
    eigenvalues, eigenvectors = np.linalg.eigh(cov)

    # 4. Sort eigenvalues in descending order
    idx = np.argsort(eigenvalues)[::-1]

    eigenvectors = eigenvectors[:, idx]

    # 5. Select the top k principal components
    components = eigenvectors[:, :k]

    # 6. Apply the sign convention
    for j in range(k):
        for i in range(n):
            if abs(components[i, j]) > 1e-10:
                if components[i, j] < 0:
                    components[:, j] *= -1
                break

    # 7. Round to 4 decimal places
    return np.round(components, 4)



    pass
