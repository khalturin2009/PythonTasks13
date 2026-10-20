# Задание 31
A = int(input())
print(A % 2 != 0)

# Задание 32
A = int(input())
print(A % 2 == 0)

# Задание 33
A, B = map(int, input().split())
print(A > 2 and B <= 3)

# Задание 34
A, B = map(int, input().split())
print(A >= 0 or B < -2)

# Задание 35
A, B, C = map(int, input().split())
print((B > A and B < C) or (B > C and B < A))

# Задание 36
A, B = map(int, input().split())
print(A % 2 != 0 and B % 2 != 0)

# Задание 37
A, B = map(int, input().split())
print(A % 2 != 0 or B % 2 != 0)

# Задание 38
A, B = map(int, input().split())
print((A % 2 != 0) != (B % 2 != 0))

# Задание 39
A, B = map(int, input().split())
print(A % 2 == B % 2)

# Задание 40
A, B, C = map(int, input().split())
print(A > 0 or B > 0 or C > 0)

# Задание 41
A = int(input())
if A > 0:
    A += 1
print(A)

# Задание 42
A = int(input())
if A > 0:
    A += 1
else:
    A -= 2
print(A)

# Задание 43
A, B, C = map(int, input().split())
count = 0
if A > 0:
    count += 1
if B > 0:
    count += 1
if C > 0:
    count += 1
print(count)

# Задание 44
A, B, C = map(int, input().split())
pos = 0
neg = 0
if A > 0:
    pos += 1
elif A < 0:
    neg += 1
if B > 0:
    pos += 1
elif B < 0:
    neg += 1
if C > 0:
    pos += 1
elif C < 0:
    neg += 1
print(pos, neg)
