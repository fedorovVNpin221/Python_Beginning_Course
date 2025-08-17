# ошибка int float
x = float((input("Введите первое значение -> ")))
y = float((input("Введите второе значение -> ")))

if x < y:
    print("Наименьшее значение: ", x)
elif y < x:
    print("Наименьшее значение: ", y)
else:
    print("Числа равны!")