import math
import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return x**3 - x - 1


def f_prime(x):
    return 3*x**2 - 1

def bisection_method(a, b, tol, max_iter):
    iterations = []
    for i in range(max_iter):
        c = (a + b) / 2.0
        iterations.append(c)
        if abs(f(c)) < tol:
            break
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return iterations

# Secant Method
def secant_method(x0, x1, tol, max_iter):
    iterations = [x0, x1]
    for i in range(2, max_iter + 1):
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        iterations.append(x2)
        if abs(x2 - x1) < tol:
            break
        x0, x1 = x1, x2
    return iterations


def g(x):
    return (x + 1) ** (1 / 3)

def iteration_method(x0, tol, max_iter):
    iterations = [x0]
    for i in range(1, max_iter + 1):
        x1 = g(x0)
        iterations.append(x1)
        if abs(x1 - x0) < tol:
            break
        x0 = x1
    return iterations


def newton_raphson(x0, tol, max_iter):
    iterations = [x0]
    for i in range(1, max_iter + 1):
        x1 = x0 - f(x0) / f_prime(x0)
        iterations.append(x1)
        if abs(x1 - x0) < tol:
            break
        x0 = x1
    return iterations


a, b = 1, 2  # interval for bisection 
x0 = 1.5     #guess for Secant, Iteration, and Newton-Raphson methods
x1 = 1.0     #guess for Secant method
TOL = 1e-6
MAX_ITER = 7


bisection_results = bisection_method(a, b, TOL, MAX_ITER)
secant_results = secant_method(x0, x1, TOL, MAX_ITER)
iteration_results = iteration_method(x0, TOL, MAX_ITER)
newton_results = newton_raphson(x0, TOL, MAX_ITER)


def results(results, max_len):
    return results + ["--"] * (max_len - len(results))

bisection_results = results(bisection_results, MAX_ITER + 1)
secant_results = results(secant_results, MAX_ITER + 1)
iteration_results = results(iteration_results, MAX_ITER + 1)
newton_results = results(newton_results, MAX_ITER + 1)


print("{:<10} {:<20} {:<20} {:<20} {:<20}".format(
    "Root", "Bisection Method", "Secant Method", "Iteration Method", "Newton-Raphson"))
print("-" * 90)

for i in range(MAX_ITER + 1):
    print("{:<10} {:<20} {:<20} {:<20} {:<20}".format(
        f"x{i}", bisection_results[i], secant_results[i], iteration_results[i], newton_results[i]))



plt.figure(figsize=(10, 6))

bisection_results_float = [r for r in bisection_results if r != "--"]
secant_results_float = [r for r in secant_results if r != "--"]
iteration_results_float = [r for r in iteration_results if r != "--"]
newton_results_float = [r for r in newton_results if r != "--"]


plt.plot(range(len(bisection_results_float)), bisection_results_float, label="Bisection Method", marker='o')
plt.plot(range(len(secant_results_float)), secant_results_float, label="Secant Method", marker='x')
plt.plot(range(len(iteration_results_float)), iteration_results_float, label="Iteration Method", marker='s')
plt.plot(range(len(newton_results_float)), newton_results_float, label="Newton-Raphson", marker='d')

plt.title("plot the resulting graphs in one")
plt.xlabel("Iteration")
plt.ylabel("Approximation of Root")
plt.legend()
plt.grid()
plt.show()