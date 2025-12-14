import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.exp(x) - 3*x

a, b = 0, 1
eps = 1e-3
iteration = 0

print("n\t x_n\t\t f(x_n)\t\t error")

while (b - a) / 2 > eps:
    c = (a + b) / 2
    error = (b - a) / 2
    iteration += 1

    print(f"{iteration}\t {c:.6f}\t {f(c):+.6f}\t {error:.6f}")

    if f(a)*f(c) < 0:
        b = c
    else:
        a = c

root = (a + b) / 2
print("\nRoot:", root)

x = np.linspace(0, 1.2, 400)
plt.plot(x, f(x))
plt.axhline(0)
plt.scatter(root, f(root), color='red')
plt.title("Bisection Method")
plt.grid()
plt.show()
