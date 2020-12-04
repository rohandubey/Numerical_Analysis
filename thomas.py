import numpy as np

## Tri Diagonal Matrix Algorithm(a.k.a Thomas algorithm) solver
def TDMAsolver(a, b, c, d):

    nf = len(d) # number of equations
    ac, bc, cc, dc = map(np.array, (a, b, c, d)) # copy arrays
    for it in range(1, nf):
        mc = ac[it-1]/bc[it-1]
        bc[it] = bc[it] - mc*cc[it-1]
        dc[it] = dc[it] - mc*dc[it-1]
        print(it+1,mc,bc[it],dc[it])

    xc = bc
    xc[-1] = dc[-1]/bc[-1]

    for il in range(nf-2, -1, -1):
        xc[il] = (dc[il]-cc[il]*xc[il+1])/bc[il]

    return xc

# A = np.array([[10,2,0,0],[3,10,4,0],[0,1,7,5],[0,0,3,4]],dtype=float)

a = np.array([-1,   -1, -1])
b = np.array([2.04,    2.04,    2.04,      2.04])
c = np.array([-1,   -1, -1])
d = np.array([40.8,    0.8, 0.8,   200.8])

print("\te","\t\t\tf","\t\tr")
print ("\n final Sol ",TDMAsolver(a, b, c, d))
#compare against numpy linear algebra library
# print (np.linalg.solve(A, d))
