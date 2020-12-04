from math import *
def newton(f,Df,DDf,x0,epsilon,max_iter):

    xn = x0
    for n in range(0,max_iter):
        fxn = f(xn)
        print('Solution after',n,'iterations :',xn,'is',fxn)
        if abs(fxn) < epsilon:
            print('Found solution after',n,'iterations.')
            return xn
        Dfxn = Df(xn)
        DDfxn = DDf(xn)
        if Dfxn == 0:
            print('Zero derivative. No solution found.')
            return None
        xn = xn - (fxn*Dfxn)/((Dfxn**2)-(fxn*DDfxn))
    print('Exceeded maximum iterations. No solution found.')
    return None

p = lambda x: x**3 - 5*x**2 + 7*x -3
Dp = lambda x: 3*x**2 -10*x +7
DDp = lambda x: 6*x -10
approx = newton(p,Dp,DDp,0,1e-10,6)
print(approx)
