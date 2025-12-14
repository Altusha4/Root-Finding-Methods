import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.exp(x) - 3*x

# Parameters (three initial guesses)
x0 = 0.0
x1 = 0.5
x2 = 1.0

eps = 0.001
Nmax = 100
iteration = 0

print("n\t x_n\t\t f(x_n)\t\t error")

while iteration < Nmax:
    f0 = f(x0)
    f1 = f(x1)
    f2 = f(x2)

    h0 = x1 - x0
    h1 = x2 - x1

    d0 = (f1 - f0) / h0
    d1 = (f2 - f1) / h1

    a = (d1 - d0) / (h1 + h0)
    b = a * h1 + d1
    c = f2

    D = np.sqrt(b**2 - 4*a*c)

    if abs(b + D) > abs(b - D):
        denom = b + D
    else:
        denom = b - D

    x3 = x2 - (2*c) / denom
    error = abs(x3 - x2)

    iteration += 1
    print(f"{iteration}\t {x3:.6f}\t {f(x3):+.6f}\t {error:.6f}")

    if error < eps:
        break

    x0 = x1
    x1 = x2
    x2 = x3

root = x3

print("\nApproximate root:", round(root, 6))
print("Iterations:", iteration)

x_vals = np.linspace(0, 1.2, 400)
y_vals = f(x_vals)

plt.figure(figsize=(8, 6))
plt.plot(x_vals, y_vals, label=r'$f(x)=e^x-3x$')
plt.axhline(0, color='black')

plt.scatter(root, f(root), color='red')
plt.text(root, f(root)+0.2, f"root ≈ {round(root,3)}", ha='center')

plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Muller's Method")
plt.grid()
plt.legend()
plt.show()
