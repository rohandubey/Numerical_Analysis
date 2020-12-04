import numpy as np

def sor_solver(A, b, omega, initial_guess, convergence_criteria):
  phi = initial_guess[:]
  count =0
  residual = np.linalg.norm(np.matmul(A, phi) - b) #Initial residual
  while residual > convergence_criteria:
    count+=1
    for i in range(A.shape[0]):
      sigma = 0
      for j in range(A.shape[1]):
        if j != i:
          sigma += A[i][j] * phi[j]
      phi[i] = (1 - omega) * phi[i] + (omega / A[i][i]) * (b[i] - sigma)
    residual = np.linalg.norm(np.matmul(A, phi) - b)
    print(count,"\t",'Residual: {0:10.6g}'.format(residual),"\t",phi)
  return phi


#An example case that mirrors the one in the Wikipedia article
residual_convergence = 1e-8
omega = 1.25 #Relaxation factor
N=3 ###############
A = np.ones((N, N))
A[0][0] = 3
A[0][1] = -1
A[0][2] = 1

A[1][0] = -1
A[1][1] = 3
A[1][2] = -1

A[2][0] = 1
A[2][1] = -1
A[2][2] = 3

b = np.ones(N)
b[0] = -1
b[1] = 7
b[2] = -7

initial_guess = np.zeros(N)
phi = sor_solver(A, b, omega, initial_guess, residual_convergence)
print(phi)
