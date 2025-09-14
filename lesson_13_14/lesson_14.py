# Задача №1 
# Написать класс для управления библиотекой и дочерние классы 
# для работы с различными объектами(книги, диски, журналы)
class Library():
    def __init__(self, title, author, item_id):
        self.title = title
        self.author = author
        self.item_id = item_id
        self.status = False

    def setAttr(self, status):
        self.status = status

    def getAllAttr(self):
        return list(self.title, self.author, self.item_id)


class Book(Library):
    def __init__(self, title, author, item_id, num_of_sheets):
        super().__init__(title, author, item_id)
        self.num_of_sheets = num_of_sheets

    def getAllAttr(self):
        return super().getAllAttr().append(self.num_of_sheets)
    
    def printAllInfo(self):
        print(f"Вся информация о книге: {self.title}, {self.author}, {self.item_id}, {self.num_of_sheets}, {self.status}")

    def getTimeToRead(self):
        return self.num_of_sheets / 30


class Disk(Library):
    def __init__(self, title, author, item_id, time):
        super().__init__(title, author, item_id)
        self.time = time

    def getAllAttr(self):
        return super().getAllAttr().append(self.time)
    
    def printAllInfo(self):
        print(f"Вся информация о диске: {self.title}, {self.author}, {self.item_id}, {self.time}, {self.status}")

    def getTimeToWatchInSeconds(self):
        return self.time * 60


class Magazine(Library):
    def __init__(self, title, author, item_id, articles_count):
        super().__init__(title, author, item_id)
        self.articles_count = articles_count

    def getAllAttr(self):
        return super().getAllAttr().append(self.articles_count)
    
    def printAllInfo(self):
        print(f"Вся информация о журнале: {self.title}, {self.author}, {self.item_id}, {self.articles_count}, {self.status}")

    def getTimeToRead(self, num_of_sheets_1_article):
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