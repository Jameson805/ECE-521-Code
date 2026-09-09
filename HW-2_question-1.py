import numpy as np
import matplotlib.pyplot as plt


# Arbitrary units
k0 = 1.0
x = np.linspace(-20, 20, 10_000)

probability_density = np.empty_like(x)
nonzero = x != 0
probability_density[nonzero] = (
	np.sin(k0 * x[nonzero]) ** 2
	/ (np.pi * k0 * x[nonzero] ** 2)
)
# Special handling for x = 0
probability_density[~nonzero] = k0 / np.pi

plt.plot(x, probability_density, label=r'$|\psi(x,0)|^2$')
plt.xlabel(r'$x$')
plt.ylabel(r'$|\psi(x,0)|^2$')
plt.title(r'Probability density: $|\psi(x,0)|^2 = \frac{\sin^2(k_0x)}{\pi k_0x^2}$')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
