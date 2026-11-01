# Задание 1 (List16)
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
print(sum(a))
print(min(a))
print(max(a))


# Задание 2 (List17)
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
print(sorted(a))
print(a)


# Задание 3 (List18)
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
a.sort(reverse=True)
print(a)
print(len(a))


# Задание 4 (List19)
n = int(input())
s = []
for i in range(n):
    s.append(input())
print(sorted(s, key=len))
print(max(s, key=len))


# Задание 5 (List20)
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
sq = [x * x for x in a]
print(sq)
print(sum(sq))


# Задание 6 (List21)
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
pos = [x for x in a if x > 0]
print(pos)
print(len(pos))


# Задание 7 (List22)
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
d = int(input())
mult = [x * d for x in a]
print(mult)
print(len([x for x in a if x == d]))


# Задание 8 (List23)
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
print(sorted(a, key=abs, reverse=True))


# Задание 9 (List24)
n = int(input())
s = []
for i in range(n):
    s.append(input())
print(sorted(s, key=len))
print(max(s, key=len))


# Задание 10 (List25)
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
b = sorted(a, reverse=True)
print(b[1])


# Задание 11 (List26)
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
avg = sum(a) / len(a)
big = [x for x in a if x > avg]
print(big)
print(avg)


# Задание 12 (List27)
n = int(input())
rows = []
for i in range(n):
    x = float(input())
    y = float(input())
    rows.append([x, y])
rows.sort(key=lambda r: r[0], reverse=True)
for r in rows:
    print(r)
print(rows[0])


# Задание 13 (List28)
n = int(input())
s = []
for i in range(n):
    s.append(input())
letter = input()
found = [x for x in s if x[0] == letter]
print(found)


# Задание 14 (List29)
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
k = int(input())
print(sorted(a, reverse=True)[:k])


# Задание 15 (List30)
n = int(input())
s = []
for i in range(n):
    s.append(input())
lengths = [len(x) for x in s]
print(lengths)
print(sum(lengths))
