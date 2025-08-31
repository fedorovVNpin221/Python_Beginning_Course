import os

# Задача №1
# Написать функцию, которая открывает заранее созданный .txt файл и выводит 
# всю информацию из него на экран
def task1(fileName):
    # создаем файл с именем. которое записано в переменную fileName 
    # a+ - ключ, означающий добавление новых данных в файл без его перезаписи
    with open(fileName, 'a+', encoding='utf-8') as file1:
        # четрые раза подряд записываем одну и ту же строку в файл
        for i in range(1, 5):
            file1.write("Новая строка! \n")

        # возвращаем "каретку" к 0 байт, чтобы прочитать файл с самого начала
        file1.seek(0) 

        # читаем данные из файла и выводим на экран
        print(file1.read()) 

        # обрезаем файл до 0 байт
        file1.truncate(0)

        print(file1.read())

# Задача №2
# Написать функцию, которая создает новый файл и записывает туда результаты 
# выполнения арифметических операций
# функция принимает 4 аргумента на вход
def task2(a, b, operation, fileName):
    # w+ позволяет создавать файл, если его нет и записывать туда информацию
    with open(fileName, 'w+', encoding='utf-8') as file2:
        if operation == '+':
            file2.write(f"Результат операции {a} {operation} {b}: {a + b}")
        elif operation == '-':
            file2.write(f"Результат операции {a} {operation} {b}: {a - b}")
        elif operation == '*':
            file2.write(f"Результат операции {a} {operation} {b}: {a * b}")
        elif operation == '/':
            file2.write(f"Результат операции {a} {operation} {b}: {a / b}")
        else:
            print("Введена некорретная операция!")

    # открываем файл с ключом для чтения и выводим инфу из файла
    with open(fileName, 'r', encoding='utf-8') as file2:
        print(file2.read())

def main():
    # передаем путь к файлу внутри рабочего каталога
    task1('lesson_9-10/task1.txt')

    a = float(input("Введите число 1 -> "))
    b = float(input("Введите число 2 -> "))
    operation = input("Введите операцию (+, -, *, /) -> ")

    # получаем список всех директорий в рабочем каталоге
    catalogList = os.listdir()
    print(catalogList)

    # ищем конкретную папку в списке всех каталогов
    for item in catalogList:
        if item == 'lesson_7-8':
            path = item

    # добавляем к найденной папке путь к новому файлу
    path = path + '/math.txt'

    # передаем в функцию все необходимые аргументы
    task2(a, b, operation, path)

if __name__ == "__main__":
    main()