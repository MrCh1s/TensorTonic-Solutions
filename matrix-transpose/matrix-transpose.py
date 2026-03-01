import numpy as np 

def matrix_transpose(A):
    A = np.asarray(A)
    m, n = A.shape
    trans = np.zeros((n, m))
    for i in range(m):
        for j in range(n):
            trans[j, i] = A[i, j]

    return trans