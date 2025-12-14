import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.exp(x) - 3*x

x0, x1 = 0, 1
eps = 1e-3

print("n\t x_n\t\t f(x_n)\t\t error")

for n in range(1, 100):
    denom = f(x1) - f(x0)
    if denom == 0:
        print("Division by zero.")
        break

    x2 = x1 - f(x1)*(x1 - x0)/denom
    error = abs(x2 - x1)

    print(f"{n}\t {x2:.6f}\t {f(x2):+.6f}\t {error:.6f}")

    if error < eps:
        break

    x0, x1 = x1, x2

root = x2

X = np.linspace(0, 1.2, 400)
plt.plot(X, f(X))
plt.axhline(0)
plt.scatter(root, f(root), color='red')
plt.title("Secant Method")
plt.grid()
plt.show()
