import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.exp(x) - 3*x

def bisection(f, a, b, eps=1e-3, Nmax=100):
    if a >= b:
        return None, [], "invalid interval order"

    if eps <= 0:
        return None, [], "invalid tolerance"

    if Nmax <= 0:
        return None, [], "invalid max iterations"

    if f(a) * f(b) > 0:
        return None, [], "invalid interval"

    table = []

    for n in range(1, Nmax + 1):
        c = (a + b) / 2
        error = (b - a) / 2
        table.append([n, c, f(c), error])

        if error < eps or abs(f(c)) < eps:
            return c, table, "tolerance reached"

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    return c, table, "max iterations reached"

root, table, reason = bisection(f, 0, 1)
#bisection(f, 1, 0)            invalid interval order
#bisection(f, 0, 0.1)          invalid interval (no sign change)
#bisection(f, 0, 1, -1e-3)     invalid tolerance
#bisection(f, 0, 1, 1e-3, 0)   invalid max iterations

print("Root:", root)
print("Stop reason:", reason)
print("Number of iterations:", len(table))

print("\n n\t x_n\t\t f(x_n)\t\t error")
for r in table:
    print(f"{r[0]}\t {r[1]:.6f}\t {r[2]:+.6f}\t {r[3]:.6f}")

X = np.linspace(0, 1.2, 400)
plt.plot(X, f(X))
plt.axhline(0)

if root is not None:
    plt.scatter(root, f(root), color='red')

plt.title("Bisection Method")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid()
plt.show()

if len(table) > 0:
    errors = [r[3] for r in table]
    plt.plot(errors, marker='o')
    plt.yscale("log")
    plt.xlabel("Iteration")
    plt.ylabel("Error")
    plt.title("Convergence (Bisection)")
    plt.grid()
    plt.show()