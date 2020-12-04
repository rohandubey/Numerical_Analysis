from math import *

def zeros(n,m): # Zeros matrix for preallocation
    Z=[]
    for i in range(n):
        Z.append([0]*m)
    return Z

def D(Func,a,h):    # centered finite difference with step size h at point x=a
	return (Func(a+h)-Func(a-h))/(2*h)

def Richardson_dif(func,a): 
    '''Richardson extrapolation method for numerical calculation of first derivative '''
    k=9 # you can change the order of approximation but try keeping it under 10 to circumvent round-off errors.
    L=zeros(k,k)
    for I in range(k):
        L[I][0]=D(func,a,1/(2**(I+1)))
    for j in range(1,k):
        for i in range(k-j):
            L[i][j]=((4**(j))*L[i+1][j-1]-L[i][j-1])/(4**(j)-1)
    return L[0][k-1]
    
print('Numerical differentiation of Func')
print('%04.20f'%Richardson_dif(lambda x: -0.1*x**4-0.15*x**3-0.5*x**2-0.25*x+1.2 ,0.5))
#################
print('diff(2**cos(pi+sin(x)) at x=pi/2 is equal to = %04.20f'%Richardson_dif(lambda x: 2**cos(pi+sin(x)),pi/3))
# next up, how to implement higher order differentiation with a few tweaks in this code and how to do do partial derivation.
