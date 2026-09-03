import numpy as np
import matplotlib.pyplot as plt
import math

x = np.arange(1.920, 2.080,  0.001)
y = np.poly1d([1,-18,144,-672,2016,-4032,5376,-4608,2304,-512])
z = y(x)

def func(x):
    return (x-2)**9

f = func(x)

fig, ax = plt.subplots(1,2)

ax[0].plot(x,z)
ax[0].set_title("Estimate")
ax[0].grid()
ax[1].plot(x,f)
ax[1].set_title("Exact")

fig.text(0.5, 0.04, 'x with stepsize 0.001', ha='center')
fig.text(0.04, 0.5, 'p(x)', va='center', rotation='vertical')
plt.grid()
plt.show()
