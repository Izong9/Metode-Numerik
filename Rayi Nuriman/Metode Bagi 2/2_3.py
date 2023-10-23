import math
import numpy as np
import matplotlib.pyplot as plt

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

x = np.linspace(a, b, 400)
y = [f(xi) for xi in x]
iterasi_x = [a, b] + iterasi

plt.plot(x, y, label=f'f(x) = {persamaan}')
plt.axhline(0, color='red', linestyle='--', linewidth=0.7, label='y = 0')
plt.scatter(iterasi_x, [f(xi) for xi in iterasi_x], color='green', label='Iterasi', zorder=5)
plt.annotate(f'Akar hampiran: {akar_hampiran:.6f}', (akar_hampiran, f(akar_hampiran)), color='blue')

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Grafik fungsi f(x) dengan Iterasi Metode Biseksi')
plt.grid(True)
plt.legend()

plt.show()
