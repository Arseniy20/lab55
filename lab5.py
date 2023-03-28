def lab1():
    list = [1, 2, 3, 4, 5]
    a = int(input('Введите число: '))
    for x in list:
        if x / a == 1:
            print('Вы угадали число')
            break
        else:
            print('Вы не угадали число')

lab1()


def lab2():
    list = [1, 1, 2, 3, 4, 5, 5, 6]
    print(*filter(lambda x: list.count(x) > 1, list))

lab2()

def lab3():
    nedelya = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']
    day = int(input('Сколько будет выходных на этой неделе? '))
    for x in nedelya:
        print("Рабочие", *nedelya[:-day])
        print("Выходные", *nedelya[:+day])
        break

lab3()


def lab4():
    import random
    com1 = ['Иванов', "Курицын", "Кораблев", "Алиев", "Венжега", "Лебедев", "Аджаров"]
    com2 = ["Абашин", "Скобиола", "Рямин", "Иванов", "Мацаковский", "Самедов", "Товмасян"]
    com3 = tuple[random.sample(com1, 3) + random.sample(com2, 3)]
    print('Первая группа', *com1)
    print('Вторая группа', *com2)
    print('Спортивная команда ', *com3)
    if 'Иванов' in com3:
        print('Фамилия Иванов встречается в списке: ', com3.count('Иванов'))
    else:
        print('НУЖНО БОЛЬШЕ ИВАНОВЫХ, МИЛОРД!!!')
lab4()






























