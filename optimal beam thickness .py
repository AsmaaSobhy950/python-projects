"""Design a Python model to calculate the optimal beam thickness that minimizes 
material cost while maintaining structural safety under load.
Material yield strength = 250 MPa
Safety factor = 2"""

import numpy as np

# Given data
load =int(input("please enter the load in kg:"))  * 1000  # N
length = int(input("please enter the length in m:"))  # m
yield_strength = 250 * 10**6  # Pa
safety_factor = 2

# Allowable stress
allowable_stress = yield_strength / safety_factor

# Try different thickness values
linspace = np.linspace(0.01, 0.1, num=100)  # Thickness range from 0.01 m to 0.1 m
thickness = np.linspace(linspace, linspace, num=100)  # Generate 100 thickness values
stress = load / thickness

# Find valid thickness
valid = thickness[stress <= allowable_stress]

optimal_thickness = min(valid)

print(f"Optimal Thickness: {optimal_thickness:} m")
