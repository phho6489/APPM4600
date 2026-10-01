import numpy as np
import matplotlib.pyplot as plt
import math

x1 = math.pi
x2 = 10**6
delta = 10.0 ** np.arange(-16,1,1)

f1 = np.cos(x1 + delta) - np.cos(x1)
f2 = np.cos(x2 + delta) - np.cos(x2)

g1 = -2 * np.sin(x1 + delta/2) * np.sin(delta/2)
g2 = -2 * np.sin(x2 + delta/2) * np.sin(delta/2)

d1 = np.abs(f1 - g1)
d2 = np.abs(f2 - g2)

fig, ax = plt.subplots(1,2)

ax[0].semilogx(delta,d1)
ax[0].set_title(r"$x=\pi$")
ax[0].grid()
ax[1].semilogx(delta,d2)
ax[1].set_title(r"$x=10^{6}$")

fig.text(0.5, 0.04, r'$\delta$', ha='center')
fig.text(0.04, 0.5, 'Difference', va='center', rotation='vertical')
plt.grid()
plt.show()