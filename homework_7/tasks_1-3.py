import sys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTableWidget, 
                             QTableWidgetItem, QVBoxLayout, QWidget, QHeaderView)
from PyQt5.QtCore import Qt
from .classBook import Book


# Задача №1
# Взять любую линейную функцию и построить график её изменения с помощью 
# matplotlib и PyQT5 по аналогии с кодом урока №11
# импортируем все необходимые библиотеки и модули, предварительно их установив
class MainWindow(QMainWindow):
    def __init__(self, x, y):
        super().__init__()
        self.setWindowTitle("Задача №1. Построение графиков функций")
        self.resize(900, 700)

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        layout = QVBoxLayout(centralWidget)

        self.figure = Figure(figsize=(5, 4), dpi=(100))
        self.canvas = FigureCanvas(self.figure)

        layout.addWidget(self.canvas)

        self.create_plot(x, y)

    def create_plot(self, x, y):
        self.figure.clear()

        ax = self.figure.add_subplot(111)

        ax.plot(x, y, label=f"Функция y = x + 5x")

        ax.set_xlabel("Ось ОX")
        ax.set_ylabel("Ось ОY")

        ax.set_title('График №1')
        ax.legend()
        ax.grid(True)

        ax.relim()
        ax.autoscale_view()

        self.canvas.draw()


# Рассматривается функция вида y = x + 5x
def task1(x):
    y = []
    
    for item in x:
        func = item + 5 * item
        y.append(func)

    app = QApplication(sys.argv)
    window1 = MainWindow(x, y)
    window1.show()
    sys.exit(app.exec_())


# Задача №2 
# Создать окно в PyQt5, которое выводит информацию об одном экземпляре(объекте)
# класса из ДЗ№6(класс "Книга"), для этого подключить файл с классом "Книга" к файлу 
# с текущим ДЗ
class Library(QMainWindow):
    def __init__(self, booksList):
        super().__init__()
        self.setWindowTitle("Задача №2. Библиотека")
        self.setGeometry(100, 100, 1200, 800)
        
        self.initUI(booksList)

    def initUI(self, booksList):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)
        
        self.table = QTableWidget()
        self.table.setRowCount(len(booksList))
        self.table.setColumnCount(4)
        
        headers = ["Название", "Автор", "Кол-во страниц", "Год издания"]
        self.table.setHorizontalHeaderLabels(headers)
        
        for row, book in enumerate(booksList):
            name_item = QTableWidgetItem(book.name)
            author_item = QTableWidgetItem(book.author)
            sheets_item = QTableWidgetItem(str(book.numOfSheets))
            date_item = QTableWidgetItem(str(book.date))
            
            name_item.setTextAlignment(Qt.AlignCenter)
            author_item.setTextAlignment(Qt.AlignCenter)
            sheets_item.setTextAlignment(Qt.AlignCenter)
            date_item.setTextAlignment(Qt.AlignCenter)
            
            self.table.setItem(row, 0, name_item)
            self.table.setItem(row, 1, author_item)
            self.table.setItem(row, 2, sheets_item)
            self.table.setItem(row, 3, date_item)
        
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)

        main_layout.addWidget(self.table)


def createBooks(booksDict):
    booksList = []

    for key, value in booksDict.items():
        for item in value:
            if len(item) == 3:
                name = item[0]
                numOfSheets = item[1]
                year = item[2]

                book = Book(name, key, numOfSheets, year)
                booksList.append(book)
            else:
                continue
        
    return booksList


def task2(booksDict):
    booksList = createBooks(booksDict)

    for item in booksList:
        print(item.getAllAttr())

    app = QApplication(sys.argv)
    library = Library(booksList)
    library.show()
    sys.exit(app.exec_())


# Задача №3
# Распределить все файлы в текущем проекте по папкам и подпапкам 
# и скопировать все полученные папки и файлы в новую рабочую папку
# Эту задачу сделать обязательно, т.к. на следующем занятии нам пригодится 
# этот новый каталог проекта
def main():
    x = [1, 2, 3, 6, 12, 24, 48]
    
    booksDict = {
    'Федор Достоевский': [
        ['Идиот', 500, 1868],
        ['Преступление и наказание', 672, 1866],
        ['Братья Карамазовы', 824, 1880]
    ],
    'Иван Тургенев': [
        ['Отцы и дети', 288, 1862],
        ['Записки охотника', 352, 1852],
    ],
    'Александр Пушкин': [
        ['Евгений Онегин', 224, 1833],
        ['Руслан и Людмила', 192, 1820],
        ['Капитанская дочка', 192, 1836]
    ],
    'Чак Паланик': [
        ['Бойцовский клуб', 224, 1996],
    ],
    'Дж. Р. Р. Толкин': [
        ['Сильмаррилион', 432, 1954],
        ['Хоббит, из огня да вполымя', 352, 1954],
        ['Хоббит, или Туда и обратно', 320, 1937]
    ],
    'Осип Мандельштам': [
        ['Стихи о неизвестном солдате', 96, 1913],
        ['Век-Волкодав', 112, 1922],
        ['Стихотворения', 256, 1928]
    ],
    'Михаил Булгаков': [
        ['Мастер и Маргарита', 384, 1940],
        ['Собачье сердце', 192, 1925],
        ['Белая гвардия', 352, 1925]
    ],
    'Лев Толстой': [
        ['Война и мир', 1225, 1869],
        ['Анна Каренина', 864, 1877],
    ]
    }

    while True:
        try:
            choice = int(input("Выберите программу (1-2): "))
            
            if choice == 1:
                print("Программа 'Задача №1. График линейной функции'")
                print(task1(x))
            elif choice == 2:
                print("Программа 'Задача №2. Библиотека")
                print(task2(booksDict))
            else:
                print("Пожалуйста, введите число от 1 до 2")
                
        except ValueError:
            print("Ошибка: пожалуйста, введите целое число от 1 до 2")

if __name__ == "__main__":
    main()