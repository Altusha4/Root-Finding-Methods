import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.exp(x) - 3*x

def g(x):
    return np.exp(x) / 3

x0 = 0.5
eps = 0.001
Nmax = 100

iteration = 0
x_old = x0

print("n\t x_n\t\t f(x_n)\t\t error")

while iteration < Nmax:
    x_new = g(x_old)
    error = abs(x_new - x_old)
    iteration += 1

    print(f"{iteration}\t {x_new:.6f}\t {f(x_new):+.6f}\t {error:.6f}")

    if error < eps:
        break

    x_old = x_new

root = x_new

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
plt.title("Fixed-Point Iteration Method")
plt.grid()
plt.legend()
plt.show()
