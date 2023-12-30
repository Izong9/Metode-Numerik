import numpy as np

def trapezoidal_method(func, lower_limit, upper_limit, num_intervals):
    h = (upper_limit - lower_limit) / num_intervals
    result = 0.5 * (func(lower_limit) + func(upper_limit))
    for i in range(1, num_intervals):
        result += func(lower_limit + i * h)
    result *= h
    return result

def midpoint_method(func, lower_limit, upper_limit, num_intervals):
    h = (upper_limit - lower_limit) / num_intervals
    result = 0
    for i in range(num_intervals):
        x_midpoint = lower_limit + (i + 0.5) * h
        result += func(x_midpoint)
    result *= h
    return result

def simpson_one_third_method(func, lower_limit, upper_limit, num_intervals):
    h = (upper_limit - lower_limit) / num_intervals
    result = func(lower_limit) + func(upper_limit)
    for i in range(1, num_intervals, 2):
        result += 4 * func(lower_limit + i * h)
    for i in range(2, num_intervals - 1, 2):
        result += 2 * func(lower_limit + i * h)
    result *= h / 3
    return result

# User input
equation = input("Masukkan persamaan: ")
lower_bound = float(input("Masukkan batas bawah: "))
upper_bound = float(input("Masukkan batas atas: "))
num_intervals = int(input("Masukkan jumlah subinterval: "))

# Define the function based on the entered equation
func = lambda x: eval(equation, globals(), {'np': np, 'x': x})

# Calculate the integral using the trapezoidal method
result_trapezoidal = trapezoidal_method(func, lower_bound, upper_bound, num_intervals)

# Calculate the integral using the midpoint method
result_midpoint = midpoint_method(func, lower_bound, upper_bound, num_intervals)

# Calculate the integral using Simpson's 1/3 method
result_simpson = simpson_one_third_method(func, lower_bound, upper_bound, num_intervals)

# Display the results
print(f"Hasil integral (Trapesium): {result_trapezoidal}")
print(f"Hasil integral (Titik tengah): {result_midpoint}")
print(f"Hasil integral (Simpson 1/3): {result_simpson}")
