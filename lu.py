import pprint
import numpy as np
import scipy.linalg   # SciPy Linear Algebra Library

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
print("Enter elemenmts of matrix C:")
C=[]
for i in range(n):
  element = int(input())
  C.append(element)
C =np.asarray(C)
# A = np.array([ [3, -1, 2], [1, 2, 3], [2, -2, -1] ])
# C = np.array([      [12],            [11],            [2]        ])
L, U = scipy.linalg.lu(A,permute_l=True)

print ("    A:")
pprint.pprint(A)

print ("    C:")
pprint.pprint(C)

print ("\n    L:")
pprint.pprint(L)

print ("    U:")
pprint.pprint(U)

Z  = scipy.linalg.solve(L,C)
print ("    z:")
pprint.pprint(Z)

X  = scipy.linalg.solve(U,Z)
print ("    Solution(x):")
pprint.pprint(X)
