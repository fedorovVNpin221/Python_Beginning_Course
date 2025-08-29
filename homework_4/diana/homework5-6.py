def print_number_ladder(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end = " ")
        print()
try:
    user_number = int(input("Введите число -> "))  
    if user_number <= 0:
        print('Пожалуйста, введите положительное число!')
    else:
        print_number_ladder(user_number)
except ValueError:
    print("Ошибка. Введите число -> ") 

def generate_multiplication_table(k):
    for i in range(1,20):
        for j in range(1,20):
            if (i * j) % k == 0:
                print("--",end = " ")
            else:
                print(i * j,end = " ")
        print()
if __name__ == "__main__":
    try:
        k = int(input("Введите число -> "))
        generate_multiplication_table(k)
    except ValueError:
        print("Ошибка. Введите число -> ")

def is_prime(num):
    """
    Проверяет, является ли число простым.

    Args:
        num: Целое число для проверки.

    Returns:
        True, если число простое, False в противном случае.
    """
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_primes_up_to_n(n):
    if n <= 1:
        print("Введите число больше 1.")
        return
    for num in range(2, n + 1):
        if is_prime(num):
            print(num)
if __name__ == "__main__":
    while True:
        try:
            n = int(input("Введите целое число n (n > 1) -> "))
            if n > 1:
                break
            else:
                print("Пожалуйста, введите число больше 1.")
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите целое число.")
    print_primes_up_to_n(n)

def find_min_of_minima(lists_of_lists):
    minimum = []
    for sublist in lists_of_lists:
        if sublist:
            minimum.append(min(sublist))
    if minimum:
        return min(minimum)
    else:
        return None
x = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [-1, 0, 1]]
result1 = find_min_of_minima(x)
print(f"Минимальное число среди минимальных значений: {result1}")
y = [[10, 20, 30], [40, 50, 60]]
result2 = find_min_of_minima(y)
print(f"Минимальное число среди минимальных значений: {result2}")
z = []
result3 = find_min_of_minima(z)
print(f"Минимальное число среди минимальных значений: {result3}")

import random 
import string  
def generate_password(L): 
    characters = string.ascii_letters + string.digits  
    password = ''.join(random.choice(characters) for _ in range(L)) 
    return password 
L = int(input("Введите длину пароля -> ")) 
password = generate_password(L) 
print("Сгенерированный пароль -> ", password) 

def sublist():
    matrica = [
        [1,2,3,4,5,6,7,8,9,4,5,6,1,22,5],
        [-1,-2,-3,-4,-5,-8,7,1,2,3,12,23,5,30,94],
        [6,7,8,9,10,1,2,5,4,6,7,8,9,3,9],
        [-6,-7,-8,-9,-5,8,9,7,66,55,4,2,10,-98,4],
        [-9,8,-7,2,6,-7,9,-1,5,8,7,9,3,4,2]
    ]
    counter = 0
    for podspiska in matrica:
            soderzhit_otricatelnoe = False
            for chislo in podspiska:
                if chislo < 0:
                    soderzhit_otricatelnoe = True
                    break 
            if soderzhit_otricatelnoe:
                counter += 1
            print(f"Количество подсписок с отрицательными числами -> {counter}")
def main():
    sublist()
if __name__ == "__main__":
    main()

def count_subscriptions_with_repeats(subscriptions):
    count = 0
    for subscription in subscriptions:
        seen = {}
        has_repeats = False
        for number in subscription:
            if number in seen:
                seen[number] += 1
                if seen[number] > 1:
                    has_repeats = True
            else:
                seen[number] = 1
        if has_repeats:
            count += 1
    return count
subscriptions = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 12, 13, 14, 15],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 11, 13, 14, 15],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 12, 13, 14, 15],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 2],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 3],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 10],
    [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 1],
    [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 16, 27, 28, 29, 30],
]
count = count_subscriptions_with_repeats(subscriptions)
print(f"Количество подписок с повторяющимися числами -> {count}")