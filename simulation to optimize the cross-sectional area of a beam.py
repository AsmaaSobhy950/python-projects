"""Develop a Python simulation to optimize the cross-sectional area of a beam
Young’s Modulus = 200 GPa
Max allowable deflection = 5 mm
Density = 7850 kg/m³"""

import numpy as np

# Given data
P = int(input("please enter the load in N:")) * 1000          # Load (N)
L = int(input("please enter the length in m:"))                  # Length (m)
E = 200 * 10**9        # Young's modulus (Pa)
delta_max = 0.005      # Max deflection (m)
density = 7850         # kg/m^3

# Assume rectangular cross-section (b = h for simplicity)
linspace= np.linspace(0.01, 0.3, 200)  # Range of heights to evaluate (m)
sizes = np.linspace(0.01, 0.3, 200)

valid_designs = []

for h in sizes:
    b = h
    I = (b * h**3) / 12   # Moment of inertia
    A = b * h             # Area
    
    # Deflection formula for simply supported beam
    delta = (P * L**3) / (48 * E * I)
    
    # Stress (approx)
    stress = P / A
    
    if delta <= delta_max:
        weight = A * L * density
        valid_designs.append((h, weight, delta, stress))

# Get optimal design (minimum weight)
optimal = min(valid_designs, key=lambda x: x[1])

print("Optimal Height (m):", round(optimal[0], 4))
print("Weight (kg):", round(optimal[1], 2))
print("Deflection (m):", round(optimal[2], 6))
print("Stress (Pa):", round(optimal[3], 2))
