import numpy as np

def F(x, y):
    return np.array([
        3*x**2 - y**2,
        3*x*y**2 - x**3 - 1
    ])

def J(x, y):
    return np.array([
        [6*x, -2*y],
        [3*y**2 - 3*x**2, 6*x*y]
    ])

# Part (a): Fixed matrix
A = np.array([
    [1/6, 1/18],
    [0, 1/6]
])

x, y = 1.0, 1.0


Nmax = 100
tol = 1e-6
print("Part (a)")
for n in range(Nmax):
    print(n, x, y)
    z = np.array([x, y]) - A @ F(x, y)
    if (np.sqrt((x - z[0])**2 + (y - z[1])**2) < tol):
        break
    x, y = z

# Part (c): Newton's method
x, y = 1.0, 1.0

print("\nPart (c)")
for n in range(6):
    print(n, x, y)
    z = np.array([x, y]) - np.linalg.solve(J(x, y), F(x, y))
    if (np.sqrt((x - z[0])**2 + (y - z[1])**2) < tol):
        break    
    x, y = z