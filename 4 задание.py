# Задание 45
A, B = map(int, input().split())
for i in range(A, B + 1):
    print(i, end=' ')
print()
print(B - A + 1)

# Задание 46
price = float(input())
for i in range(1, 11):
    print(i, price * i)

# Задание 47
price = float(input())
i = 1
while i <= 10:
    kg = i / 10
    print(round(kg, 1), round(price * kg, 2))
    i += 1

# Задание 48
price = float(input())
i = 12
while i <= 20:
    kg = i / 10
    print(round(kg, 1), round(price * kg, 2))
    i += 2

# Задание 49
A, B = map(int, input().split())
prod = 1
for i in range(A, B + 1):
    prod *= i
print(prod)

# Задание 50
A, B = map(int, input().split())
total = 0
for i in range(A, B + 1):
    total += i * i
print(total)

# Задание 51
N = int(input())
total = 0
for i in range(N, 2 * N + 1):
    total += i * i
print(total)

# Задание 52
N = int(input())
prod = 1.0
for i in range(1, N + 1):
    prod *= 1 + i / 10
print(prod)

# Задание 53
N = int(input())
sign = 1
total = 0.0
for i in range(1, N + 1):
    total += sign * (1 + i / 10)
    sign = -sign
print(total)

# Задание 54
A = float(input())
N = int(input())
result = 1.0
for i in range(N):
    result *= A
print(result)
