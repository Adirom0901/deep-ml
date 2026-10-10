def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here
    j_len= len(a[0])
    i_len=len(a)
    b=[[0]*i_len for _ in range(j_len)]

    for i in range(len(a)):
        for j in range(len(b)):
            b[j][i]=a[i][j]
    return b
    pass