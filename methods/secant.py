import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.exp(x) - 3*x

def secant(f, x0, x1, eps=1e-3, Nmax=100):

    if eps <= 0:
        return None, [], "invalid tolerance"

    if Nmax <= 0:
        return None, [], "invalid max iterations"

    if x0 == x1:
        return None, [], "invalid initial guesses (x0 = x1)"

    table = []

    for n in range(1, Nmax + 1):

        denom = f(x1) - f(x0)
        if denom == 0:
            return None, table, "division by zero"

        x2 = x1 - f(x1) * (x1 - x0) / denom
        error = abs(x2 - x1)

        table.append([n, x2, f(x2), error])

        if error < eps:
            return x2, table, "tolerance reached"

        x0, x1 = x1, x2

    return x2, table, "max iterations reached"

root, table, reason = secant(f, 0, 1)
#secant(f, 0, 0)            invalid initial guesses
#secant(f, 0, 1, -1e-3)     invalid tolerance
#secant(f, 0, 1, 1e-3, 0)   invalid max iterations

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

plt.title("Secant Method")
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
    plt.title("Convergence (Secant)")
    plt.grid()
    plt.show()