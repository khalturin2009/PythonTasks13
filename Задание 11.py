# Задание 1 (Dict1)
n = int(input())
d = {}
for i in range(n):
    key = input()
    value = int(input())
    d[key] = value
print(len(d))
for key in d:
    print(key)


# Задание 2 (Dict2)
n = int(input())
d = {}
for i in range(n):
    key = input()
    value = int(input())
    d[key] = value
k = input()
if k in d:
    print(d[k])
else:
    print("нет такого ключа")


# Задание 3 (Dict3)
n = int(input())
d = {}
for i in range(n):
    key = input()
    value = int(input())
    d[key] = value
k = input()
print(d.get(k, 0))


# Задание 4 (Dict4)
n = int(input())
d = {}
for i in range(n):
    key = input()
    value = int(input())
    d[key] = value
k = input()
v = int(input())
if k in d:
    d[k] = d[k] + v
else:
    d[k] = v
print(d[k])


# Задание 5 (Dict5)
n = int(input())
d = {}
for i in range(n):
    key = input()
    value = int(input())
    d[key] = value
k = input()
d.pop(k, None)
print(len(d))


# Задание 6 (Dict6)
n = int(input())
d = {}
for i in range(n):
    key = input()
    value = int(input())
    d[key] = value
total = 0
for value in d.values():
    total = total + value
print(total)


# Задание 7 (Dict7)
n = int(input())
d = {}
for i in range(n):
    key = input()
    value = int(input())
    d[key] = value
best = None
for key in d:
    if best is None or d[key] > d[best]:
        best = key
print(best)


# Задание 8 (Dict8)
n = int(input())
d = {}
for i in range(n):
    key = input()
    value = int(input())
    d[key] = value
v = int(input())
print(v in d.values())


# Задание 9 (Dict9)
n = int(input())
d1 = {}
for i in range(n):
    key = input()
    value = int(input())
    d1[key] = value
m = int(input())
d2 = {}
for i in range(m):
    key = input()
    value = int(input())
    d2[key] = value
d1.update(d2)
print(len(d1))
common = None
for key in d2:
    if key in d1:
        common = key
print(d1[common])


# Задание 10 (Dict10)
n = int(input())
d = {}
for i in range(n):
    key = input()
    value = int(input())
    d[key] = value
for name, price in d.items():
    print(f"{name}: {price}")


# Задание 11 (Dict11)
n = int(input())
counts = {}
for i in range(n):
    word = input()
    counts[word] = counts.get(word, 0) + 1
for word, count in counts.items():
    print(f"{word}: {count}")


# Задание 12 (Dict12)
n = int(input())
d = {}
for i in range(n):
    key = input()
    value = int(input())
    d[key] = value
rev = {}
for key, value in d.items():
    rev[value] = key
for key, value in rev.items():
    print(f"{key}: {value}")


# Задание 13 (Dict13)
n = int(input())
d = {}
for i in range(n):
    name = input()
    price = int(input())
    qty = int(input())
    d[name] = [price, qty]
total = 0
best = None
for name, (price, qty) in d.items():
    cost = price * qty
    total += cost
    if best is None or cost > best:
        best = cost
        best_name = name
print(total)
print(best_name)


# Задание 14 (Dict14)
n = int(input())
d = {}
for i in range(n):
    key = input()
    value = int(input())
    d[key] = value
v = int(input())
for key in list(d):
    if d[key] < v:
        del d[key]
print(len(d))


# Задание 15 (Dict15)
n = int(input())
d1 = {}
for i in range(n):
    key = input()
    value = int(input())
    d1[key] = value
m = int(input())
d2 = {}
for i in range(m):
    key = input()
    value = int(input())
    d2[key] = value
ignored = 0
for key, value in d2.items():
    if key in d1:
        ignored += 1
    else:
        d1[key] = value
print(len(d1))
print(ignored)