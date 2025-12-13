import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.exp(x) - 3*x

a = 0
b = 1
eps = 0.001

if f(a) * f(b) > 0:
    print("Bisection cannot be applied.")
else:
    iteration = 0
    table = []

    while (b - a) / 2 > eps:
        c = (a + b) / 2
        error = (b - a) / 2
        iteration += 1

        table.append([iteration, c, f(c), error])

        if f(c) == 0:
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c

    root = (a + b) / 2

    print("Approximate root:", round(root, 6))
    print("Iterations:", iteration)

    print("\nIteration Table")
    print("n\t x_n\t\t f(x_n)\t\t error")
    for row in table:
        print(f"{row[0]}\t {row[1]:.6f}\t {row[2]:+.6f}\t {row[3]:.6f}")

x_vals = np.linspace(0, 1.2, 400)
y_vals = f(x_vals)

plt.figure(figsize=(8, 6))
plt.plot(x_vals, y_vals, label=r'$f(x)=e^x-3x$', color='blue')

plt.axhline(0, color='black', lw=0.5)
plt.axvline(0, color='black', lw=0.5)

plt.scatter([root], [f(root)], color='red', zorder=6)
plt.text(root, f(root) + 0.2, f"root ≈ {round(root,3)}", ha='center')

plt.title("Bisection Method for f(x) = e^x - 3x")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid()
plt.legend()
plt.show()
