import numpy as np
import matplotlib.pyplot as plt
import math

x1 = math.pi
x2 = 10**6

delta = 10.0 ** np.arange(-16, 1, 1)


def estimate(x, delta):

    result = []

    for d in delta:

        if abs(d) < 1e-5:
            # Taylor approximation
            value = -d * np.sin(x) - (d**2 / 2) * np.cos(x)

        else:
            # Stable trigonometric identity
            value = -2 * np.sin(x + d/2) * np.sin(d/2)

        result.append(value)

    return np.array(result)


f1 = estimate(x1, delta)
f2 = estimate(x2, delta)

fig, ax = plt.subplots(1, 2)

ax[0].semilogx(delta, f1)
ax[0].set_title(r"$x=\pi$")
ax[0].grid()

ax[1].semilogx(delta, f2)
ax[1].set_title(r"$x=10^{6}$")
ax[1].grid()

fig.text(0.5, 0.04, r'$\delta$', ha='center')
fig.text(0.04, 0.5, 'f(x)', va='center', rotation='vertical')

plt.show()