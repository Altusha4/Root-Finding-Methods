import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.exp(x) - 3*x

def df(x):
    return np.exp(x) - 3

x = 0.5
eps = 1e-3

print("n\t x_n\t\t f(x_n)\t\t error")

for n in range(1, 100):
    if df(x) == 0:
        print("Division by zero.")
        break

    x_new = x - f(x)/df(x)
    error = abs(x_new - x)

    print(f"{n}\t {x_new:.6f}\t {f(x_new):+.6f}\t {error:.6f}")

    if error < eps:
        break
    x = x_new

root = x_new

X = np.linspace(0, 1.2, 400)
plt.plot(X, f(X))
plt.axhline(0)
plt.scatter(root, f(root), color='red')
plt.title("Newton-Raphson Method")
plt.grid()
plt.show()
