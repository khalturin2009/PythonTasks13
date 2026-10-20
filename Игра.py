# ================================================
# ИГРА «ПОДЗЕМЕЛЬЕ: СОЛЯНЫЕ ШАХТЫ»
# Автор: Халтурин Пётр
# Дата: сентябрь 2026
# ================================================

# --- Заголовок ------------------------------------
title = "СОЛЯНЫЕ ШАХТЫ"
frame = "=" * 19
print(frame)
print(" " + title + " ")
print(frame)
print()

# --- Знакомство с героем --------------------------
print("Как зовут героя?")
hero_name = input()
print(f"Добро пожаловать, {hero_name}!")
print("Ты входишь в шахту. Здесь темно, пахнет солью и капает вода.")
print()

# --- Настройка героя -------------------------------
print("Настройка героя.")
print("Здоровье, сила, ловкость, удача — по одному числу в строке:")
health = int(input())
strength = int(input())
agility = int(input())
luck = int(input())

# --- Расчёт урона ----------------------------------
base_attack = 10
damage = base_attack + strength * 1.5
crit_damage = damage * 2
stamina = (health + luck) // 10

# --- Формуляр героя --------------------------------
print("Характеристики героя:")
print(f"Здоровье: {health}")
print(f"Сила: {strength}")
print(f"Ловкость: {agility}")
print(f"Удача: {luck}")
print()
print(f"Урон героя: {damage:.1f}")
print(f"Критический урон: {crit_damage:.1f}")
print(f"Запас сил: {stamina}")
print()

# --- Главный цикл игры ---------------------------
running = True
actions = 0
while running:
    print("Что делаешь?")
    print("1 - осмотреться")
    print("2 - идти вперёд")
    print("3 - отдохнуть")
    print("4 - прислушаться")
    print("5 - постучать по стене")
    print("6 - тренировка")
    print("0 - выйти из подземелья")

    valid = ("0", "1", "2", "3", "4", "5", "6")
    choice = input()
    while choice not in valid:
        print("Такого пункта нет. Введи номер пункта из меню.")
        choice = input()

    match choice:
        case "1":
            print("Вы осмотрелись. Стены в белых разводах соли, на полу пыль.")
        case "2":
            cost = 2
            if stamina >= cost:
                stamina -= cost
                print("Вы осторожно идёте вперёд. Соль хрустит под ногами.")
            else:
                health -= cost - stamina
                stamina = 0
                print("Сил больше нет — вы идёте на одном упорстве.")
        case "3":
            stamina = stamina + 2
            print("Вы присели отдохнуть. Дыхание выровнялось.")
        case "4":
            print("Вы замерли и прислушались. Где-то капает вода.")
        case "5":
            if stamina >= 1:
                stamina -= 1
                print("Вы постучали по стене. Звук глухой — за ней пустота.")
            else:
                health -= 1
                print("Вы стучите из последних сил — и это стоит вам здоровья.")
        case "6":
            strikes = 6
            total_damage = 0
            crit_count = 0
            print("Вы подходите к глыбе соли, на которой кто-то вырубил мишень.")
            print("Видно, что здесь тренировались до вас.")
            print()
            print(f"Наносите {strikes} ударов.")
            for i in range(1, strikes + 1):
                if i % 3 == 0:
                    hit_damage = crit_damage
                    crit_count += 1
                    print(f"Удар {i}: {hit_damage:.1f} — критический!")
                else:
                    hit_damage = damage
                    print(f"Удар {i}: {hit_damage:.1f}")
                total_damage += hit_damage
            stamina = stamina - 3
            print()
            print(f"Итог: {strikes} ударов, критических ударов: {crit_count}.")
            print(f"Общий урон: {total_damage:.1f}")
            print(f"Средний урон: {total_damage / strikes:.1f}")
        case "0":
            print("Вы поднимаетесь обратно к свету. Шахта остаётся позади.")
            running = False

    if running:
        actions += 1

    if health <= 0:
        print(f"{hero_name} падает без сил. Шахта забирает ещё одного искателя.")
        running = False

    print()
    print(f"Здоровье: {health:5d} Запас сил: {stamina:5d}")

# --- Прощание --------------------------------------
print()
print(frame)
if health <= 0:
    print(f"Ты не дошёл, {hero_name}. Действий совершено: {actions}.")
else:
    print(f"Забег окончен, {hero_name}. Действий совершено: {actions}.")
print(frame)
