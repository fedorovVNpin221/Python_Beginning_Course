import random

# Задача №1
# Написать игру "Угадай число" с подсказками.
# Пользователь вводит числа, пока не угадает загаданное. 
# Если число больше, подсказка - "Число больше!"
# Если число меньше, подсказка - "Число меньше!"
def func1():
    secret_number = random.randint(1, 50)
    guess = None
    attempts = 0

    while (guess != secret_number):
        guess = int(input("Введите загаднное число -> "))
        attempts += 1

        if (attempts > 5):
            break

        if (guess < secret_number):
            print("Загаданное число больше!")
        elif (guess > secret_number):
            print("Загаданное число меньше!")
        else:
            print(f"Вы отгадали число за {attempts} попыток")
            print(f"Загаданное число -> {secret_number}")
            break

# Задача №2
# Написать игру "Камень, ножницы, бумага"
def func2():
    list = ['камень', 'ножницы', 'бумага']

    while True:
        user_choice = input("Выберите камень, ножницы, бумага -> ")

        if (user_choice == "q"):
            print("Выход.")
            break

        comp_choice = random.choice(list)

        if (user_choice == comp_choice):
            print("Ничья")
        elif (user_choice == 'бумага' and comp_choice == 'камень') or \
            (user_choice == 'камень' and comp_choice == 'ножницы') or \
            (user_choice == 'ножницы' and comp_choice == 'бумага'):
            print("Вы выиграли!")
        else:
            print("Вы проиграли") 

def main():
    func1()
    func2()

if __name__ == "__main__":
    main()