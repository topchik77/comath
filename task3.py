import math

def f1(x):
    return x**3 - x - 1
def f1_prime(x):
    return 3*x**2 - 1

def f2(x):
    return x - math.cos(x)
def f2_prime(x):
    return 1 + math.sin(x)

def f3(x):
    return math.exp(-x) - x
def f3_prime(x):
    return -math.exp(-x) - 1

def f4(x):
    return x**3 + x**2 + x + 7
def f4_prime(x):
    return 3*x**2 + 2*x + 1

def f5(x):
    return x**2 + 4*math.sin(x)
def f5_prime(x):
    return 2*x + 4*math.cos(x)

def f6(x):
    return math.cos(x) - x * math.exp(x)
def f6_prime(x):
    return -math.sin(x) - math.exp(x) - x * math.exp(x)


def g2(x):  # g(x) for x - cos(x) = 0
    return math.cos(x)

def g3(x):  # g(x) for e^(-x) - x = 0
    return math.exp(-x)

def g4(x):  # g(x) for x^3 - x - 1 = 0
    return (x + 1) ** (1 / 3)


def secant_method(f, x0, x1, tol=1e-6, max_iter=100):
    for i in range(max_iter):
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        if abs(x2 - x1) < tol:
            return x2
        x0, x1 = x1, x2
    return None


def newton_raphson(f, f_prime, x0, tol=1e-6, max_iter=100):
    for i in range(max_iter):
        x1 = x0 - f(x0) / f_prime(x0)
        if abs(x1 - x0) < tol:
            return x1
        x0 = x1
    return None


def iteration_method(g, x0, tol=1e-6, max_iter=100):
    for i in range(max_iter):
        x1 = g(x0)
        if abs(x1 - x0) < tol:
            return x1
        x0 = x1
    return None


def solve_equations():
    equations = [
        {"name": "x^3 - x - 1 = 0", "f": f1, "f_prime": f1_prime, "g": g4},
        {"name": "x - cos(x) = 0", "f": f2, "f_prime": f2_prime, "g": g2},
        {"name": "e^(-x) - x = 0", "f": f3, "f_prime": f3_prime, "g": g3},
        {"name": "x^3 + x^2 + x + 7 = 0", "f": f4, "f_prime": f4_prime, "g": None},
        {"name": "x^2 + 4*sin(x) = 0", "f": f5, "f_prime": f5_prime, "g": None},
        {"name": "cos(x) = x*e^x", "f": f6, "f_prime": f6_prime, "g": None},
    ]

    x0 = 1.5  #guess for Newton-Raphson and Iteration
    x1 = 1.0  #guess for Secant method

    for idx, eq in enumerate(equations, start=1):
        print(f"\n{idx}) Solving equation: {eq['name']}")
        

        root_secant = secant_method(eq['f'], x0, x1)
        print(f"   Root found using Secant Method: {root_secant:.3f}")
        

        root_newton = newton_raphson(eq['f'], eq['f_prime'], x0)
        print(f"   Root found using Newton-Raphson Method: {root_newton:.3f}")
        

        if eq['g'] is not None:
            root_iteration = iteration_method(eq['g'], x0)
            print(f"   Root found using Iteration Method: {root_iteration:.3f}")
        else:
            print("   Iteration Method: Not applicable for this equation.")

solve_equations()
