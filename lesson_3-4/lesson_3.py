# Задча №1 
# Пользователь вводит число, обозначающее текущее время.
# Нужно определить, какое время суток в данный момент.
def func1():
    time = int(input("Который час? "))

    if (time >= 6 and time < 12):
        print("Утро!")
    elif (time >= 12 and time < 18):
        print("День!")
    elif (time >= 18 and time < 24):
        print("Вечер!")
    else:
        print("Ночь!")

# Задача №2
# Пользователь вводит произвольное число,
# нужно определить, число больше 100 или меньше
def func2():
    num = int(input("Введите произвольное число -> "))
    num1 = 100
    num2 = 50

    if (num > 100):
        print(f"Число {num} больше {num1}!")
    elif (num < 100 and num > 50):
        print(f"Число {num} меньше {num1}, но больше {num2}!")
    elif (num == 100 or num == 50):
        if (num == 100):
            print(f"Число равно {num1}!")
        else:
            print(f"Число равно {num2}!")
    else:
        print(f"Число {num} меньше {num1}")

def main():
    func1()
    func2()

if __name__ == "__main__":
    main()