from math import *
def newton(f,Df,x0,epsilon,max_iter):

    xn = x0
    for n in range(0,max_iter):
        fxn = f(xn)
        print('Solution after',n,'iterations :',xn,'is',fxn)
        if abs(fxn) < epsilon:
            print('Found solution after',n,'iterations.')
            return xn
        Dfxn = Df(xn)
        if Dfxn == 0:
            print('Zero derivative. No solution found.')
            return None
        xn = xn - fxn/Dfxn
    print('Exceeded maximum iterations. No solution found.')
    return None

p = lambda x: x**3 -5*x**2 +8*x -4
Dp = lambda x: 3*x**2 -10*x +8
approx = newton(p,Dp,2,1e-10,20)
print(approx)
