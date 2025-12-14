import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.exp(x) - 3*x

def g(x):
    return np.exp(x) / 3


def fixed_point(g, x0, eps=1e-3, Nmax=100):
    table = []
    n = 0
    x = x0

    while n < Nmax:
        x_new = g(x)
        error = abs(x_new - x)
        n += 1

        table.append([n, x_new, f(x_new), error])

        if error < eps:
            return x_new, table, "tolerance reached"

        x = x_new

    return x, table, "max iterations reached"

root, table, reason = fixed_point(g, 0.5)

print("n\t x_n\t\t f(x_n)\t\t error")
for r in table:
    print(f"{r[0]}\t {r[1]:.6f}\t {r[2]:+.6f}\t {r[3]:.6f}")

print("\nRoot estimate: x ≈ {:.6f}".format(root))
print("Number of iterations:", len(table))
print("Stopping reason:", reason)

X = np.linspace(0, 1.2, 400)
plt.plot(X, f(X))
plt.axhline(0)
plt.scatter(root, f(root), color='red')
plt.title("Fixed-Point Iteration Method")
plt.grid()
plt.show()

errors = [r[3] for r in table]
plt.plot(errors, marker='o')
plt.yscale("log")
plt.xlabel("Iteration")
plt.ylabel("Error")
plt.title("Convergence (Fixed-Point)")
plt.grid()
plt.show()
