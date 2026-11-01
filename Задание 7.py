# Задание 1 (List1)
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
print(len(a))
print(a[0])


# Задание 2 (List2)
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
k = int(input())
print(a[k])
print(a[-1])
print(k)


# Задание 3 (List3)
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
s = 0
p = 1
for x in a:
    s = s + x
for i in range(0, len(a), 2):
    p = p * a[i]
print(s)
print(p)


# Задание 4 (List4)
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
imax = 0
for i in range(len(a)):
    if a[i] > a[imax]:
        imax = i
print(imax)
print(a[imax])


# Задание 5 (List5)
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
d = int(input())
a.append(d)
print(a)
print(len(a))


# Задание 6 (List6)
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
k1 = int(input())
k2 = int(input())
b = a[k1:k2 + 1]
print(b)
s = 0
for x in b:
    s = s + x
print(s)


# Задание 7 (List7)
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
print(a[::-1])
print(a)


# Задание 8 (List8)
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
d = int(input())
if d in a:
    a.remove(d)
print(a)
print(len(a))


# Задание 9 (List9)
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
s = 0
for x in a:
    s = s + x
avg = s / len(a)
count = 0
for x in a:
    if x > avg:
        print(x)
        count = count + 1
print(count)


# Задание 10 (List10)
n = int(input())
a = []
for i in range(n):
    a.append(input())
imax = 0
imin = 0
for i in range(len(a)):
    if len(a[i]) > len(a[imax]):
        imax = i
    if len(a[i]) < len(a[imin]):
        imin = i
print(a[imax])
print(len(a[imax]))
print(a[imin])
print(len(a[imin]))


# Задание 11 (List11)
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
k = 0
for i in range(len(a)):
    if a[i] < 0:
        a[i] = 0
        k = k + 1
print(a)
print(k)


# Задание 12 (List12)
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
k = int(input())
a.insert(k, 0)
print(a)
print(len(a))


# Задание 13 (List13)
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
x = a.pop()
print(x)
print(a)


# Задание 14 (List14)
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
d = int(input())
print(a.count(d))
if d in a:
    print(a.index(d))
else:
    print(-1)


# Задание 15 (List15)
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
s = 0
for i in range(1, len(a), 2):
    print(a[i])
    s = s + a[i]
print(s)
