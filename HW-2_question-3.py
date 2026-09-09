import numpy as np
import matplotlib.pyplot as plt


# Arbitrary units
x = np.linspace(-20, 20, 10_000)
wave_function = 1 / (np.sqrt(10) * np.cosh(x / 5))

plt.plot(x, wave_function, label=r'$\psi(x) = \frac{1}{\sqrt{10}}\,\mathrm{sech}(x/5)$')
plt.xlabel(r'$x$')
plt.ylabel(r'$\psi(x)$')
plt.title(r'Wave function: $\psi(x) = \frac{1}{\sqrt{10}}\,\mathrm{sech}(x/5)$')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
