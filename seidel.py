def seidel(a, x ,b):
    #Finding length of a(3)
    n = len(a)
    # for loop for 3 times as to calculate x, y , z
    for j in range(0, n):
        # temp variable d to store b[j]
        d = b[j]

        # to calculate respective xi, yi, zi
        for i in range(0, n):
            if(j != i):
                d-=a[j][i] * x[i]
        # updating the value of our solution
        x[j] = d / a[j][j]
    # returning our updated solution
    return x

# int(input())input as number of variable to be solved
n = 3
a = []
b = []
# initial solution depending on n(here n=3)
x = [3.067, 0.9, -2.29]
a = [   [10,  2,    1],
        [1,  10,      -1],
        [-2,  3,      10]]
b = [9.0, -22, 22.0]
print("Iteration no 0 sol =",x)

#loop run for m times depending on m the error value
for i in range(0, 25):
    x = seidel(a, x, b)
    #print each time the updated solution
    print("Iteration no",i+1,"sol =",x)
