def dataStructExamples():
    # стандартная инициализация
    spisok = [1, 2, 3, 4, 78]
    kortezh = ('1', 2, 4, 89)
    mnozhestvo = {12, 14, 888, 0}

    print(spisok, '\n', kortezh,  '\n', mnozhestvo)
    print(spisok[1])
    print(kortezh[2])
    print(list(mnozhestvo)[3]) # обязательное преобразование в список
    print()

    # инициализация с помощью встроенных функций
    spisok1 = list([1, 2, 3, 4, 990, 0]) 
    kortezh1 = tuple([12, 33, 'stroka', 11]) 
    mnozhestvo1 = set([9876, 345, 4567, 34321, "длинная строка"])  

    print(spisok1, '\n', kortezh1, '\n', mnozhestvo1, '\n')
    print(spisok1[1])
    print(kortezh1[2])
    print(list(mnozhestvo1)[3])
    print()

    # комбинированная инициализация 
    spisok2 = [1, [1, 2, 3, 7], mnozhestvo, spisok1]
    kortezh2 = tuple([34, 17, set([12, 987, *kortezh]), 'symbol'])  # распаковываем кортеж kortezh
    mnozhestvo2 = {1, 'symbol', 123, frozenset([1, 4, 5]), tuple(['1', 23, 18])} # список не может быть элементом множества!

    print(spisok2, '\n', kortezh2, '\n', mnozhestvo2, '\n')
    print(spisok2[1])
    print(kortezh2[2])
    print(list(mnozhestvo2)[3])
    print()

    # словарь
    my_dict = {
        'a': 'z',
        1: 100,
        2: 200,
        3: 300,
        4: "string",
        tuple(spisok): set(['строка', 'слово', 'Python', 1]),  
        991: 11,
        'ключ': 12345
    }

    print(my_dict)
    print(my_dict[4])
    print(my_dict[1])
    print(my_dict[tuple(spisok)])

    # добавление элементов в список с помощью input
    spisok.append(input('введите что-нибудь ->'))
    print(spisok)

    var = input('Введите значение ->')
    my_dict['ключ'] = var
    print(my_dict['ключ'])

def biggerNumber():
    var1 = int(input("Введите первое число -> "))
    var2 = int(input("Введите второе число -> "))

    if (var1 > var2):
        print(f"Число {var1} больше, чем {var2}")
    elif (var2 > var1):
        print(f"Число {var2} больше, чем {var1}")
    else:
        print("Числа равны")

def main():
    dataStructExamples()
    biggerNumber()

if __name__ == "__main__":
    main()