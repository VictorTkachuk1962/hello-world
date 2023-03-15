z = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]

def draw():
    y = []
    y.append(f"- 0 1 2")
    for n in range(3):
        y.append(f"{n} {z[n][0]} {z[n][1]} {z[n][2]}")

    for i in range(4):
        print(y[i])

draw()

def hod(num):
        while True:
            if num == 1:
                a = input(
                "Первый игрок, введите через пробел две цифры от 0 до 2. Первая цифра - это номер строки, вторая цифра - номер столбца: ")
            else:
                a = input(
                "Второй игрок, введите через пробел две цифры от 0 до 2. Первая цифра - это номер строки, вторая цифра - номер столбца: ")

            b = a.split()

            if len(b) != 2:
                print("Ошибка ввода! Читайте инструкцию. Повторите ввод.")
                continue

            if not(b[0].isdigit()) or not(b[1].isdigit()):
                print("Ошибка! Необходимо ввести числа. Повторите ввод.")
                continue

            one = int(b[0])
            two = int(b[1])


            if (not(((one == 0) or (one == 1) or (one == 2)) and ((two == 0) or (two == 1) or (two == 2)))):
                print("Не правильно введены цифры. Повторите ввод.")
                continue

            if z[one][two] == "-":
                if num == 1:
                    z[one][two] = "x"
                else:
                    z[one][two] = "0"
                break
            else:
                print("Поле занято. Повторите ввод.")
        draw()

schet = 0

while True:
    hod(1)
    if ((z[0][0] == "x" and z[0][1] == "x" and z[0][2] == "x") or
        (z[1][0] == "x" and z[1][1] == "x" and z[1][2] == "x") or
        (z[2][0] == "x" and z[2][1] == "x" and z[2][2] == "x") or
        (z[0][0] == "x" and z[1][0] == "x" and z[2][0] == "x") or
        (z[0][1] == "x" and z[1][1] == "x" and z[2][1] == "x") or
        (z[0][2] == "x" and z[1][2] == "x" and z[2][2] == "x") or
        (z[0][0] == "x" and z[1][1] == "x" and z[2][2] == "x") or
        (z[0][2] == "x" and z[1][1] == "x" and z[2][0] == "x")):
            print("Первый игрок выиграл! Игра окончена!")
            break
    schet += 1
    if schet == 9:
        print("Ничья! Игра окончена!")
        break

    hod(2)
    if ((z[0][0] == "0" and z[0][1] == "0" and z[0][2] == "0") or
        (z[1][0] == "0" and z[1][1] == "0" and z[1][2] == "0") or
        (z[2][0] == "0" and z[2][1] == "0" and z[2][2] == "0") or
        (z[0][0] == "0" and z[1][0] == "0" and z[2][0] == "0") or
        (z[0][1] == "0" and z[1][1] == "0" and z[2][1] == "0") or
        (z[0][2] == "0" and z[1][2] == "0" and z[2][2] == "0") or
        (z[0][0] == "0" and z[1][1] == "0" and z[2][2] == "0") or
        (z[0][2] == "0" and z[1][1] == "0" and z[2][0] == "0")):
            print("Второй игрок выиграл! Игра окончена!")
            break
    schet += 1