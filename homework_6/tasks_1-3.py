# Задача №1
# Создать класс Math, имеющий два целочисленных атрибута a и b. Внутри класса 
# реализовать методы сложения, вычитания, умножения и деления. Результат выполнения 
# операций выводить в консоль
class Math():
    a = 0
    b = 0

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def multiplication(self):
        return self.a * self.b
    
    def division(self):
        return self.a / self.b
    
    def addition(self):
        return self.a + self.b
    
    def subtraction(self):
        return self.a - self.b
    
def task1(oper1):
    print(f"Сложение : {oper1.addition()}")
    print(f"Вычитание : {oper1.subtraction()}")
    print(f"Умножение : {oper1.multiplication()}")
    print(f"Деление: {oper1.division()}")

# Задача №2
# Создать файл words.txt, содержащий 100 любых русских или английских слов,
# получить в коде информацию из этого файла и найти только те слова, которые начинаются 
# с согласной буквы и записать их в новый файл new_words.txt. 
# Информацию из нового файла вывести в консоль
def task2(englishWords, filename1, filename2):
    with open(filename1, 'w', encoding='utf-8') as allWords:
        for word in englishWords:
            allWords.write(word + '\n')
    
    with open(filename1, 'r', encoding='utf-8') as allWords:
        wordsFromFile = allWords.read().splitlines()
    
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    
    consonant_words = []
    with open(filename2, 'w', encoding='utf-8') as consWords:
        for word in wordsFromFile:
            if word and word[0] in consonants:
                consWords.write(word + '\n')
                consonant_words.append(word)
    
    print("Слова, начинающиеся с согласной буквы:")
    for word in consonant_words:
        print(word)

# Задача №3
# Реализовать класс "Книга" с атрибутами "Название", "Автор", "Количество страниц", "Дата публикации" 
# Добавить методы для получения и для изменения всех атрибутов 
# + два метода для записи информации о книге в файл и для чтения этой информации из файла
class Book():
    name = ''
    author = ''
    numOfSheets = 0
    date = ''

    def __init__(self, name, author, numOfSheets, date):
        self.name = name
        self.author = author
        self.numOfSheets = numOfSheets
        self.date = date

        print(f"Книга '{self.name}' успешно создана!")
    
    def getAllAttr(self):
        return [self.name, self.author, self.numOfSheets, self.date]
    
    def setAllAttr(self, name, author, numOfSheets, date):
        self.name = name
        self.author = author
        self.numOfSheets = numOfSheets
        self.date = date

        print(f"Книга '{self.name}' успешно изменена!")

def task3(name, author, numOfSheets, date):
    book1 = Book(name, author, numOfSheets, date)
    print(book1.getAllAttr())
    
    book1.setAllAttr("Идиот", "Федор Достоевский", 150, "1886")
    print(book1.getAllAttr())


def main():
    oper1 = Math(11, 34)
    task1(oper1)

    englishWords = [
        "apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew",
        "kiwi", "lemon", "mango", "nectarine", "orange", "papaya", "quince", "raspberry",
        "strawberry", "tangerine", "ugli", "vanilla", "watermelon", "xigua", "yam", "zucchini",
        "cat", "dog", "elephant", "fox", "giraffe", "horse", "iguana", "jaguar", "koala",
        "lion", "monkey", "newt", "owl", "penguin", "quetzal", "rabbit", "snake", "tiger",
        "umbrella", "violin", "whale", "xylophone", "yak", "zebra", "house", "table",
        "chair", "book", "pen", "computer", "keyboard", "mouse", "screen", "phone",
        "car", "bike", "train", "bus", "road", "city", "country", "mountain", "river",
        "ocean", "sky", "sun", "moon", "star", "cloud", "rain", "snow", "wind", "fire",
        "water", "earth", "air", "tree", "flower", "grass", "garden", "park", "school",
        "doctor", "nurse", "teacher", "student", "parent", "child", "friend", "family",
        "love", "hate", "happy", "sad", "big", "small", "tall", "short", "fast", "slow"
    ]
    task2(englishWords, "homework_6/all_words.txt", "homework_6/cons_words.txt")

    name = "Отцы и дети"
    author = "Тургенев"
    numOfSheets = 200
    date = "1800"
    task3(name, author, numOfSheets, date)

if __name__ == "__main__":
    main()