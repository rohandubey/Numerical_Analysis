
# Defining equations to be solved
# in diagonally dominant form
f1 = lambda x,y,z: (9-2*y-z)/10
f2 = lambda x,y,z: (-22-x+z)/10
f3 = lambda x,y,z: (22+2*x-3*y)/10

# Initial setup
x0 = 3.067
y0 = 0.9
z0 = -2.29
count = 1

# Reading tolerable error
e = float(input('Enter tolerable error: '))

# Implementation of Jacobi Iteration
print('\nCount\tx\ty\tz\n')

condition = True

while condition:
    x1 = f1(x0,y0,z0)
    y1 = f2(x0,y0,z0)
    z1 = f3(x0,y0,z0)
    print('%d\t%0.4f\t%0.4f\t%0.4f\n' %(count, x1,y1,z1))
    e1 = abs(x0-x1);
    e2 = abs(y0-y1);
    e3 = abs(z0-z1);

    count += 1
    x0 = x1
    y0 = y1
    z0 = z1

    condition = e1>e and e2>e and e3>e

print('\nSolution: x=%0.3f, y=%0.3f and z = %0.3f\n'% (x1,y1,z1))
