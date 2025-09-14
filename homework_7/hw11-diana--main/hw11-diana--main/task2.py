import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
from book import Book # импорт класса Book из файла book.py

class BookWindow(QMainWindow):
    def __init__(self, book_instance):
        super().__init__()
        self.book = book_instance
        self.setWindowTitle("Задача №2. Класс: книга")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        # виджеты для отображения информации
        self.label_title = QLabel("Название:")
        self.line_edit_title = QLineEdit()
        self.line_edit_title.setText(self.book.title)

        self.label_author = QLabel("Автор:")
        self.line_edit_author = QLineEdit()
        self.line_edit_author.setText(self.book.author)
        self.line_edit_author.setReadOnly(True)

        self.label_year = QLabel("Год:")
        self.line_edit_year = QLineEdit()
        self.line_edit_year.setText(str(self.book.year))
        self.line_edit_year.setReadOnly(True)

        # добавляем виджеты в макет
        self.layout.addWidget(self.label_title)
        self.layout.addWidget(self.line_edit_title)
        self.layout.addWidget(self.label_author)
        self.layout.addWidget(self.line_edit_author)
        self.layout.addWidget(self.label_year)
        self.layout.addWidget(self.line_edit_year)

def main():
    app = QApplication(sys.argv)
    # создаем экземпляр класса Book
    my_book = Book("Мастер и Маргарита", "Михаил Булгаков", "1866")
    # показываем окно с информацией об объекте
    window = BookWindow(my_book)
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()