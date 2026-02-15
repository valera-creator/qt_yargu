from book import Book
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QFrame, QVBoxLayout, QHBoxLayout, QWidget, QScrollArea


class Window(QMainWindow):
    def add_book(self, name, author, cnt_pages, link):
        try:
            self.books.append(Book(name, author, cnt_pages, link))
        except ValueError as text:
            quit(f"ошибка создания книги: {text}")

    def create_scroll_books(self):
        central_widget = QWidget()  # для привязки layout`ов
        central_widget.setLayout(self.vertical_layout)  # привязка layout`ов к виджету

        scroll_area = QScrollArea()  # объект скроллинга
        self.setCentralWidget(scroll_area)  # привязка скроллинга к окну

        scroll_area.setWidgetResizable(True)  # прокрутка и растяжение
        scroll_area.setWidget(central_widget)  # привязка виджета к скроллингу

        for book in self.books:
            horizontal_layout = QHBoxLayout()

            label_text = QLabel(book.get_info(), self)
            label_text.setFrameStyle(QFrame.Panel | QFrame.Raised)  # рамка
            label_text.setLineWidth(2)
            label_text.setMargin(5)

            label_image = QLabel(self)
            label_image.setFrameStyle(QFrame.Panel | QFrame.Raised)  # рамка
            label_image.setLineWidth(2)
            label_image.setAlignment(Qt.AlignCenter)

            image = QPixmap(book.link)
            if image.isNull():
                label_image.setText("Обложка книги не найдена!")
            else:
                image = image.scaledToHeight(250)
                label_image.setPixmap(image)

            horizontal_layout.addWidget(label_text)
            horizontal_layout.addWidget(label_image)

            self.vertical_layout.addLayout(horizontal_layout)

    def __init__(self):
        super().__init__()
        self.setFixedSize(500, 500)
        self.setWindowTitle("книги")
        self.vertical_layout = QVBoxLayout()

        self.books = []
        self.add_book("Демон", "Лермонтов", 272, "demon.png")
        self.add_book("Барышня-крестьянка", "Пушкин", 32, "young_lady.png")
        self.add_book("Мцыри", "Лермонтов", 15, "mcury.png")

        self.create_scroll_books()


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()

    app.exec()
