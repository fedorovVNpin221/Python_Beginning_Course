# Задача №1
# Создать класс Student с атрибутами имя, номер, возраст 
# и реализовать 5 методов:
# - для получения имени, номера и возраста
# - для изменения имени и возраста

# создаем класс Student
class Student:
    name = "" # поля или атрибуты класса (его статические характеристики)
    number = ""
    age = 0

    # метод-конструктор для создания объекта класса 
    # и выдачи его атрибутам(полям) значений
    def __init__(self, NAME, NUMBER, AGE): # self - ссылка на текущий объект класса
        self.name = NAME
        self.number = NUMBER
        self.age = AGE

    # метод для установки атрибутам объекта класса новых значений
    def setAttr(self, newName, newNumber, newAge):
        self.name = newName
        self.number = newNumber
        self.age = newAge

    # методы для получения значений атрибутов объекта класса
    def getName(self):
        return self.name
    
    def getNumber(self):
        return self.number
    
    def getAge(self):
        return self.age
    
    # метод для вывода значений всех атрибутов объекта класса в консоль
    def printAllInfo(self):
        print(f"Имя : {self.name},\nНомер : {self.number},\nВозраст : {self.age}")

    # метод для сохранения данных объекта класса в файл
    def saveToFile(self, fileName):
        try:
            with open(fileName, 'w', encoding='utf-8') as file:
                file.write(f"Имя : {self.name}\n")
                file.write(f"Номер : {self.number}\n")
                file.write(f"Возраст : {self.age}\n")
        finally:
            print(f"Информация успешно сохранена в файл {fileName}!")

    # сатический метод для чтения и получения всех данных из файла
    @staticmethod
    def readFromFile(fileName):
        try:
            with open(fileName, 'r', encoding='utf-8') as file:
                fileData = file.read()
                return fileData
        except FileNotFoundError:
            return f"Файл {fileName} не найден!"
        
def task1():
    # создаем экземпляр класса(объект) и задаем значения его полям
    Object1 = Student("Ivan", 123, 18)
    Object1.printAllInfo()
    print()

    # изменяем значения всех атрибутов объекта
    Object1.setAttr("Олег", 400, 20)
    Object1.printAllInfo()
    print()

    Object2 = Student("Sveta", 890, 12)
    Object2.printAllInfo()
    print()

    Object2.setAttr("Елена", 0, 30)
    Object2.printAllInfo()
    print()

# Задача №2
# Реализовать методы в классе Student для записи и чтения информации о студенте из файла
def task2():
    # создаем новый экземпляр класса
    Object1 = Student("Николай", 11, 40)
    # сохраняем все данные об объекте в файл
    Object1.saveToFile("lesson_9-10/student_info.txt")

    # читаем всю инфу об объекте из файла
    print(Object1.readFromFile("lesson_9-10/student_info.txt"))

def main():
    task1()
    task2()

if __name__ == "__main__":
    main()