# Задание 1 (Proc1)
def power_a3(a):
    return a ** 3

for i in range(5):
    a = float(input())
    print(power_a3(a))


# Задание 2 (Proc2)
def power_a234(a):
    return a ** 2, a ** 3, a ** 4

for i in range(5):
    a = float(input())
    p2, p3, p4 = power_a234(a)
    print(p2)
    print(p3)
    print(p4)


# Задание 3 (Proc3)
import math

def mean(x, y):
    amean = (x + y) / 2
    gmean = math.sqrt(x * y)
    return amean, gmean

a = float(input())
b = float(input())
c = float(input())
d = float(input())

am, gm = mean(a, b)
print(am)
print(gm)

am, gm = mean(a, c)
print(am)
print(gm)

am, gm = mean(a, d)
print(am)
print(gm)


# Задание 4 (Proc4)
def triangle_ps(a):
    p = 3 * a
    s = a * a * math.sqrt(3) / 4
    return p, s

for i in range(3):
    a = float(input())
    p, s = triangle_ps(a)
    print(p)
    print(s)


# Задание 5 (Proc5)
def rect_ps(x1, y1, x2, y2):
    w = abs(x2 - x1)
    h = abs(y2 - y1)
    p = 2 * (w + h)
    s = w * h
    return p, s

for i in range(3):
    x1 = float(input())
    y1 = float(input())
    x2 = float(input())
    y2 = float(input())
    p, s = rect_ps(x1, y1, x2, y2)
    print(p)
    print(s)


# Задание 6 (Proc6)
def digit_count_sum(k):
    count = 0
    total = 0
    while k > 0:
        total += k % 10
        count += 1
        k //= 10
    return count, total

for i in range(5):
    k = int(input())
    c, s = digit_count_sum(k)
    print(c)
    print(s)


# Задание 7 (Proc7)
def invert_digits(k):
    rev = 0
    while k > 0:
        rev = rev * 10 + k % 10
        k //= 10
    return rev

for i in range(5):
    k = int(input())
    print(invert_digits(k))


# Задание 8 (Proc8)
def add_right_digit(d, k):
    return k * 10 + d

k = int(input())
d1 = int(input())
d2 = int(input())
k = add_right_digit(d1, k)
print(k)
k = add_right_digit(d2, k)
print(k)


# Задание 9 (Proc9)
def digit_count(k):
    count = 0
    while k > 0:
        count += 1
        k //= 10
    return count

def add_left_digit(d, k):
    return d * 10 ** digit_count(k) + k

k = int(input())
d1 = int(input())
d2 = int(input())
k = add_left_digit(d1, k)
print(k)
k = add_left_digit(d2, k)
print(k)


# Задание 10 (Proc10)
def swap(x, y):
    return y, x

a = float(input())
b = float(input())
c = float(input())
d = float(input())

a, b = swap(a, b)
c, d = swap(c, d)
b, c = swap(b, c)

print(a)
print(b)
print(c)
print(d)


# Задание 11 (Proc11)
def minmax(x, y):
    if x < y:
        return x, y
    return y, x

a = float(input())
b = float(input())
c = float(input())
d = float(input())

lo1, hi1 = minmax(a, b)
lo2, hi2 = minmax(c, d)
lo, _ = minmax(lo1, lo2)
_, hi = minmax(hi1, hi2)
print(lo)
print(hi)


# Задание 12 (Proc12)
def sort_inc3(a, b, c):
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if a > b:
        a, b = b, a
    return a, b, c

a1 = float(input())
b1 = float(input())
c1 = float(input())
a2 = float(input())
b2 = float(input())
c2 = float(input())
print(sort_inc3(a1, b1, c1))
print(sort_inc3(a2, b2, c2))


# Задание 13 (Proc13)
def sort_dec3(a, b, c):
    if a < b:
        a, b = b, a
    if b < c:
        b, c = c, b
    if a < b:
        a, b = b, a
    return a, b, c

a1 = float(input())
b1 = float(input())
c1 = float(input())
a2 = float(input())
b2 = float(input())
c2 = float(input())
print(sort_dec3(a1, b1, c1))
print(sort_dec3(a2, b2, c2))


# Задание 14 (Proc14)
def shift_right3(a, b, c):
    return c, a, b

a1 = float(input())
b1 = float(input())
c1 = float(input())
a2 = float(input())
b2 = float(input())
c2 = float(input())
print(shift_right3(a1, b1, c1))
print(shift_right3(a2, b2, c2))


# Задание 15 (Proc15)
def shift_left3(a, b, c):
    return b, c, a

a1 = float(input())
b1 = float(input())
c1 = float(input())
a2 = float(input())
b2 = float(input())
c2 = float(input())
print(shift_left3(a1, b1, c1))
print(shift_left3(a2, b2, c2))