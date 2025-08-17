def canculator(num1,num2,operation):
    if operation == "+":
        return num1+num2
    elif operation == "*":
        return num1*num2
    elif operation == "/":
        if num2 == 0:
            return "Ошибка: деление на ноль"
        return num1/num2
    # отсутствует операция вычитание
    else:
        return "Ошибка: неверная операция"

def get_user_input():
    num1 = float(input("Введите первое значение -> "))
    num2 = float(input("Введите второе значение -> "))
    operation = input("Введите операцию(+,-,*,/) -> ")
    return num1,num2,operation

def main():
    previous_result = None
    while True:
        if previous_result is None: # используется впервые
            num1,num2,operation = get_user_input()
        else: # последующие вычисления
            # ошибка ветвления
            use_previous = input(f"Использовать предыдущий результат({previous_result})? (y/n) -> ")
            if use_previous.lower() == 'y':
                num1 = previous_result
                num2, _, operation = get_user_input() # функция возвращает три значения
                if num2 is None:
                    print("Ошибка ввода!")
                    continue
            else:
                num1,num2,operation = get_user_input()

        # ошибка обработки операций
        if num1 is None or num2 is None or operation is None:
            print("Ошибка ввода!")
            continue

        result = canculator(num1,num2,operation)
        print("Результат:", result)

        if isinstance(result,float) or isinstance(result,int):
            previous_result = result
        else:
            previous_result = None
        another_canculation = input("Продолжить вычисления? (y/n) -> ")
        if another_canculation.lower() != 'y':
            break

if __name__ == "__main__":
    main()