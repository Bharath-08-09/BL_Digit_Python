import numpy as np

def strassen_matrix_multiply(A, B):
    n = len(A)
    
    # Base case: 1x1 matrix
    if n == 1:
        return [[A[0][0] * B[0][0]]]

    # Split matrices into quadrants
    mid = n // 2
    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]

    B11 = [row[:mid] for row in B[:mid]]
    B12 = [row[mid:] for row in B[:mid]]
    B21 = [row[:mid] for row in B[mid:]]
    B22 = [row[mid:] for row in B[mid:]]

    # Compute the 7 products (recursive calls)
    M1 = strassen_matrix_multiply(add(A11, A22), add(B11, B22))
    M2 = strassen_matrix_multiply(add(A21, A22), B11)
    M3 = strassen_matrix_multiply(A11, subtract(B12, B22))
    M4 = strassen_matrix_multiply(A22, subtract(B21, B11))
    M5 = strassen_matrix_multiply(add(A11, A12), B22)
    M6 = strassen_matrix_multiply(subtract(A21, A11), add(B11, B12))
    M7 = strassen_matrix_multiply(subtract(A12, A22), add(B21, B22))

    # Combine intermediate matrices into result
    C11 = add(subtract(add(M1, M4), M5), M7)
    C12 = add(M3, M5)
    C21 = add(M2, M4)
    C22 = add(subtract(add(M1, M3), M2), M6)

    # Combine quadrants into a single matrix
    new_matrix = []
    for i in range(mid):
        new_matrix.append(C11[i] + C12[i])
    for i in range(mid):
        new_matrix.append(C21[i] + C22[i])

    return new_matrix


# Helper functions
def add(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def subtract(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

if __name__ == "__main__":
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]

    result = strassen_matrix_multiply(A, B)
    print("Result of Strassen's Matrix Multiplication:")
    for row in result:
        print(row)