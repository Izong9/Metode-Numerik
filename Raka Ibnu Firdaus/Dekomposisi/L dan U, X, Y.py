def decompose_SPL(matrix, n, b):
    L = [[0 for _ in range(n)] for _ in range(n)]
    U = [[0 for _ in range(n)] for _ in range(n)]
    y = [0 for _ in range(n)]
    x = [0 for _ in range(n)]
    
    # Step 2: Mencari matriks L dan U
    for j in range(n):
        for i in range(n):
            p1 = 0
            for k in range(i):
                p1 += L[i][k] * U[k][j]
            if i <= j:
                U[i][j] = matrix[i][j] - p1
                if i == j:
                    L[i][j] = 1
            else:
                L[i][j] = (matrix[i][j] - p1) / U[j][j]
    
    # Memastikan determinan matriks A tidak sama dengan 0
    if det(matrix, n) == 0:
        print("Determinan matriks A sama dengan 0. Sistem tidak memiliki solusi unik.")
        return None, None, None, None
    
    # Step 3: Mencari nilai y
    for i in range(n):
        p = 0
        for k in range(i):
            p += L[i][k] * y[k]
        y[i] = b[i] - p
    
    # Step 4: Mencari nilai x
    x[n-1] = y[n-1] / U[n-1][n-1]
    for i in range(n-2, -1, -1):
        p = 0
        for k in range(i+1, n):
            p += U[i][k] * x[k]
        x[i] = (y[i] - p) / U[i][i]
    
    return L, U, y, x

def det(matrix, n):
    # Fungsi untuk menghitung determinan matriks
    pass

# Input dari pengguna
n = int(input("Masukkan ukuran matriks (n): "))
matrix = []
print("Masukkan elemen-elemen matriks A:")
for i in range(n):
    row = list(map(float, input().split()))
    matrix.append(row)

b = list(map(float, input("Masukkan elemen vektor b: ").split()))

L, U, y, x = decompose_SPL(matrix, n, b)

if L is not None and U is not None:
    print("Matriks L:")
    for i in range(n):
        print(L[i])

    print("Matriks U:")
    for i in range(n):
        print(U[i])
    
    print("Nilai y:")
    print(y)
    
    print("Nilai x:")
    print(x)
