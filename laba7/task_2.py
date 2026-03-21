from PySide6.QtCore import Slot, Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QWidget, QScrollArea, QVBoxLayout, QLabel, QPushButton, QFileDialog


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Список картинок")
        self.setObjectName("main")
        self.v_layout = QVBoxLayout()

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.widget_scroll = QWidget()  # скроллинг работает с Qwidget
        self.widget_scroll.setObjectName("widget_srcoll")

        self.image_layout = QVBoxLayout()
        self.widget_scroll.setLayout(self.image_layout)  # пихаю layout в виджет, который будет в скроллинге
        self.scroll_area.setWidget(self.widget_scroll)

        self.v_layout.addWidget(self.scroll_area)  # добавляю скроллинг в основной Qwidget, где будет скроллинг и кнопка

        self.btn_add_image = QPushButton("Добавить")
        self.btn_add_image.clicked.connect(self.btn_click)
        self.v_layout.addWidget(self.btn_add_image)

        self.setLayout(self.v_layout)

    def add_image(self, path):
        image = QPixmap(path)
        label_image = QLabel()
        if not image.isNull():
            scaled_pixmap = image.scaledToWidth(self.width() - 75, Qt.SmoothTransformation)
            label_image.setPixmap(scaled_pixmap)
            self.image_layout.addWidget(label_image)

    @Slot()
    def btn_click(self):
        dlg = QFileDialog()
        path, _ = dlg.getOpenFileName(filter="Images (*.png *.jpg *.jpeg *.bmp *.webp)")
        self.add_image(path)


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    with open("task_2_style.qss", "r") as f:
        style = f.read()
        app.setStyleSheet(style)
    app.exec()
