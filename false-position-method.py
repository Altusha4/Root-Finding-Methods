import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.exp(x) - 3*x

# Parameters
a = 0.0
b = 1.0
eps = 0.001
Nmax = 100

iteration = 0

if f(a) * f(b) > 0:
    print("False Position method cannot be applied.")
else:
    print("n\t x_n\t\t f(x_n)\t\t error")

    c_old = a

    while iteration < Nmax:
        # False Position formula
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        error = abs(c - c_old)
        iteration += 1

        print(f"{iteration}\t {c:.6f}\t {f(c):+.6f}\t {error:.6f}")

        if abs(f(c)) < eps or error < eps:
            break

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

        c_old = c

    root = c

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
plt.title("False Position (Regula Falsi) Method")
plt.grid()
plt.legend()
plt.show()
