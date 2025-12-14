import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.exp(x) - 3*x

def false_position(f, a, b, eps=1e-3, Nmax=100):
    if f(a) * f(b) > 0:
        return None, [], "invalid interval"

    table = []
    n = 0
    fa = f(a)
    fb = f(b)

    while n < Nmax:
        c = (a * fb - b * fa) / (fb - fa)
        fc = f(c)

        n += 1
        table.append([n, c, fc, abs(fc)])

        if abs(fc) < eps:
            return c, table, "tolerance reached"

        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

    return c, table, "max iterations reached"

root, table, reason = false_position(f, 0, 1)

print("n\t x_n\t\t f(x_n)\t\t |f(x_n)|")
for r in table:
    print(f"{r[0]}\t {r[1]:.6f}\t {r[2]:+.6f}\t {r[3]:.6f}")

print("\nRoot estimate: x ≈ {:.6f}".format(root))
print("Number of iterations:", len(table))
print("Stopping reason:", reason)

X = np.linspace(0, 1.2, 400)
plt.plot(X, f(X))
plt.axhline(0, color="black")
plt.scatter(root, f(root), color="red")
plt.title("False Position (Regula Falsi) Method")
plt.grid()
plt.show()

errors = [r[3] for r in table]
plt.plot(errors, marker='o')
plt.yscale("log")
plt.xlabel("Iteration")
plt.ylabel("|f(x)|")
plt.title("Convergence (False Position)")
plt.grid()
plt.show()