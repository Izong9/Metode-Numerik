import numpy as np #panggil library
import math as mat
def my_bisection(f, a, b, e): #mendeklarasikan fungsi bagi dua
  if np.sign(f(a)) == np.sign(f(b)):#menentukan apakah jumlah iterasi yang diinginkan sudah tercapai atau belum
    raise Exception('Tidak ada akar pada interval a dan b')#memberhentikan program apabila interval tersebut tidak mengandung akar
  m = (a + b)/2#mencari bilangan c dimana bilangan tersebut akan menjadi interval selanjutnya
  if np.abs(f(m)) < e:#mengeluarkan hasil persamaan apabila hasil persamaan c sudah bernilai lebih kecil dari nilai hampiran yang dicari
    return m
  elif np.sign(f(a)) == np.sign(f(m)):#untuk menentukan apakah nilai c akan menggantikan nilai a atau b pada iterasi selanjutnya
    return my_bisection(f, m, b, e)
  elif np.sign(f(b)) == np.sign(f(m)):
    return my_bisection(f, a, m, e)

E = mat.exp(1)

f = lambda x: E**x-x

r1 = my_bisection(f, -1, 0, 0.1)#memanggil fungsi bagi dua untuk mencari akar dengan interval (-1,0) dan nilai hampiran 0,1
print("r1 =", r1)
print("f(r1) =", f(r1))

r01 = my_bisection(f, -1, 0, 0.01)#memanggil fungsi bagi dua untuk mencari akar dengan interval (-1,0) dan nilai hampiran 0,1
print("r01 =", r01)
print("f(r01) =", f(r01))

#hasil tidak memiliki interval yang mengandung akar karena hasil fungsi tidak melewati y=0
