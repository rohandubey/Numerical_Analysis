from math import *
def regulaFalsi(func, a , b,MAX_ITER,e):
    if func(a) * func(b) >= 0:
        print("You have not assumed right a and b")
        return -1

    c = a # Initialize result

    for i in range(MAX_ITER):

        # Find the point that touches x axis
        c = (a * func(b) - b * func(a))/ (func(b) - func(a))
        print(i+1,"\t\t",a,"\t",b,"\t",c,"\t",func(c),"\t",abs(c-a))
        # Check if the above found point is root
        if func(c) == 0:
            break
        if abs(c-a)<= e:
            return c
        if abs(c-b)<= e:
            return c
        # Decide the side to repeat the steps
        elif func(c) * func(a) < 0:
            b = c
        else:
            a = c
    return c


##########
fx = input("Enter a polynomial: ")
p = lambda x: eval(fx)
a = input("Enter a: ")
b = input("Enter b: ")
print("Iteration","\t","x0","\t\t","x1","\t\t","x2","\t\t","f(x2)",0.005)
approx = regulaFalsi(p,eval(a),eval(b),200,0.005)
print(approx)
