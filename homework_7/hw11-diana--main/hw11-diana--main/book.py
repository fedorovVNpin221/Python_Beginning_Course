class Book:
    title = ''
    author = ''
    year = 0

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def getTitle(self):
        return self.title

    def getAuthor(self):
        return self.author

    def getYear(self):
        return self.year

    def printAllInfo(self):
        print(f"Название: {self.title}, \nАвтор: {self.author}, \nГод: {self.year}")