import math

# Задание 16
A, B, C = map(float, input().split())
A, B, C = C, A, B
print(A, B, C)

# Задание 17
A, B, C = map(float, input().split())
A, B, C = B, C, A
print(A, B, C)

# Задание 18
x = float(input())
y = 4 * (x - 3)**6 - 7 * (x - 3)**3 + 2
print(y)

# Задание 19
A = float(input())
A2 = A * A
A4 = A2 * A2
A8 = A4 * A4
print(A2, A4, A8)

# Задание 20
A = float(input())
A2 = A * A
A3 = A2 * A
A5 = A3 * A2
A10 = A5 * A5
A15 = A10 * A5
print(A2, A3, A5, A10, A15)

# Задание 21
alpha = float(input())
degrees = alpha * 180 / 3.14
print(degrees)

# Задание 22
TF = float(input())
TC = (TF - 32) * 5 / 9
print(TC)

# Задание 23
TC = float(input())
TF = TC * 9 / 5 + 32
print(TF)

# Задание 24
X, A, Y = map(float, input().split())
price1 = A / X
priceY = price1 * Y
print(price1, priceY)

# Задание 25
X, A, Y, B = map(float, input().split())
price_choc = A / X
price_iris = B / Y
ratio = price_choc / price_iris
print(price_choc, price_iris, ratio)

# Задание 26
V, U, T1, T2 = map(float, input().split())
S = V * T1 + (V - U) * T2
print(S)

# Задание 27
V1, V2, S, T = map(float, input().split())
S_new = S + (V1 + V2) * T
print(S_new)

# Задание 28
M = int(input())
print(M // 1000)

# Задание 29
size = int(input())
print(size // 1024)

# Задание 30
A, B = map(int, input().split())
print(A // B)
