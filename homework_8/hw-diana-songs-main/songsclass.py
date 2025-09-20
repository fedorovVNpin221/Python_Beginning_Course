# Импортируем необходимые библиотеки  
import sys  
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QListWidget, QLabel  
  
class AlenaShvets:  
    def __init__(self):  
        self.songs = []  
      
    def add_song(self, song):  
        self.songs.append(song)  
      
    def get_songs(self):  
        return self.songs  
  
class OldSongs(AlenaShvets):  
    def __init__(self):  
        super().__init__()  
        self.add_song("Первое свидание")  
        self.add_song("Союзу не нужен пафос")  
        self.add_song("Одуванчик")  
  
class NewSongs(AlenaShvets):  
    def __init__(self):  
        super().__init__()  
        self.add_song("Marry Me")  
        self.add_song("Нелюбовь")  
        self.add_song("Молодость")  
  
class MainWindow(QMainWindow):  
    def __init__(self):  
        super().__init__()  
          
        self.setWindowTitle("Песни Алёны Швец")  
        self.setGeometry(100, 100, 500, 500)  
          
        self.central_widget = QWidget()  
        self.setCentralWidget(self.central_widget)  
          
        self.layout = QVBoxLayout()  
        self.central_widget.setLayout(self.layout)  
          
        self.label = QLabel("Выберите категорию песен:")  
        self.layout.addWidget(self.label)  
          
        self.old_button = QPushButton("Старые песни")  
        self.old_button.clicked.connect(self.show_old_songs)  
        self.layout.addWidget(self.old_button)  
          
        self.new_button = QPushButton("Новые песни")  
        self.new_button.clicked.connect(self.show_new_songs)  
        self.layout.addWidget(self.new_button)  
          
        self.list_widget = QListWidget()  
        self.layout.addWidget(self.list_widget)  
          
        self.old_songs = OldSongs()  
        self.new_songs = NewSongs()  
  
    def show_old_songs(self):  
        self.list_widget.clear()  
        for song in self.old_songs.get_songs():  
            self.list_widget.addItem(song)  
  
    def show_new_songs(self):  
        self.list_widget.clear()  
        for song in self.new_songs.get_songs():  
            self.list_widget.addItem(song)  
  
if __name__ == "__main__":  
    app = QApplication(sys.argv)  
    window = MainWindow()  
    window.show()  
    sys.exit(app.exec_())  
