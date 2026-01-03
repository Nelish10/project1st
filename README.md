# Projectile Motion Simulator

Python program that simulates projectile motion using physics equations.

## Features
- Time of flight
- Maximum height
- Range
- Trajectory graph

## How to Run
pip install numpy matplotlib
python projectile.py


import numpy as np
import matplotlib.pyplot as plt

# Gravity
g = 9.8

# User Inputs
u = float(input("Enter initial velocity (m/s): "))
theta = float(input("Enter angle (degrees): "))

# Convert angle to radians
theta = np.radians(theta)

# Calculations
time_of_flight = (2 * u * np.sin(theta)) / g
max_height = (u**2 * np.sin(theta)**2) / (2 * g)
range_ = (u**2 * np.sin(2 * theta)) / g

print("\nResults:")
print(f"Time of Flight: {time_of_flight:.2f} s")
print(f"Maximum Height: {max_height:.2f} m")
print(f"Range: {range_:.2f} m")

# Time array
t = np.linspace(0, time_of_flight, 100)

# Trajectory
x = u * np.cos(theta) * t
y = u * np.sin(theta) * t - 0.5 * g * t**2

# Plot
plt.plot(x, y)
plt.xlabel("Horizontal Distance (m)")
plt.ylabel("Vertical Distance (m)")
plt.title("Projectile Motion Trajectory")
plt.grid()
plt.show()
