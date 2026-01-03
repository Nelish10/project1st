import numpy as np
import matplotlib.pyplot as plt

# Acceleration due to gravity (m/s^2)
g = 9.8

# User inputs
u = float(input("Enter initial velocity (m/s): "))
theta_deg = float(input("Enter launch angle (degrees): "))

# Convert angle to radians
theta = np.radians(theta_deg)

# Calculations
time_of_flight = (2 * u * np.sin(theta)) / g
max_height = (u**2 * (np.sin(theta))**2) / (2 * g)
range_ = (u**2 * np.sin(2 * theta)) / g

# Display results
print("\n--- Projectile Motion Results ---")
print(f"Time of Flight : {time_of_flight:.2f} s")
print(f"Maximum Height : {max_height:.2f} m")
print(f"Range          : {range_:.2f} m")

# Time array
t = np.linspace(0, time_of_flight, 200)

# Trajectory equations
x = u * np.cos(theta) * t
y = u * np.sin(theta) * t - 0.5 * g * t**2

# Plot trajectory
plt.figure()
plt.plot(x, y)
plt.xlabel("Horizontal Distance (m)")
plt.ylabel("Vertical Distance (m)")
plt.title("Projectile Motion Trajectory")
plt.grid(True)
plt.show()
