# ============================================================
# ИГРА «ПОДЗЕМЕЛЬЕ: СОЛЯНЫЕ ШАХТЫ» — этап 12: меню понимает команды
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

# --- Потолки и формуляр ----------------------------
max_health = health
max_stamina = stamina

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

# --- Состояние забега ------------------------------
enemies = ["гуль", "скелет", "паук", "летучая мышь"]
enemy_stats = {
    "скелет": {"hp": 45, "damage": 6, "loot": 25},
    "гуль": {"hp": 30, "damage": 4, "loot": 15},
    "паук": {"hp": 20, "damage": 3, "loot": 10},
    "летучая мышь": {"hp": 12, "damage": 2, "loot": 5},
}
prices = {"зелье": 10, "масло": 15, "эликсир": 40}
inventory = {}
log = []
gold_total = 0
ability_bonus = 0

# --- Команды и меню --------------------------------
num_to_verb = {
    "1": "look", "2": "go", "3": "rest", "4": "listen",
    "5": "torch", "6": "train", "7": "descend", "8": "leaders",
    "9": "shop", "10": "backpack", "11": "drink", "0": "exit",
}
commands = ["look", "go", "rest", "listen", "torch", "train", "descend",
            "leaders", "shop", "backpack", "drink potion",
            "buy <item> [count]", "exit"]
MENU = [
    "Что делаешь? (номер или команда; help — справка)",
    "1 - осмотреться (look)",
    "2 - идти вперёд (go)",
    "3 - отдохнуть (rest)",
    "4 - прислушаться (listen)",
    "5 - постучать по стене (torch)",
    "6 - тренировка (train)",
    "7 - спуститься глубже (descend)",
    "8 - таблица лидеров (leaders)",
    "9 - магазин (shop)",
    "10 - рюкзак (backpack)",
    "11 - выпить зелье (drink)",
    "0 - выйти из подземелья (exit)",
]


# --- Функции правил и боя --------------------------

def hero_hit(strike_n):
    """Урон героя в удар номер strike_n.
    Возвращает пару (hit, crit): урон и признак критического удара.
    Читает глобальные правила damage и crit_damage, не меняет ничего.
    """
    if strike_n % 3 == 0:
        return crit_damage, True
    return damage, False


def fight(enemy, hero_health, bonus=0):
    """Бой с enemy до гибели одного из двоих.
    Карточка врага берётся из enemy_stats по имени: нужны ключи
    hp, damage, loot. bonus — надбавка к урону героя (по умолчанию 0),
    прибавляется после расчёта крита. Печатает строки раундов.
    Возвращает (rounds, won, hero_health, loot).
    """
    stats = enemy_stats[enemy]
    enemy_hp = float(stats["hp"])
    rounds = []
    round_n = 0
    print(f"Вы спускаетесь по ступеням. Из темноты выходит {enemy}!")
    while enemy_hp > 0 and hero_health > 0:
        round_n += 1
        hit, crit = hero_hit(round_n)
        hit = hit + bonus
        enemy_hp -= hit
        line = f"Раунд {round_n}: вы наносите {hit:.1f}"
        if crit:
            line += " — критический удар!"
        if enemy_hp <= 0:
            line += " Враг падает."
            rounds.append([round_n, hit, 0])
        else:
            blow = stats["damage"]
            hero_health -= blow
            line += f" Здоровье {enemy}: {enemy_hp:.1f}. {enemy} бьёт в ответ на {blow}."
            rounds.append([round_n, hit, blow])
        print(line)
    won = enemy_hp <= 0
    loot = stats["loot"] if won else 0
    return rounds, won, hero_health, loot


def buy(price, gold, quantity=1):
    """Покупает quantity штук товара ценой price за золото gold.
    quantity по умолчанию 1. Возвращает (gold_left, ok).
    Ничего не печатает.
    """
    cost = price * quantity
    if gold >= cost:
        return gold - cost, True
    return gold, False


def print_leaderboard(log):
    """Печатает топ-3 раундов по урону героя и рекорд врага."""
    if not log:
        print("Вы ещё не сражались.")
        return
    top = sorted(log, key=lambda r: r[1], reverse=True)[:3]
    print("Таблица лидеров (урон героя):")
    for i in range(len(top)):
        print(f"{i + 1}. Раунд {top[i][0]}: {top[i][1]:.1f}")
    worst = max(log, key=lambda r: r[2])
    print(f"Самый сильный удар врага: {worst[2]} (раунд {worst[0]}).")


def print_run_summary(log):
    """Печатает итог забега: суммарный и средний урон героя."""
    total = sum(r[1] for r in log)
    rounds = len(log)
    if rounds > 0:
        print(f"Урон: {total:.1f} за {rounds} раундов, в среднем {total / rounds:.1f}.")
    else:
        print("В этом забеге не было боёв.")


# --- Главный цикл игры ----------------------------
outcome = "прерывание"

try:
    running = True
    actions = 0
    while running:
        print("\n".join(MENU))
        print()

        line = input()
        cmd = line.strip().lower()
        while cmd == "":
            print("Пустая команда. Введи команду или номер.")
            line = input()
            cmd = line.strip().lower()
        words = cmd.split()
        verb = words[0]
        if cmd in num_to_verb:
            verb = num_to_verb[cmd]

        match verb:
            case "look":
                print("Вы осмотрелись. Стены в белых разводах соли, на полу пыль.")
            case "go":
                cost = 2
                if stamina >= cost:
                    stamina -= cost
                    print("Вы осторожно идёте вперёд. Соль хрустит под ногами.")
                else:
                    health -= cost - stamina
                    stamina = 0
                    print("Сил больше нет — вы идёте на одном упорстве.")
            case "rest":
                stamina = stamina + 2
                print("Вы присели отдохнуть. Дыхание выровнялось.")
            case "listen":
                print("Вы замерли и прислушались. Где-то капает вода.")
            case "torch":
                if stamina >= 1:
                    stamina -= 1
                    print("Вы постучали по стене. Звук глухой — за ней пустота.")
                else:
                    health -= 1
                    print("Вы стучите из последних сил — и это стоит вам здоровья.")
            case "train":
                strikes = 6
                total_damage = 0
                crit_count = 0
                print("Вы подходите к глыбе соли, на которой кто-то вырубил мишень.")
                print("Видно, что здесь тренировались до вас.")
                print()
                print(f"Наносите {strikes} ударов.")
                for i in range(1, strikes + 1):
                    hit_damage, crit = hero_hit(i)
                    if crit:
                        crit_count += 1
                        print(f"Удар {i}: {hit_damage:.1f} — критический!")
                    else:
                        print(f"Удар {i}: {hit_damage:.1f}")
                    total_damage += hit_damage
                stamina = stamina - 3
                print()
                print(f"Итог: {strikes} ударов, критических ударов: {crit_count}.")
                print(f"Общий урон: {total_damage:.1f}")
                print(f"Средний урон: {total_damage / strikes:.1f}")
            case "descend":
                if not enemies:
                    print("Вы спускаетесь ниже, но подземелье пусто — врагов больше нет.")
                else:
                    enemy = random.choice(enemies)
                    rounds, won, health, loot = fight(enemy, health, bonus=ability_bonus)
                    for r in rounds:
                        log.append(r)
                    if won:
                        gold_total += loot
                        enemies.remove(enemy)
                        print(f"{enemy} побеждён! В подземелье осталось врагов: {len(enemies)}. Добыча: {loot} золота.")
                    print(f"Бой: {len(rounds)} раундов.")
            case "leaders":
                print_leaderboard(log)
            case "shop":
                print("Магазин:")
                for name, price in prices.items():
                    print(f"{name}: {price} золота")
            case "backpack":
                if not inventory:
                    print("Рюкзак пуст.")
                else:
                    print("Рюкзак:")
                    for name, qty in inventory.items():
                        print(f"{name}: {qty} шт.")
            case "buy":
                if len(words) > 1 and words[-1].isdigit():
                    qty = int(words[-1])
                    item = " ".join(words[1:-1])
                else:
                    qty = 1
                    item = " ".join(words[1:])
                if item == "":
                    print("Купить что? Введи: buy <предмет>.")
                    continue
                if item not in prices:
                    print("Такого предмета в магазине нет.")
                    continue
                gold_total, ok = buy(prices[item], gold_total, quantity=qty)
                if ok:
                    inventory[item] = inventory.get(item, 0) + qty
                    if item == "зелье":
                        health = min(health + 10 * qty, max_health)
                    elif item == "масло":
                        stamina = min(stamina + 5 * qty, max_stamina)
                    else:
                        ability_bonus += 2 * qty
                    print(f"Куплено {qty} {item} за {prices[item] * qty} золота. Остаток золота: {gold_total}.")
                else:
                    print(f"Не хватает золота: нужно {prices[item] * qty}, есть {gold_total}.")
            case "drink":
                item = " ".join(words[1:]) or "зелье"
                if inventory.get(item, 0) == 0:
                    print(f"В рюкзаке нет: {item}.")
                else:
                    health = min(health + 10, max_health)
                    inventory[item] -= 1
                    if inventory[item] == 0:
                        del inventory[item]
                    print(f"Вы выпили {item}. Здоровье: {health}. Осталось: {inventory.get(item, 0)}.")
            case "help":
                print("Команды: " + ", ".join(commands) + ".")
                print("Номера 0-11 работают как раньше.")
            case "exit":
                print("Вы поднимаетесь обратно к свету. Шахта остаётся позади.")
                outcome = "выход"
                running = False
            case _:
                print(f"Не понимаю команду: '{line.strip()}'. Введи 'help'.")
                continue

        actions += 1

        if health <= 0:
            print(f"{hero_name} падает без сил. Шахта забирает ещё одного искателя.")
            outcome = "гибель"
            running = False

        print()
        print(f"Здоровье: {health:5d} Запас сил: {stamina:5d} Врагов осталось: {len(enemies)} Золото: {gold_total}")

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
    if inventory:
        print("В рюкзаке осталось:")
        for name, qty in inventory.items():
            print(f"{name}: {qty} шт.")
    else:
        print("В рюкзаке ничего не осталось.")
    print_run_summary(log)
    print(frame)
