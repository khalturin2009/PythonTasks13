# ============================================================
# ИГРА «ПОДЗЕМЕЛЬЕ: СОЛЯНЫЕ ШАХТЫ» — этап 7: враги подземелья
# ============================================================

import random

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
while True:
    try:
        health = int(input())
        strength = int(input())
        agility = int(input())
        luck = int(input())
        if health <= 0:
            raise ValueError(f"Здоровье должно быть положительным, а введено {health}")
        if strength < 0 or agility < 0 or luck < 0:
            raise ValueError("Характеристики не могут быть отрицательными")
        if health + luck < 10:
            raise ValueError("Здоровье и удача вместе должны давать хотя бы 10")
        if agility > strength + 5:
            raise ValueError("Ловкость не может превышать силу больше чем на 5")
        break
    except ValueError as e:
        print(f"Ой: {e}. Введите все четыре числа снова:")

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

# --- Враги и журнал --------------------------------
enemies = ["гуль", "скелет", "паук", "летучая мышь"]
log = []

# --- Главный цикл игры с полной защитой -----------
menu_last = 7
outcome = "прерывание"

try:
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
        print("7 - спуститься глубже")
        print("0 - выйти из подземелья")

        while True:
            choice = input()
            try:
                menu_number = int(choice)
            except ValueError:
                print("Такого пункта нет. Введи номер пункта из меню.")
                continue
            if 0 <= menu_number <= menu_last:
                break
            print("Такого пункта нет. Введи номер пункта из меню.")

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
            case "7":
                if not enemies:
                    print("Вы спускаетесь ниже, но подземелье пусто — врагов больше нет.")
                else:
                    print("Вы спускаетесь по ступеням. Из темноты выходит враг!")
                    enemy = random.choice(enemies)
                    enemy_hp = 45
                    round_n = 0
                    hero_strikes = 0
                    print(f"На вас нападает {enemy}!")
                    while enemy_hp > 0 and health > 0:
                        round_n += 1
                        hero_strikes += 1
                        if hero_strikes % 3 == 0:
                            hit_damage = crit_damage
                            print(f"Раунд {round_n}: вы наносите {hit_damage:.1f} — критический удар!")
                        else:
                            hit_damage = damage
                            print(f"Раунд {round_n}: вы наносите {hit_damage:.1f}.")
                        enemy_hp -= hit_damage
                        if enemy_hp <= 0:
                            print(f"{enemy} повержен!")
                            log.append(f"round {round_n}: hero -{hit_damage:.1f}, {enemy} -0")
                            break
                        print(f"Здоровье {enemy}: {enemy_hp:.1f}.")
                        enemy_damage = random.randint(2, 6)
                        health -= enemy_damage
                        log.append(f"round {round_n}: hero -{hit_damage:.1f}, {enemy} -{enemy_damage}")
                        print(f"{enemy} бьёт в ответ на {enemy_damage}. Ваше здоровье: {health}.")
                    if enemy_hp <= 0:
                        enemies.remove(enemy)
                        print(f"{enemy} побеждён! В подземелье осталось врагов: {len(enemies)}.")
                    print(f"Бой: {round_n} раундов.")
                    print(f"Последняя запись журнала: {log[-1]}")
            case "0":
                print("Вы поднимаетесь обратно к свету. Шахта остаётся позади.")
                outcome = "выход"
                running = False

        if running:
            actions += 1

        if health <= 0:
            print(f"{hero_name} падает без сил. Шахта забирает ещё одного искателя.")
            outcome = "гибель"
            running = False

        print()
        print(f"Здоровье: {health:5d} Запас сил: {stamina:5d} Врагов осталось: {len(enemies)}")

except KeyboardInterrupt:
    print()
    print("Игрок прервал сеанс.")

finally:
    print()
    print(frame)
    if outcome == "гибель":
        print(f"Ты не дошёл, {hero_name}. Действий совершено: {actions}.")
    elif outcome == "выход":
        print(f"Забег окончен, {hero_name}. Действий совершено: {actions}.")
    else:
        print(f"Сеанс прерван, {hero_name}. Действий совершено: {actions}.")
    print(frame)
