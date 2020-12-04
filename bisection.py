from math import *
def bisection(f,a,b,N):

    if f(a)*f(b) >= 0:
        print("Bisection method fails.")
        return None
    a_n = a
    b_n = b
    for n in range(1,N+1):
        m_n = (a_n + b_n)/2
        f_m_n = f(m_n)
        print(n,"\t\t",a_n,"\t",b_n,"\t",m_n,"\t",f_m_n)
        if f(a_n)*f_m_n < 0:
            a_n = a_n
            b_n = m_n
        elif f(b_n)*f_m_n < 0:
            a_n = m_n
            b_n = b_n
        elif f_m_n == 0:
            print("Found exact solution.")
            return m_n
        else:
            print("Bisection method fails.")
            return None
    return (a_n + b_n)/2

#############
# f = lambda x: 0.016 - (4+x)/(((42-(2*x))**2)*(28-x))
f = input("Enter a polynomial: ")
p = lambda x: eval(f)
a = input("Enter a: ")
b = input("Enter b: ")
print("Iteration","\t","x0","\t\t","x1","\t\t","x2","\t\t","f(x2)")
approx_phi = bisection(p,eval(a),eval(b),11,)
print(approx_phi)
