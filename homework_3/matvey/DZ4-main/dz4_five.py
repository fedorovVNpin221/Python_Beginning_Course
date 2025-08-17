while True:
    num1 = input("введите первое чило -> ")
    num2 = input("введите второе число  -> ")
    znaki = input("введите что-то из скобочек (+, -, *, /)  -> ")

    if (num1 == 'q'):
        break

    # нет выхода из цикла
    
    if (znaki == "+"):
        print(int(num1) + num2) 
    elif (znaki == "-"):
        print(num1 - num2) 
    elif (znaki == "*"):
        print(num1 * num2)
    elif (znaki == "/"):
        print(num1 / num2)  
    else:
        print("error")