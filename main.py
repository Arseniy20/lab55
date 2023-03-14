import random import randit
n = 2

kusko = []

for i in range(n):
    kusko.append(input())
    word = ' '.join(kusko)

print(word)

def lab31():
    kusko = []
    while (new_word := str(input())) != "stop":
        kusko.append(new_word)

    print(" ".join(kusko))


lab31()

def lab32():
    kusko = []
    while (new_word := str(input())) != "stop":
        if "ф" in new_word or "Ф" in new_word:
            print("Это редкое слово!")
        else:
            print("Это не редкое слово!")

lab32()


def lab33():
    on = 0
    op = 0
    while on < 3:
        n1 = randint(1, 100)
        n2 = randint(1, 100)
        print(f"{n1} + {n2} = ", end="")
        otv = input()
        if not otv.isdigit() and otv != "stop":
            print("Некорректный ввод, повторите попытку!")
            otv = input()
            if (n1 + n2) != int(otv):
                print("Ответ неверный:(")
                on += 1
            if (n1 + n2) == int(otv):
                print("Правильно!")
                op += 1
            if on >= 3:
                print("Игра окончена. Правильных ответов: ", op)
        elif otv == "stop":
            print("Игра завершена.")
        else:
            if (n1 + n2) != int(otv):
                print("Ответ неверный:(")
                on += 1
            if (n1 + n2) == int(otv):
                print("Правильно!")
                op += 1
            if on >= 3:
                print("Игра окончена. Правильных ответов: ", op)



lab33()

