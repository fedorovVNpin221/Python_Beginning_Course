import random 
import string 
def generate_password(length):                                              # Length-длина, characters-персонажи

    characters = string.ascii_letters + string.digits + string.punctuation   #(строка.ascii_буквы + строка.цифры + строка.знаки препинания)   
    password = ''.join(random.choice(characters) for _ in range(length))     # выбирает один символ из строки characters случайным образом.
    return password
password_length = int(input("Введите желаемую длину пароля: "))
generated_password = generate_password(password_length)
print("Ваш сгенерированный пароль:", generated_password)
