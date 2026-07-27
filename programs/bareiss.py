import numpy as np

def bareiss_det(M):
    """Exact integer determinant via fraction-free Gaussian elimination (Bareiss algorithm).
    M: list of list of python ints (square). Returns exact integer determinant.
    """
    n = len(M)
    if n == 0:
        return 1
    A = [row[:] for row in M]
    prev = 1
    sign = 1
    for k in range(n-1):
        if A[k][k] == 0:
            # find pivot
            swap = None
            for i in range(k+1, n):
                if A[i][k] != 0:
                    swap = i; break
            if swap is None:
                return 0
            A[k], A[swap] = A[swap], A[k]
            sign = -sign
        for i in range(k+1, n):
            for j in range(k+1, n):
                A[i][j] = (A[i][j]*A[k][k] - A[i][k]*A[k][j]) // prev
        prev = A[k][k]
    return sign*A[n-1][n-1]
