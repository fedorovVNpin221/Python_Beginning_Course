# импортируем все необходимые библиотеки и модули, предварительно их установив
import sys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget

# Задача №1
# Создать простой график с помощью matplotlib и поместить его внутрь окна pyQT5
class MainWindow(QMainWindow):
    # создаем метод-конструктор главного окна
    def __init__(self, x, y_list):
        super().__init__()
        self.setWindowTitle("Задача №1. Построение графиков функций")
        self.resize(900, 700)

        # создание центрального виджета и макета(слоя)
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        layout = QVBoxLayout(centralWidget)

        # создание фигуры и canvas для добавления в виджет
        self.figure = Figure(figsize=(5, 4), dpi=(100))
        self.canvas = FigureCanvas(self.figure)

        # добавляем макет в виджет
        layout.addWidget(self.canvas)

        # вызываем метод для построения графика, который сами написали, 
        # и передаем туда параметры(в данном случае список иксов и список списков игреков)
        self.create_plot(x, y_list)

    # метод для создания графика
    def create_plot(self, x, y_list):
        self.figure.clear()

        ax = self.figure.add_subplot(111)

        count = 0

        # проходимся по списку списков игреков 
        # и для каждого подсписка созадем отдельный график
        for item in y_list:
            count += 1
            ax.plot(x, item, label=f"Функция {count}")

        ax.set_xlabel("Ось ОX")
        ax.set_ylabel("Ось ОY")

        ax.set_title('График №1')
        ax.legend()
        ax.grid(True)

        ax.relim()
        ax.autoscale_view()

        self.canvas.draw()

def main():
    x = [1, 2, 3, 4, 5]
    y1 = [2, 4, 6, 8, 10]
    y2 = [1, 3, 5, 7, 9]
    y3 = [1, 5, 9, 13, 17]
    y_list = [y1, y2, y3]

    # экземпляр класса приложения
    app = QApplication(sys.argv)
    window1 = MainWindow(x, y_list)
    window1.show()
    # ожидание события "закрытие окна"
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()