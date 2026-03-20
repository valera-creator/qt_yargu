from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QComboBox, QLabel, QLineEdit, QProgressBar, QSlider


class Window(QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.setMinimumWidth(500)
        self.setMinimumHeight(500)
        layout = QVBoxLayout()
        combo = QComboBox()
        combo.addItems(['красный', 'зеленый', 'синий'])
        layout.addWidget(combo)
        label = QLabel()
        label.setLineWidth(2)
        layout.addWidget(label)

        # passwordLineEdit = QLineEdit()
        # passwordLineEdit.setEchoMode(QLineEdit.Password)
        # layout.addWidget(passwordLineEdit)

        # bar = QProgressBar()
        # bar.setRange(30, 110)
        # bar.setValue(50)
        # bar.setTextVisible(True)
        # layout.addWidget(bar)

        # slider = QSlider()
        # slider.setRange(-4, 38)
        # slider.setOrientation(Qt.Orientation.Horizontal)
        # layout.addWidget(slider)
        self.setLayout(layout)



if __name__ == "__main__":
    app = QApplication()
    window = Window()
    window.show()
    with open("style_widgets.qss", "r") as f:
        style = f.read()
        app.setStyleSheet(style)
    app.exec()
