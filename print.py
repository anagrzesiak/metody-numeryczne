#rk method

def f(x, y):
    return x * x + y


def print_f():
    output = "y'(x) = x^2 + y"
    return output


def euler(x, y, end, step):
    stop = (end - x) / step
    x_temp = x
    y_temp = y
    for i in range(int(stop + 1)):
        y_temp = y_temp + step * f(x_temp, y_temp)
        x_temp = x_temp + step
    print("EULER'S METHOD= ", y_temp)
    return y_temp


def f_rk2(x, y, step):
    k1 = f(x, y)
    k2 = f(x + step, y + step * k1)
    function = 0.5 * (k1 + k2)
    return function


def rk2(x, y, end, step):
    stop = (end - x) / step
    x_temp = x
    y_temp = y
    for i in range(int(stop + 1)):
        function = f_rk2(x_temp, y_temp, step)
        y_temp = y_temp + step * function
        x_temp = x_temp + step
    print("RK2 METHOD= ", y_temp)
    return y_temp


def f_rk4(x, y, step):
    k1 = f(x, y)
    k2 = f(x + (0.5 * step), y + (0.5 * step * k1))
    k3 = f(x + (0.5 * step), y + (0.5 * step * k2))
    k4 = f(x + step, y + (step * k3))
    function = (1 / 6) * (k1 + (2 * k2) + (2 * k3) + k4)
    return function


def rk4(x, y, end, step):
    stop = (end - x) / step
    x_temp = x
    y_temp = y
    for i in range(int(stop + 1)):
        y_temp = y_temp + (step * f_rk4(x_temp, y_temp, step))
        x_temp = x_temp + step
    print("RK4 METHOD= ", y_temp)
    return y_temp


print(print_f())
x0: float = float(input("ENTER X0: "))
y0: float = float(input("ENTER Y0: "))
end_point: float = float(input("ENTER ENDPOINT: "))
h: float = float(input("ENTER STEP: "))

euler(x0, y0, end_point, h)
rk2(x0, y0, end_point, h)
rk4(x0, y0, end_point, h)
