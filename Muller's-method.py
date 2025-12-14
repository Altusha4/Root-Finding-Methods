import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.exp(x) - 3*x

x0, x1, x2 = 0, 0.5, 1
eps = 1e-3

print("n\t x_n\t\t f(x_n)\t\t error")

for n in range(1, 100):
    f0, f1, f2 = f(x0), f(x1), f(x2)
    h0, h1 = x1-x0, x2-x1
    d0, d1 = (f1-f0)/h0, (f2-f1)/h1

    a = (d1-d0)/(h1+h0)
    b = a*h1 + d1
    c = f2

    D = np.sqrt(b*b - 4*a*c)
    denom = b + D if abs(b+D) > abs(b-D) else b - D

    if denom == 0:
        print("Division by zero.")
        break

    x3 = x2 - 2*c/denom
    error = abs(x3 - x2)

    print(f"{n}\t {x3:.6f}\t {f(x3):+.6f}\t {error:.6f}")

    if error < eps:
        break

    x0, x1, x2 = x1, x2, x3

root = x3

X = np.linspace(0, 1.2, 400)
plt.plot(X, f(X))
plt.axhline(0)
plt.scatter(root, f(root), color='red')
plt.title("Muller's Method")
plt.grid()
plt.show()
