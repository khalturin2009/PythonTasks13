# Задание 1 (Err1)
try:
    number = int(input())
    print(number)
except ValueError:
    print("Ошибка ввода")


# Задание 2 (Err2)
try:
    a = int(input())
    b = int(input())
    print(f"{a / b:.1f}")
except ZeroDivisionError:
    print("Делить на ноль нельзя")


# Задание 3 (Err3)
try:
    a = int(input())
    b = int(input())
    print(a / b)
except ValueError:
    print("Ошибка ввода")
except ZeroDivisionError:
    print("Делить на ноль нельзя")


# Задание 4 (Err4)
try:
    n = int(input())
    result = 100 / n
except ValueError:
    print("Ошибка ввода")
except ZeroDivisionError:
    print("Делить на ноль нельзя")
else:
    print(result)
finally:
    print("Вычисление завершено")


# Задание 5 (Err5)
word = input()
index = int(input())
try:
    print(word[index])
except IndexError:
    print("Нет такого символа")


# Задание 6 (Err6)
word = input()
try:
    index = int(input())
    print(word[index])
except ValueError:
    print("Ошибка ввода")
except IndexError:
    print("Нет такого символа")


# Задание 7 (Err7)
while True:
    try:
        number = int(input())
        break
    except ValueError:
        print("Это не число. Попробуй ещё:")
print(number)


# Задание 8 (Err8)
total = 0
skipped = 0
while True:
    line = input()
    if line == "":
        break
    try:
        total += int(line)
    except ValueError:
        skipped += 1
        print("Пропущено: не число")
print(total)
print(skipped)


# Задание 9 (Err9)
try:
    age = int(input())
    if age < 0 or age > 120:
        raise ValueError("Возраст вне допустимого диапазона")
except ValueError as e:
    print(f"Отклонено: {e}")
else:
    print(f"Принято: {age}")


# Задание 10 (Err10)
while True:
    try:
        choice = int(input())
    except ValueError:
        print("Введите число")
        continue
    if 1 <= choice <= 5:
        break
    print("Такого пункта нет")
print(choice)


# Задание 11 (Err11)
try:
    a = int(input())
    b = int(input())
    result = a / b
except (ValueError, ZeroDivisionError):
    print("Посчитать не удалось")
else:
    print(f"{result:.2f}")


# Задание 12 (Err12)
try:
    number = int(input())
except ValueError as e:
    print(e)
    print(type(e))
else:
    print(number)


# Задание 13 (Begin8_protect)
try:
    a = int(input())
    b = int(input())
except ValueError:
    print("Ошибка ввода")
else:
    print((a + b) / 2)


# Задание 14 (If3_protect)
try:
    n = int(input())
except ValueError:
    print("Ошибка ввода")
else:
    if n > 0:
        n += 1
    elif n < 0:
        n -= 2
    else:
        n = 10
    print(n)


# Задание 15 (While11_protect)
try:
    n = int(input())
except ValueError:
    print("Ошибка ввода")
else:
    k = 0
    total = 0
    while total < n:
        k += 1
        total += k
    print(k)
    print(total)