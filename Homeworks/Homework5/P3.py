import numpy as np

def f(x, y, z):
    return x**2 + 4*y**2 + 4*z**2 - 16

x, y, z = 1.0, 1.0, 1.0

print("n       x           y           z          residual")


Nmax = 100
tol = 1e-6
for n in range(Nmax):
    residual = abs(f(x, y, z))
    print(n, x, y, z, residual, residual)

    fx = 2*x
    fy = 8*y
    fz = 8*z

    d = f(x, y, z) / (fx**2 + fy**2 + fz**2)

    xstar = x - d*fx
    ystar = y - d*fy
    zstar = z - d*fz

    if (np.sqrt((x - xstar)**2 + (y - ystar)**2 + (z - zstar)**2) < tol):
        break

    x = xstar
    y = ystar
    z = zstar