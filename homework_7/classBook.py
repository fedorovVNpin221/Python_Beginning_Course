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