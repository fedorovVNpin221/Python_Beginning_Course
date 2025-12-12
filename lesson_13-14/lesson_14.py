# Задача №1 
# Написать класс для управления библиотекой и дочерние классы 
# для работы с различными объектами(книги, диски, журналы)
class Library(): # родительский класс библиотеки
    # необходим для работы с журналами, книгами и дисками
    def __init__(self, title, author, item_id): # метод-конструктор 
        self.title = title     # Наименование книги
        self.author = author   # ФИО автора
        self.item_id = item_id # ID книги
        self.status = False    # Статус выдачи книги

    def setAttr(self, status): # метод для изменения значения атрибута
        self.status = status

    def getAllAttr(self):  # метод для получения значений всех атрибутов класса
        return list(self.title, self.author, self.item_id)


class Book(Library): # Дочерний класс книги
    # наследует поля родительского класса и имеет свое уникальное поле
    # "количество страниц"
    def __init__(self, title, author, item_id, num_of_sheets): # метод-конструктор с уникальным атрибутом
        super().__init__(title, author, item_id)
        self.num_of_sheets = num_of_sheets

    def getAllAttr(self): # метод для получения значений всех атрибутов класса
        return super().getAllAttr().append(self.num_of_sheets)
    
    def printAllInfo(self): # метод для вывода значений всех атрибутов класса в консоль
        print(f"Вся информация о книге: {self.title}, {self.author}, {self.item_id}, {self.num_of_sheets}, {self.status}")

    def getTimeToRead(self): # метод для получения времени прочтения книги
        return self.num_of_sheets / 30


class Disk(Library): # Дочерний класс диска
    # наследует поля родительского класса библиотеки и имеет свое уникальное поле
    # "хронометраж"
    def __init__(self, title, author, item_id, time): # метод-конструктор с уникальным атрибутом
        super().__init__(title, author, item_id)
        self.time = time

    def getAllAttr(self): # метод для получения значений всех атрибутов класса
        return super().getAllAttr().append(self.time)
    
    def printAllInfo(self): # метод для вывода значений всех атрибутов класса в консоль
        print(f"Вся информация о диске: {self.title}, {self.author}, {self.item_id}, {self.time}, {self.status}")

    def getTimeToWatchInSeconds(self): # метод для получения значения уникального атрибута в секундах
        return self.time * 60


class Magazine(Library): # Дочерний класс журнала
    # наследует поля родительского класса библиотеки и имеет свое уникальное поле
    # "количество статей"
    def __init__(self, title, author, item_id, articles_count): # метод-конструктор с уникальным атрибутом
        super().__init__(title, author, item_id)
        self.articles_count = articles_count

    def getAllAttr(self): # метод для получения значений всех атрибутов класса
        return super().getAllAttr().append(self.articles_count)
    
    def printAllInfo(self): # метод для вывода значений всех атрибутов класса в консоль
        print(f"Вся информация о журнале: {self.title}, {self.author}, {self.item_id}, {self.articles_count}, {self.status}")

    def getTimeToRead(self, num_of_sheets_1_article): # метод для получения времени на прочтение одной статьи в журнале
        return (self.articles_count * num_of_sheets_1_article) / 30


def main():
    book1 = Book("1984", "Джордж Оруэлл", "B01", 155)
    disk1 = Disk("Мстители 1", "Руссо", "D01", 205)
    magazine1 = Magazine("Playboy", "Иван Петров", "M01", 12)

    book1.printAllInfo()
    disk1.printAllInfo()
    magazine1.printAllInfo()

    book1.setAttr(True)
    disk1.setAttr(False)
    magazine1.setAttr(True)

    book1.printAllInfo()
    disk1.printAllInfo()
    magazine1.printAllInfo()

    print(f"{book1.getTimeToRead()} часов")
    print(f"{disk1.getTimeToWatchInSeconds()} секунд")
    print(f"{magazine1.getTimeToRead(10)} часов")

if __name__ == "__main__":
    main()