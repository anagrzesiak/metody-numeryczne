import numpy as np


def function(x):
    f = x * x
    # f = 2 * x + 3
    # f = 4 ** x - x
    return f


def print_function():
    s = "y = x^2"
    # s = "y = 2x + 3"
    # s = "y = 4^x - x"
    return s


def gauss_quad2(a, b, n):
    x2 = 0.577350
    x1 = -x2
    a1 = 1
    a2 = a1
    t1 = ((a + b) / 2) + ((b - a) / 2) * x1
    t2 = ((a + b) / 2) + ((b - a) / 2) * x2
    sum = 0

    for i in range(0, n):
        sum += ((b - a) / 2)/n * (function(t1) * a1 + function(t2) * a2)

    return sum


def gauss_quad4(a, b, n):
    x4 = 0.86114
    a4 = 0.347851
    x3 = 0.33998
    a3 = 0.65214
    x2 = -x3
    a2 = a3
    x1 = -x4
    a1 = a4
    sum = 0
    t1 = ((b - a) / 2) + ((b + a) / 2) * x1
    t2 = ((b - a) / 2) + ((b + a) / 2) * x2
    t3 = ((b - a) / 2) + ((b + a) / 2) * x3
    t4 = ((b - a) / 2) + ((b + a) / 2) * x4

    for i in range(0, n):
        sum += ((b - a) / 2)/n * (a1*function(t1) + a2*function(t2) + a3*function(t3) + a4*function(t4))

    return sum


def simpson(a, b, n):
    if n % 2:
        raise ValueError("n must be even (received n=%d)" % n)

    h = (b - a) / n
    s = function(a) + function(b)

    for i in range(1, n, 2):
        s += 4 * function(a + i * h)
    for i in range(2, n - 1, 2):
        s += 2 * function(a + i * h)

    return s * h / 3


def monte_carlo(a, b, n):
    x_values = a + (b - a) * np.random.random(n)
    f_values = function(x_values)  # f(x_i) for each rectangle
    areas = f_values * (b - a) / n  # Area for each rectangle

    return sum(areas)


start: float = float(input("ENTER THE BEGINNING OF THE INTERVAL: "))
end: float = float(input("ENTER THE END OF THE INTERVAL: "))
subintervals: int = int(input("ENTER THE NUMBER OF SUBINTERVALS: "))

print("FUNCTION: ", print_function())
print("The given interval is [%s, %s]" % (start, end))
print("The given number of subintervals is: ", subintervals)
print("Simpson method: ", simpson(start, end, subintervals))
print("Monte-Carlo method: ", monte_carlo(start, end, subintervals))
print("Gaussian quadrature, 2-rooted: ", gauss_quad2(start, end, subintervals))
print("Gaussian quadrature, 4-rooted: ", gauss_quad4(start, end, subintervals))
