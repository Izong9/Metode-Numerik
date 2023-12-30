import numpy as np

def forward_difference_derivative(func, x, h):
    derivative = (func(x + h) - func(x)) / h
    return derivative

def backward_difference_derivative(func, x, h):
    derivative = (func(x) - func(x - h)) / h
    return derivative

def central_difference_derivative(func, x, h):
    derivative = (func(x + h) - func(x - h)) / (2 * h)
    return derivative

function_input = input("Masukkan fungsi: ")
function = lambda x: eval(function_input)

x_values_input = input("Masukkan nilai x: ")
x_values = np.array([float(x) for x in x_values_input.split(',')])

h_value = float(input("Masukkan jarak dari nilai x (h): "))

forward_derivative_array = np.vectorize(lambda x: forward_difference_derivative(function, x, h_value))(x_values[:-1])
backward_derivative_array = np.vectorize(lambda x: backward_difference_derivative(function, x, h_value))(x_values[1:])
central_derivative_array = np.vectorize(lambda x: central_difference_derivative(function, x, h_value))(x_values[1:-1])

print(f"\nFungsi: {function_input}")
print(f"Nilai x: {x_values}")
print(f"Nilai h: {h_value}")
print("\nTurunan pertama (Maju):", forward_derivative_array)
print("Turunan pertama (Mundur):", backward_derivative_array)
print("Turunan pertama (Tengah):", central_derivative_array)
