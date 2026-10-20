import math

# Задание 1
a, b, c = map(float, input().split())
V = a * b * c
S = 2 * (a * b + b * c + a * c)
print(V, S)

# Задание 2
R = float(input())
L = 2 * 3.14 * R
S = 3.14 * R * R
print(L, S)

# Задание 3
a, b = map(float, input().split())
print((a + b) / 2)

# Задание 4
a, b = map(float, input().split())
print(math.sqrt(a * b))

# Задание 5
a, b = map(float, input().split())
print(a*a + b*b, a*a - b*b, a*a * b*b, (a*a) / (b*b))

# Задание 6
a, b = map(float, input().split())
print(abs(a) + abs(b), abs(a) - abs(b), abs(a) * abs(b), abs(a) / abs(b))

# Задание 7
a, b = map(float, input().split())
c = math.sqrt(a*a + b*b)
P = a + b + c
print(c, P)

# Задание 8
R1, R2 = map(float, input().split())
S1 = 3.14 * R1 * R1
S2 = 3.14 * R2 * R2
S3 = S1 - S2
print(S1, S2, S3)

# Задание 9
L = float(input())
R = L / (2 * 3.14)
S = 3.14 * R * R
print(R, S)

# Задание 10
S = float(input())
R = math.sqrt(S / 3.14)
D = 2 * R
L = 2 * 3.14 * R
print(D, L)

# Задание 11
x1, x2 = map(float, input().split())
print(abs(x2 - x1))

# Задание 12
A, B, C = map(float, input().split())
AC = abs(C - A)
BC = abs(C - B)
print(AC, BC, AC + BC)

# Задание 13
A, B, C = map(float, input().split())
AC = abs(C - A)
BC = abs(C - B)
print(AC * BC)

# Задание 14
x1, y1, x2, y2 = map(float, input().split())
w = abs(x2 - x1)
h = abs(y2 - y1)
P = 2 * (w + h)
S = w * h
print(P, S)

# Задание 15
x1, y1, x2, y2 = map(float, input().split())
print(math.sqrt((x2 - x1)**2 + (y2 - y1)**2))