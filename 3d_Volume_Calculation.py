# Required modules
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, integrate, pi

# Define the function
x = symbols('x')
f = x**3 - 3*x + 1

# Compute the volume
integral = integrate(f**2, (x, 0, 5))
volume = pi * integral
print(f'Volume: {float(volume)} cubic unit')

# Plotting solid of revolution (surface)
X = np.linspace(0, 5, 250)
Y = X**3 - 3*X + 1

# Create mesh for revolution
theta = np.linspace(0, 2*np.pi, 100)
X_grid, Theta = np.meshgrid(X, theta)
Y_grid = (X_grid**3 - 3*X_grid + 1)
Z_grid = Y_grid * np.cos(Theta)
W_grid = Y_grid * np.sin(Theta)

# Plot
fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X_grid, Z_grid, W_grid, cmap='viridis', alpha=0.8)

ax.set_xlabel(r'x$\longrightarrow$')
ax.set_ylabel(r'y$\longrightarrow$')
ax.set_zlabel(r'z$\longrightarrow$')
plt.title(r'Volume calculation of f(x) = $x^3$ - 3x + 1 using $\int_0^5(\pi$ f(x)$^2$) dx')
plt.show()