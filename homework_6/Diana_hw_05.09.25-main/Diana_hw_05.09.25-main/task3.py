class Book:
    title = ""
    author = ""
    number_of_pages = 0
    date_of_publication = ""

    def __init__(self, title1, author1, number_of_pages1, date_of_publication1):
        self.title = title1
        self.author = author1
        self.number_of_pages = number_of_pages1
        self.date_of_publication = date_of_publication1

    # зачем два метода для установки атрибутов
    def setAttr(self, title2, author2, number_of_pages2, date_of_publication2):
        self.title = title2
        self.author = author2
        self.number_of_pages = number_of_pages2
        self.date_of_publication = date_of_publication2

    # def setAttr(self, title3, author3, number_of_pages3, date_of_publication3):
    #     self.title = title3
    #     self.author = author3
    #     self.number_of_pages = number_of_pages3
    #     self.date_of_publication = date_of_publication3

    def getTitle(self):
        return self.title

    def getAuthor(self):
        return self.author

    def getNumber_of_pages(self):
        return self.number_of_pages

    def getDate_of_publication(self):
        return self.date_of_publication

    def printAllInfo(self):
        print(f"Название: {self.title}, \nАвтор: {self.author}, \nКоличество страниц: {self.number_of_pages}, \nДата публикации: {self.date_of_publication}")

    def saveToFile(self, fileBook):
        try:
            with open(fileBook, 'w', encoding = 'utf-8') as file:
                file.write(f"Название: {self.title}\n")
                file.write(f"Автор:{self.author}\n")
                file.write(f"Количество страниц: {self.number_of_pages}\n")
                file.write(f"Дата публикации: {self.date_of_publication}\n")
        finally:
            print(f"Информация успешно сохранена в файл {fileBook}!")

    @staticmethod
    def readFromFile(fileBook):
        try:
            with open(fileBook, 'r', encoding='utf-8') as file:
                fileData = file.read()
                return fileData
        except FileNotFoundError:
            return f"Файл {fileBook} не найден!"
        
        
# создаем функцию main ВНЕ класса Book
def main():
    book1 = Book('Идиот', 'Федор Достоевский', '150', '25.08.1868')
    print(book1.getAuthor())
    print(book1.getDate_of_publication())
    book1.printAllInfo()

    book1.saveToFile('homework_6/Diana_hw_05.09.25-main/Diana_hw_05.09.25-main/book1.txt')

    file_content = book1.readFromFile('homework_6/Diana_hw_05.09.25-main/Diana_hw_05.09.25-main/book1.txt')
    print("\nСодержимое файла:")
    print(file_content)

if __name__ == "__main__":
    main()