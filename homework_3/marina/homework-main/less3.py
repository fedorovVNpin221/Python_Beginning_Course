num1 = int(input("1 число -> "))
num2 = int(input("2 число -> "))

operation = input("введите операцию ->")

# нет цикличности и выхода из программы

if operation == '+':
    print(num1 + num2)
elif operation == '-':
    print(num1 - num2)
elif operation == '/':
    print(num1 / num2)
elif operation == '*':
    print(num1 * num2)
else:
    print('Неизвестная операция')