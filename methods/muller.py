import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.exp(x) - 3*x

def muller(f, x0, x1, x2, eps=1e-3, Nmax=100):
    table = []

    for n in range(1, Nmax+1):
        f0, f1, f2 = f(x0), f(x1), f(x2)
        h0, h1 = x1-x0, x2-x1
        d0, d1 = (f1-f0)/h0, (f2-f1)/h1

        a = (d1-d0)/(h1+h0)
        b = a*h1 + d1
        c = f2

        D = b*b - 4*a*c
        if D < 0:
            return None, table, "complex root"

        D = np.sqrt(D)
        denom = b + D if abs(b+D) > abs(b-D) else b - D
        if denom == 0:
            return None, table, "division by zero"

        x3 = x2 - 2*c/denom
        error = abs(x3 - x2)
        table.append([n, x3, f(x3), error])

        if error < eps:
            return x3, table, "tolerance reached"

        x0, x1, x2 = x1, x2, x3

    return x3, table, "max iterations reached"

root, table, reason = muller(f, 0, 0.5, 1)
print("Root:", root)
print("Stop reason:", reason)

print("n\t x_n\t\t f(x_n)\t\t error")
for r in table:
    print(f"{r[0]}\t {r[1]:.6f}\t {r[2]:+.6f}\t {r[3]:.6f}")

X = np.linspace(0, 1.2, 400)
plt.plot(X, f(X))
plt.axhline(0)
plt.scatter(root, f(root), color='red')
plt.title("Muller's Method")
plt.grid()
plt.show()

errors = [r[3] for r in table]
plt.plot(errors, marker='o')
plt.yscale("log")
plt.xlabel("Iteration")
plt.ylabel("Error")
plt.title("Convergence (Muller)")
plt.grid()
plt.show()