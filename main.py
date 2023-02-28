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
    import random
    



lab33()
