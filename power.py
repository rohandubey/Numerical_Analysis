import numpy as np
def __find_p(x):
    return np.argwhere(np.isclose(np.abs(x), np.linalg.norm(x, np.inf))).min()

def __iterate(A, x, p):

    y = np.dot(A, x)
    μ = y[p]
    p = __find_p(y)
    error = np.linalg.norm(x - y / y[p],  np.inf)
    x = y / y[p]

    return (error, p, μ, x)

def power_method(A, tolerance=1e-10, max_iterations=20):

    n = A.shape[0]
    x = [1,-1]
    x =np.asarray(x)
    p = __find_p(x)

    error = 1

    x = x / x[p]

    for _ in range(max_iterations):

        if error < tolerance:
            break
        error, p, μ, x = __iterate(A, x, p)
        print("Iteration :",_+1,"\tEigenvalue :",μ,"\tEigenvector :",x)
    return (μ, x)


matrix = []
n = int(input("enter number of unknowns in a matrix : "))
print("Enter elemenmts of matrix A:")
for i in range(n):
   row = []
   for j in range(n):
      element = int(input())
      row.append(element)
   matrix.append(row)
A =np.asarray(matrix)
print("")
a,b = power_method(A)
print("\nEigenvector(final) :\t",a)
print("Eigenvalue(final) :\t",b)
