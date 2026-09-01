import numpy as np
import matplotlib.pyplot as plt


# Wavelengths are given in angstroms; stopping potential in volts.
wavelength_angstrom = np.array([2536, 2830, 3039, 3302, 3663, 4358], dtype=float)
stopping_potential = np.array([2.60, 2.11, 1.81, 1.47, 1.10, 0.57], dtype=float)

# Physical constants
speed_of_light = 3e8  # m/s

# Conversions
frequency = speed_of_light / (wavelength_angstrom * 1e-10) #Hz
maximum_kinetic_energy = stopping_potential  # eV

plt.scatter(frequency, maximum_kinetic_energy, color="navy", label="Measured data")

# Linear fit: KE_max = h f - work function (when KE is in eV).
fit = np.polyfit(frequency, maximum_kinetic_energy, 1)
print(f"Empirical slope (h) = {fit[0]:.4g} eV·s")
fit_frequency = np.linspace(frequency.min(), frequency.max(), 200)
plt.plot(fit_frequency, np.polyval(fit, fit_frequency), "--", label="Linear fit")

plt.xlabel("Frequency (Hz)")
plt.ylabel("Maximum Kinetic Energy (eV)")
plt.title("Photoelectric Effect: Maximum Kinetic Energy vs. Frequency")
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()
