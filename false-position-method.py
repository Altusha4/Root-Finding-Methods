import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.exp(x) - 3*x

a, b = 0, 1
eps = 1e-3
c_old = a

print("n\t x_n\t\t f(x_n)\t\t error")

for n in range(1, 100):
    denom = f(b) - f(a)
    if denom == 0:
        print("Division by zero.")
        break

    c = (a*f(b) - b*f(a))/denom
    error = abs(c - c_old)

    print(f"{n}\t {c:.6f}\t {f(c):+.6f}\t {error:.6f}")

    if error < eps:
        break

    if f(a)*f(c) < 0:
        b = c
    else:
        a = c

    c_old = c

root = c

# Plot
X = np.linspace(0, 1.2, 400)
plt.plot(X, f(X))
plt.axhline(0)
plt.scatter(root, f(root), color='red')
plt.title("False Position Method")
plt.grid()
plt.show()
