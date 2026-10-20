# Задание 1 (While1)
a = int(input())
b = int(input())
free = a
while free >= b:
    free -= b
print(free)

# Задание 2 (While2)
a = int(input())
b = int(input())
count = 0
rest = a
while rest >= b:
    rest -= b
    count += 1
print(count)

# Задание 3 (While3)
n = int(input())
k = int(input())
quotient = 0
rest = n
while rest >= k:
    rest -= k
    quotient += 1
print(quotient)
print(rest)

# Задание 4 (While4)
n = int(input())
rest = n
while rest % 3 == 0:
    rest //= 3
print(rest == 1)

# Задание 5 (While5)
n = int(input())
k = 0
while n > 1:
    n //= 2
    k += 1
print(k)

# Задание 6 (While6)
n = int(input())
product = 1.0
while n >= 2:
    product *= n
    n -= 2
if n == 1:
    product *= 1
print(product)

# Задание 7 (While7)
n = int(input())
k = 0
while k * k <= n:
    k += 1
print(k)

# Задание 8 (While8)
n = int(input())
k = 0
while (k + 1) * (k + 1) <= n:
    k += 1
print(k)

# Задание 9 (While9)
n = int(input())
power = 1
k = 0
while power <= n:
    power *= 3
    k += 1
print(k)

# Задание 10 (While10)
n = int(input())
power = 1
k = 0
while power * 3 < n:
    power *= 3
    k += 1
print(k)

# Задание 11 (While11)
n = int(input())
total = 0
k = 0
while total < n:
    k += 1
    total += k
print(k)
print(total)

# Задание 12 (While12)
n = int(input())
total = 0
k = 0
while total + (k + 1) <= n:
    k += 1
    total += k
print(k)
print(total)

# Задание 13 (While13)
a = float(input())
total = 0.0
k = 0
while total <= a:
    k += 1
    total += 1 / k
print(k)
print(total)

# Задание 14 (While14)
a = float(input())
total = 0.0
k = 0
while total + 1 / (k + 1) < a:
    k += 1
    total += 1 / k
print(k)
print(total)

# Задание 15 (While15)
p = float(input())
deposit = 1000.0
months = 0
while deposit <= 1100:
    deposit = deposit * (1 + p / 100)
    months += 1
print(months)
print(deposit)
