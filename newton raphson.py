import numpy as np
from scipy.optimize import fsolve

def jacobian(xy):
    x, y = xy
    return [[y, x + 2],
            [2 * x, 8 * y]]


def function(xy):
    x, y = xy
    return [x*y + (2 * y) - 2, (x ** 2) + (4 * y ** 2) - 4]


def newton(fun, init, jacobian):
    max_iter = 50
    epsilon = 1e-8

    last = init

    for k in range(max_iter):
        J = np.array(jacobian(last))
        F = np.array(fun(last))

        diff = np.linalg.solve(J, -F)
        last = last + diff

        if np.linalg.norm(diff) < epsilon:
            print('convergent!!! number of iterations:', k)
            break

    else:
        print('not convergent')

    return last


x_sol = newton(function, [1, 2], jacobian)
print('solution:', x_sol)
print('initial value: ', [1, 2])
print('value of the function at root: ', function(x_sol))
print('value of the function at initial value: ', function([1, 2]))

# verification using fsvole from Scipy
# x0 = [2, 2]
# sol = fsolve(function, x0, fprime=jacobian, full_output=1)
# print('solution exercice fsolve:', sol)