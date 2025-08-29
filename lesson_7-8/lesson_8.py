import random

# Задача №1
# Разработать программу, которая находит одинаковые значения в двух двумерных матрицах
def task1(matrix1, matrix2):
    currentNum = 0
    result = []

    for sublist1 in matrix1:
        for item1 in sublist1:
            currentNum = item1

            for sublist2 in matrix2:
                for item2 in sublist2:
                    if currentNum == item2:
                        result.append(currentNum)
                    else:
                        continue
    return result

# Задача №2
# Разработать программу, которая принимает на вход два списка, 
# а возвращает общий список, где элементы расположены поочередно
def task2(letters, N):
    numbers = []
    result = []

    for i in range(1, 10):
        numbers.append(random.randint(1, 9))

    for i in range(1, N + 1):
        result.append(str(random.choice(letters)) + str(random.choice(numbers)))

    return result

def main():
    matrix1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8 ,9]
    ]
    matrix2 = [
        [1, 2, 3, 11],
        [4, 5, 6, 78],
        [7, 8 ,9, 90],
        [12, 45, 78, 0]
    ]

    print(task1(matrix1, matrix2))

    letters = ['a', 'b', 'c', 'd', 'e']

    N = int(input("Введите длину пароля -> "))
    print(task2(letters, N))

if __name__ == "__main__":
    main()