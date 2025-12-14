import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.exp(x) - 3*x

def df(x):
    return np.exp(x) - 3

def newton(f, df, x0, eps=1e-3, Nmax=100):

    if eps <= 0:
        return None, [], "invalid tolerance"

    if Nmax <= 0:
        return None, [], "invalid max iterations"

    table = []
    x = x0

    for n in range(1, Nmax + 1):
        if df(x) == 0:
            return None, table, "derivative is zero"

        x_new = x - f(x) / df(x)
        error = abs(x_new - x)

        table.append([n, x_new, f(x_new), error])

        if error < eps:
            return x_new, table, "tolerance reached"

        x = x_new

    return x, table, "max iterations reached"

root, table, reason = newton(f, df, 0.5)
#newton(f, df, 0.5, -1e-3)      invalid tolerance
#newton(f, df, 0.5, 1e-3, 0)    invalid max iterations

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

plt.title("Newton–Raphson Method")
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
    plt.title("Convergence (Newton)")
    plt.grid()
    plt.show()