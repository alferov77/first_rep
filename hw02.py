def greet():
    print("-" * 34)
    print("     Приветствуем вас в игре      ")
    print("        'Крестики-нолики'         ")
    print()
    print("Обратите внимание на формат ввода:")
    print("               х у                ")
    print("        x - номер строки          ")
    print("        y - номер столбца         ")
    print("-" * 34)

def show_field():
    print("  Выберите, кто ставит крестики,  ")
    print("       а кто ставит нолики        ")
    print("        Выбрали? Отлично!         ")
    print()
    print("        Итак, первыми ...")
    print()
    print("  ⎮ 0 ⎮ 1 ⎮ 2 ⎮ ")
    print("  ","-" * 11)
    for i, row in enumerate(field):
        row_str = f'{i} ⎮ {' ⎮ '.join(row)} ⎮'
        print(row_str)
        print("  ","-" * 11)

def ask_user():
    while True:
        print()
        coordinates = input('Ваш ход:   ').split()

        if len(coordinates) != 2:
            print(' Пожалуйста, введите два числа от 0 до 2 в качестве координат ')
            continue

        x, y = coordinates

        if not (x.isdigit()) or not(y.isdigit()):
            print(' Вводите только числа! ')
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(' Координаты вне диапазона ')
            continue

        if field[x][y] != " ":
            print(' Клетка занята! ')
            continue

        return x, y

def check_win():
    win_coordinates = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                       ((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)), ((0, 2), (0, 2), (2, 2)),
                       ((0, 0), (1, 1), (2, 2)), ((0, 2), (1, 1), (2, 0)))
    for coordinates in win_coordinates:
        symbols = []
        for c in coordinates:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print ("Выиграли крестики !")
            return True
        if symbols == ["0", "0", "0"]:
            print ("Выиграли нолики !")
            return True
    return False

greet()
field = [[" "] * 3 for i in range(3)]
nums = 0
while True:
    nums += 1
    show_field()
    if nums % 2 == 1:
        print('          ходят крестики ')
    else:
        print('          ходят нолики ')

    x, y = ask_user()

    if nums % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if check_win():
        break

    if nums == 9:
        print(' Ничья ! ')
        break

