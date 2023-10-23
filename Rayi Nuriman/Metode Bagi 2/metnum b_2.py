import math
import numpy as np

def f(x):
    return eval(persamaan, {"x": x})

def bisection(a, b, tlt, n):
    iterasi = []
    for i in range(n):
        c = (a + b) / 2.0
        iterasi.append(c)
        if f(c) == 0.0 or (b - a) / 2.0 < tlt:
            return c, iterasi
        elif f(a) * f(c) < 0.0:
            b = c
        else:
            a = c
    return c, iterasi  # Mengembalikan nilai c, bukan (a + b) / 2.0

persamaan = input("Masukkan persamaan fungsi : ")
persamaan = persamaan.replace("e", "math.e")

a = float(input("Masukkan batas bawah interval (a): "))
b = float(input("Masukkan batas atas interval (b): "))
teliti = float(input("Masukkan ketelitian (3 angka dibelakang koma): "))
n = int(input("Masukkan jumlah maksimum iterasi: "))

akar_hampiran, iterasi = bisection(a, b, teliti, n)

print(f'Akar hampiran: {akar_hampiran:.6f}')
print(f'Nilai f(x) pada akar: {f(akar_hampiran):.6f}')
print(f'Jumlah iterasi: {len(iterasi)}')
print('Iterasi: ', iterasi)
