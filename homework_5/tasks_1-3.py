# Домашнее задание №5
# Разработать 3 отдельных функции, каждая решает свою задачу.
# Все функции должны вызываться из меню в главной функции main(),
# реализованного по аналогии с файлом tasks_1-3.py

# Задача №1
# Разработать программу, которая объединяет два списка, но добавлять элементы из второго списка 
# только если они не встречаются в первом. 
# Вход: два списка
# Выход: один список
def task1(list1, list2):
    list3 = list1.copy()
    
    for item in list2:
        if item not in list1:
            list3.append(item)
    
    return list3

# Задача №2
# Разработать программу, которая создает новый список, где каждый элемент - это сумма 
# соответствующих элементов из двух списков. Если списки разной длины, дополнять меньший список нулями.
# Вход: два списка
# Выход: один список
def task2(list1, list2):
    maxLength = max(len(list1), len(list2))

    if maxLength == len(list1):
        for i in range(maxLength - len(list2)):
            list2.append(0)
    else:
        for i in range(maxLength - len(list1)):
            list1.append(0)

    list3 = []

    if len(list1) == len(list2):
        for i in range(1, len(list1)):
            list3.append(list1[i] + list2[i])

    return list3

# Задача №3
# Разработать программу, которая обрабатывает список данных по следующим правилам:
#    1. Добавить в конец сумму всех чисел (append)
#    2. Добавить первые 3 элемента в начало (extend + срез)
#    3. Удалить каждый второй элемент (del + срезы)
#    4. Удалить все отрицательные числа (remove в цикле)
def task3(list1):
    total = 0

    for item in list1:
        total += item

    list1.append(total)
    print(list1)

    temp = list1[0:2]
    list1.extend(temp)
    print(list1)

    for i in range(len(list1)-1, -1, -2): 
        if i < len(list1): 
            del list1[i]
    print(list1)

    for item in list1:
        if item < 0:
            list1.remove(item)
    print(list1)

def main():
    list1 = [1, 33, 67, 90, [123, 78, 'stroka'], 123]
    list2 = [234, 70, (12, 98, 0), 'symbol', 89, 1, 1, 1]

    list3 = [1, 3, 4, 9, 11, 23, 78]
    list4 = [23, 78, 9, 0, 34, 123, 45, 11, 19, 1]

    list5 = [1, -4, -56, 90, 0, -11, 345]

    while True:
        try:
            choice = int(input("Выберите программу (1-3): "))
            
            if choice == 1:
                print("Программа 'Задача №1'")
                print(task1(list1, list2))
            elif choice == 2:
                print("Программа 'Задача №2'")
                print(task2(list3, list4))
            elif choice == 3:
                print("Программа 'Задача №3'")
                task3(list5)
            else:
                print("Пожалуйста, введите число от 1 до 3")
                
        except ValueError:
            print("Ошибка: пожалуйста, введите целое число от 1 до 3")

if __name__ == "__main__":
    main()