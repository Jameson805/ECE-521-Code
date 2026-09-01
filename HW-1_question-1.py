import numpy as np
import matplotlib.pyplot as plt


# Physical constants
h = 6.626e-34  # Planck constant (J s)
k_B = 1.3807e-23  # Boltzmann constant (J K^-1)
c = 2.998e8  # Speed of light (m s^-1)


def rayleigh_jeans(nu, temperature):
	"""Return spectral radiant energy density per unit frequency"""
	return 8 * np.pi * nu**2 * k_B * temperature / c**3


def planck(nu, temperature):
	"""Return Planck spectral radiant energy density per unit frequency"""
	x = h * nu / (k_B * temperature)
	return 8 * np.pi * h * nu**3 / (c**3 * np.expm1(x))


frequencies = np.logspace(np.log10(2e12), np.log10(2e15), 2000)


def make_plot(temperature):
	"""Plot both spectral-density models for one temperature"""
	fig, axis = plt.subplots(figsize=(8, 5))
	axis.loglog(
		frequencies,
		rayleigh_jeans(frequencies, temperature),
		label="Rayleigh-Jeans Law",
	)
	axis.loglog(
		frequencies,
		planck(frequencies, temperature),
		label="Planck's Radiation Formula",
	)
	axis.set_title(f"Spectral Radiant Energy Density at T = {temperature:,} K")
	axis.set_xlabel(r"Frequency, $\nu$ (Hz)")
	axis.set_ylabel(r"Spectral radiant energy density, $u_\nu$ (J m$^{-3}$ Hz$^{-1}$)")
	axis.grid(True, which="both", alpha=0.3)
	axis.legend()
	fig.tight_layout()

make_plot(300)
make_plot(9000)
make_plot(15000)
plt.show()
