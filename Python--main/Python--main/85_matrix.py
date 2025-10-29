# Function to input a 3x3 matrix
def input_matrix(name):
    print(f"Enter elements of {name} matrix (3x3):")
    matrix = []
    for i in range(3):
        row = list(map(int, input().split()))
        matrix.append(row)
    return matrix

# Function to print matrix
def print_matrix(matrix):
    for row in matrix:
        print(row)

# Function to add two matrices
def add_matrices(A, B):
    return [[A[i][j] + B[i][j] for j in range(3)] for i in range(3)]

# Function to subtract two matrices
def subtract_matrices(A, B):
    return [[A[i][j] - B[i][j] for j in range(3)] for i in range(3)]

# Function to multiply two matrices
def multiply_matrices(A, B):
    result = [[0 for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                result[i][j] += A[i][k] * B[k][j]
    return result

# Function to find transpose of a matrix
def transpose_matrix(A):
    return [[A[j][i] for j in range(3)] for i in range(3)]

# ---- Main Program ----
A = input_matrix("First")
B = input_matrix("Second")

print("\n\nMatrix A:")
print_matrix(A)
print("\n\nMatrix B:")
print_matrix(B)

print("\n\nAddition of A and B:")
print_matrix(add_matrices(A, B))

print("\n\nSubtraction of A and B (A - B):")
print_matrix(subtract_matrices(A, B))

print("\n\nMultiplication of A and B:")
print_matrix(multiply_matrices(A, B))

print("\n\nTranspose of Matrix A:")
print_matrix(transpose_matrix(A))

print("\n\nTranspose of Matrix B:")
print_matrix(transpose_matrix(B))

print("\n\nThis program is executed by Vanshika Khanna , 0231BCA033")