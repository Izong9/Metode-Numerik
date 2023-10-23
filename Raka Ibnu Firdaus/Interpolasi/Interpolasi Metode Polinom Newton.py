import numpy as np #panggil library

x = []
y = []

n = int(input("Banyak data: ")) #menentukan jumlah data yang akan diinput
xp = float(input("nilai x yang dicari = ")) #menentukan nilai x yang akan dicari 
yp = 0

d = n-1
for i in range(0, n): #menginput nilai x dan y
    nilx = float(input("X%d = " % (i+1)))
    nily = float(input("Y%d = " % (i+1)))
    # adding the element
    x.append(nilx) #menambahkan nilai yang diinput ke array
    y.append(nily) 


Selisih = np.zeros((d+1,d+1))
Selisih[:,0] = y 

for k in range(1, d+1):
  for i in range (0, d-k+1):
    Selisih[i,k] = (Selisih[i+1,k-1] - Selisih[i,k-1])/(x[i+k] - x[i])

yp = Selisih[0,0]

for i in range (1 , d + 1):
  a = Selisih[0,i]

  for j in range(0,i):
    a = a * (xp-x[j])

  yp = yp + a

print("Nilai Y dari X = %f adalah Y = %.3f" %(xp,yp))