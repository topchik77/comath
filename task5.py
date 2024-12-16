import math
import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return x**3 - x - 1

def f_prime(x):
    return 3*x**2 - 1

def bisection_method_with_errors(a, b, tol, max_iter):
    iterations = []
    abs_errors = []
    rel_errors = []
    prev_c = None

    for i in range(max_iter):
        c = (a + b) / 2.0
        iterations.append(c)

        if prev_c is not None:
            abs_error = abs(c - prev_c)
            rel_error = abs_error / abs(c) * 100 if c != 0 else float('inf')
            abs_errors.append(abs_error)
            rel_errors.append(rel_error)

            if abs_error < tol:
                break

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

        prev_c = c

    return iterations, abs_errors, rel_errors

def newton_raphson_with_errors(x0, tol, max_iter):
    iterations = [x0]
    abs_errors = []
    rel_errors = []

    for i in range(1, max_iter + 1):
        x1 = x0 - f(x0) / f_prime(x0)
        iterations.append(x1)

        abs_error = abs(x1 - x0)
        rel_error = abs_error / abs(x1) * 100 if x1 != 0 else float('inf')
        abs_errors.append(abs_error)
        rel_errors.append(rel_error)

        if abs_error < tol:
            break

        x0 = x1

    return iterations, abs_errors, rel_errors


a, b = 1, 2  #interval for bisection
x0 = 1.5     #guess for NewtonRaphson
TOL = 1e-6
MAX_ITER = 20


bisection_iterations, bisection_abs_errors, bisection_rel_errors = bisection_method_with_errors(a, b, TOL, MAX_ITER)
newton_iterations, newton_abs_errors, newton_rel_errors = newton_raphson_with_errors(x0, TOL, MAX_ITER)


plt.figure(figsize=(10, 6))
plt.plot(range(len(bisection_abs_errors)), bisection_abs_errors, label="Bisection abs", marker='o',color='grey')
plt.plot(range(len(newton_abs_errors)), newton_abs_errors, label="Newton-Raphson abs", marker='x', color="brown")
plt.plot(range(len(bisection_rel_errors)), bisection_rel_errors, label="Bisection rel", marker='o')
plt.plot(range(len(newton_rel_errors)), newton_rel_errors, label="Newton-Raphson rel", marker='x')

plt.legend()
plt.grid()
plt.show()


analysis = """
    Analysis of Absolute and Relative Errors

    Absolute Error (Ea): The absolute error tells us the magnitude of the difference between our calculated 
    or measured value and the actual or true value

    Relative Error (Er): Using this method we can determine the magnitude of the absolute error in terms of 
    the actual size of the measurement

    Observations:
    1. Bisection:
       - Absolute errors decrease steadily but relatively slowly because the interval is halved at each step
       - Relative errors also decrease steadily but show more fluctuation near the root

    2. Newton-Raphson:
       - Absolute errors drop rapidly after a few iterations, showcasing the quadratic convergence of the method
       - Relative errors behave similarly, indicating that the method achieves higher accuracy faster than bisection

    Influence of Absolute Error on Iterations:
    - This is more significantly can be seen in the bisection method, where convergence is linear, compared to the Newton-Raphson method,
    where convergence is quadratic

    Example Illustration:
      - The bisection method converges in approximately 20 iterations
      - The Newton-Raphson method converges in fewer iterations due to its faster convergence
    """