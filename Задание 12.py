# Задание 1 (String1)
c = input()
print(ord(c))


# Задание 2 (String2)
n = int(input())
print(chr(n))


# Задание 3 (String3)
c = input()
print(chr(ord(c) - 1))
print(chr(ord(c) + 1))


# Задание 4 (String4)
n = int(input())
print("".join(chr(ord("A") + i) for i in range(n)))


# Задание 5 (String5)
n = int(input())
print("".join(chr(ord("z") - i) for i in range(n)))


# Задание 6 (String6)
c = input()
if "0" <= c <= "9":
    print("digit")
elif "a" <= c <= "z" or "A" <= c <= "Z":
    print("lat")
else:
    print("rus")


# Задание 7 (String7)
s = input()
print(ord(s[0]))
print(ord(s[-1]))


# Задание 8 (String8)
n = int(input())
c = input()
print(c * n)


# Задание 9 (String9)
n = int(input())
c1 = input()
c2 = input()
print("".join(c1 if i % 2 == 0 else c2 for i in range(n)))


# Задание 10 (String10)
s = input()
print(s[::-1])


# Задание 11 (String11)
s = input()
print(" ".join(s))


# Задание 12 (String12)
s = input()
n = int(input())
print(("*" * n).join(s))


# Задание 13 (String13)
s = input()
count = 0
for ch in s:
    if ch.isdigit():
        count += 1
print(count)


# Задание 14 (String14)
s = input()
count = 0
for ch in s:
    if "A" <= ch <= "Z":
        count += 1
print(count)


# Задание 15 (String15)
s = input()
alphabet = "abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
count = 0
for ch in s:
    if ch in alphabet:
        count += 1
print(count)