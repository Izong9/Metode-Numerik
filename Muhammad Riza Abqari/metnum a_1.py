import numpy as np #panggil library
def my_bisection(f, a, b, e, i): #mendeklarasikan fungsi bagi dua
  if i > 0:#menentukan apakah jumlah iterasi yang diinginkan sudah tercapai atau belum
    i = i - 1
    if np.sign(f(a)) == np.sign(f(b)):#menentukan apakah persamaan fungsi dari kedua interval bernilai a*b=-ab
      raise Exception('Tidak ada akar pada interval a dan b')#memberhentikan program apabila interval tersebut tidak mengandung akar
    c = (a + b)/2#mencari bilangan c dimana bilangan tersebut akan menjadi interval selanjutnya
    if np.abs(f(c)) < e:#mengeluarkan hasil persamaan apabila hasil persamaan c sudah bernilai lebih kecil dari nilai hampiran yang dicari
      return c
    elif np.sign(f(a)) == np.sign(f(c)):#untuk menentukan apakah nilai c akan menggantikan nilai a atau b pada iterasi selanjutnya
      return my_bisection(f, c, b, e, i)
    elif np.sign(f(b)) == np.sign(f(c)):
      return my_bisection(f, a, c, e, i)
  else:
    c = (a + b)/2
    return c 

f = lambda x: x**3-(2*x)+1#fungsi a. f(x) = x^3 - 2x + 1

I = int(input("Masukan iterasi : "))#menginput batas iterasi yang akan dihitung

print("Pada iterasi ke",I,":")
r1 = my_bisection(f, -2, 2, 0.1, I)#memanggil fungsi bagi dua untuk mencari akar dengan interval (-2,2) dan nilai hampiran 0,1
print("r1 =", r1)
print("f(r1) =", f(r1))

r01 = my_bisection(f, -2, 2, 0.01, I)#memanggil fungsi bagi dua untuk mencari akar dengan interval (-2,2) dan nilai hampiran 0,01
print("r01 =", r01)
print("f(r01) =", f(r01))