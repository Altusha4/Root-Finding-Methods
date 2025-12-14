import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.exp(x) - 3*x

def false_position(f, a, b, eps=1e-3, Nmax=100):
    if a >= b:
        return None, [], "invalid interval order"

    if eps <= 0:
        return None, [], "invalid tolerance"

    if Nmax <= 0:
        return None, [], "invalid max iterations"

    if f(a) * f(b) > 0:
        return None, [], "invalid interval"

    table = []
    fa, fb = f(a), f(b)

    for n in range(1, Nmax + 1):

        if fb - fa == 0:
            return None, table, "division by zero (fb - fa = 0)"

        c = (a * fb - b * fa) / (fb - fa)
        fc = f(c)
        error = abs(fc)

        table.append([n, c, fc, error])

        if error < eps:
            return c, table, "tolerance reached"

        if fa * fc < 0:
            b, fb = c, fc
        else:
            a, fa = c, fc

    return c, table, "max iterations reached"

root, table, reason = false_position(f, 0, 1)
#false_position(f, 1, 0)             invalid interval order
#false_position(f, 0, 0.2)           invalid interval
#false_position(f, 0, 1, -1e-3)      invalid tolerance
#false_position(f, 0, 1, 1e-3, 0)    invalid max iterations

print("Root:", root)
print("Stop reason:", reason)
print("Number of iterations:", len(table))

print("\n n\t x_n\t\t f(x_n)\t\t |f(x_n)|")
for r in table:
    print(f"{r[0]}\t {r[1]:.6f}\t {r[2]:+.6f}\t {r[3]:.6f}")

X = np.linspace(0, 1.2, 400)
plt.plot(X, f(X))
plt.axhline(0)

if root is not None:
    plt.scatter(root, f(root), color='red')

plt.title("False Position (Regula Falsi) Method")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid()
plt.show()

if len(table) > 0:
    errors = [r[3] for r in table]
    plt.plot(errors, marker='o')
    plt.yscale("log")
    plt.xlabel("Iteration")
    plt.ylabel("|f(x)|")
    plt.title("Convergence (False Position)")
    plt.grid()
    plt.show()