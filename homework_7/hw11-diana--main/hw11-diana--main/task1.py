import sys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self,x,y_list):
        super().__init__()
        self.setWindowTitle("Задача №1. Построение графиков функций")
        self.resize(500,500)

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        layout = QVBoxLayout(centralWidget)

        self.figure = Figure(figsize = (5,4), dpi = (100))
        self.canvas = FigureCanvas(self.figure)

        layout.addWidget(self.canvas)

        self.create_plot(x,y_list)

    def create_plot(self,x,y_list):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        count = 0

        for item in y_list:
            count += 1
            ax.plot(x,item,label = f"Функция {count}")

        ax.set_xlabel("Ось 0x")
        ax.set_ylabel("Ось 0y")

        ax.set_title("График №1")
        ax.legend()
        ax.grid(True)

        ax.relim()
        ax.autoscale_view()

        self.canvas.draw()

def main():
    x = [1,2,7,3,5]
    y1 = [2,10,6,8,4]
    y2 = [9,3,5,7,1]
    y3 = [1,5,9,13,17]
    y_list = [y1,y2,y3]

    app = QApplication(sys.argv)
    window1 = MainWindow(x,y_list)
    window1.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()