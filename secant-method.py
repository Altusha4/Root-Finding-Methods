import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.exp(x) - 3*x

# Parameters
x0 = 0.0          # first initial guess
x1 = 1.0          # second initial guess
eps = 0.001
Nmax = 100

iteration = 1
x_prev = x0
x_curr = x1

print("n\t x_n\t\t f(x_n)\t\t error")

while iteration < Nmax:
    x_next = x_curr - f(x_curr) * (x_curr - x_prev) / (f(x_curr) - f(x_prev))
    error = abs(x_next - x_curr)

    print(f"{iteration}\t {x_next:.6f}\t {f(x_next):+.6f}\t {error:.6f}")

    if error < eps:
        break

    x_prev = x_curr
    x_curr = x_next
    iteration += 1

root = x_next

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
plt.title("Secant Method")
plt.grid()
plt.legend()
plt.show()
