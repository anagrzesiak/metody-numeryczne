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


def rectangle(first_interval, second_interval, intervals_number):
    step = (second_interval - first_interval) / intervals_number
    integral = 0

    for i in range(intervals_number):
        integral += step * function(first_interval + (i - 1) * step)

    return integral


def trapezoid(first_interval, second_interval, intervals_number):
    step = (second_interval - first_interval) / intervals_number
    integral = 0.5 * (function(first_interval) + function(second_interval))

    for i in range(intervals_number):
        integral += function(first_interval + step * i)

    integral *= step
    return integral


f_interval: float = float(input("ENTER THE BEGINNING OF THE INTERVAL: "))
s_interval: float = float(input("ENTER THE END OF THE INTERVAL: "))
i_number: int = int(input("ENTER THE NUMBER OF INTERVALS (NUMBER OF ITERATIONS): "))

print("FUNCTION: ", print_function())
print("The given interval is [%s, %s]" % (f_interval, s_interval))
print("The given number of intervals (number of iterations) is", i_number)
print("Rectangular method: ", rectangle(f_interval, s_interval, i_number))
print("Trapezoidal method: ", trapezoid(f_interval, s_interval, i_number))
