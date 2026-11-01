# Задание 1 (Proc16)
def sign(x):
    if x < 0:
        return -1
    if x == 0:
        return 0
    return 1


a = float(input())
b = float(input())
print(sign(a) + sign(b))


# Задание 2 (Proc17)
def roots_count(a, b, c):
    d = b * b - 4 * a * c
    if abs(d) < 1e-9:
        return 1
    if d > 0:
        return 2
    return 0


for i in range(3):
    a = float(input())
    b = float(input())
    c = float(input())
    print(roots_count(a, b, c))


# Задание 3 (Proc18)
def circle_s(r):
    return 3.14 * r * r


for i in range(3):
    r = float(input())
    print(circle_s(r))


# Задание 4 (Proc19)
def circle_s(r):
    return 3.14 * r * r


def ring_s(r1, r2):
    return circle_s(r1) - circle_s(r2)


for i in range(3):
    r1 = float(input())
    r2 = float(input())
    print(ring_s(r1, r2))


# Задание 5 (Proc20)
import math


def triangle_p(a, h):
    b = math.sqrt((a / 2) ** 2 + h * h)
    return a + 2 * b


for i in range(3):
    a = float(input())
    h = float(input())
    print(triangle_p(a, h))


# Задание 6 (Proc21)
def sum_range(a, b):
    if a > b:
        return 0
    total = 0
    for x in range(a, b + 1):
        total += x
    return total


a = int(input())
b = int(input())
c = int(input())
print(sum_range(a, b))
print(sum_range(b, c))


# Задание 7 (Proc22)
def calc(a, b, op):
    if op == 1:
        return a - b
    if op == 2:
        return a * b
    if op == 3:
        return a / b
    return a + b


a = float(input())
b = float(input())
n1 = int(input())
n2 = int(input())
n3 = int(input())
print(calc(a, b, n1))
print(calc(a, b, n2))
print(calc(a, b, n3))


# Задание 8 (Proc23)
def quarter(x, y):
    if x > 0 and y > 0:
        return 1
    if x < 0 and y > 0:
        return 2
    if x < 0 and y < 0:
        return 3
    return 4


for i in range(3):
    x = float(input())
    y = float(input())
    print(quarter(x, y))


# Задание 9 (Proc24)
def even(k):
    return k % 2 == 0


count = 0
for i in range(10):
    k = int(input())
    if even(k):
        count += 1
print(count)


# Задание 10 (Proc25)
def is_square(k):
    if k <= 0:
        return False
    r = int(k ** 0.5)
    return r * r == k or (r + 1) * (r + 1) == k


count = 0
for i in range(10):
    k = int(input())
    if is_square(k):
        count += 1
print(count)


# Задание 11 (Proc26)
def is_power5(k):
    if k <= 0:
        return False
    while k % 5 == 0:
        k //= 5
    return k == 1


count = 0
for i in range(10):
    k = int(input())
    if is_power5(k):
        count += 1
print(count)


# Задание 12 (Proc27)
def is_power_n(k, n):
    if k <= 0:
        return False
    while k % n == 0:
        k //= n
    return k == 1


n = int(input())
count = 0
for i in range(10):
    k = int(input())
    if is_power_n(k, n):
        count += 1
print(count)


# Задание 13 (Proc28)
def is_prime(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


count = 0
for i in range(10):
    k = int(input())
    if is_prime(k):
        count += 1
print(count)


# Задание 14 (Proc29)
def digit_count(k):
    count = 0
    while k > 0:
        count += 1
        k //= 10
    return count


for i in range(5):
    k = int(input())
    print(digit_count(k))


# Задание 15 (Proc30)
def digit_n(k, n):
    pos = 1
    cur = k
    while cur > 0:
        if pos == n:
            return cur % 10
        cur //= 10
        pos += 1
    return -1


for i in range(5):
    k = int(input())
    for n in range(1, 6):
        print(digit_n(k, n))
