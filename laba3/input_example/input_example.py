from PySide6.QtGui import QColor, Qt
from PySide6.QtWidgets import QApplication, QLineEdit, QWidget, QPushButton, QVBoxLayout, QLabel, QFrame, QTextEdit, \
    QProgressBar, QSlider, QCheckBox, QComboBox, QButtonGroup, QRadioButton, QDial, QSpinBox, QDateTimeEdit, QGroupBox, \
    QHBoxLayout
from PySide6.QtCore import Slot, QDate


class Window(QWidget):
    @Slot()
    def handle_radio_buttons(self):
        print(self.__group.checkedId())

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Примеры виджетов")
        self.setMinimumWidth(300)
        self.setMinimumHeight(100)
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        textEditMd = QTextEdit()
        textEditMd.setMarkdown('## Emphasis \n\n'
                             '**This is bold text** \n\n'
                             '*This is italic text*\n\n'
                             '~~Strikethrough~~')
        layout.addWidget(textEditMd)
        textEditHtml = QTextEdit()
        textEditHtml.setHtml('<h1 style="font-family:verdana;">This is a heading</h1>'
                         '<p style="font-family:courier;">This is a paragraph.</p>')
        layout.addWidget(textEditHtml)
        textEdit = QTextEdit()
        textEdit.setTextColor(QColor("red"))
        textEdit.setText('Первая строка\nВторая строка')
        layout.addWidget(textEdit)

        # bar = QProgressBar()
        # bar.setRange(30, 110)
        # bar.setValue(50)
        # bar.setTextVisible(True)
        # layout.addWidget(bar)

        # slider = QSlider()
        # slider.setRange(-4, 38)
        # slider.setOrientation(Qt.Orientation.Horizontal)
        # layout.addWidget(slider)
        # label = QLabel('0')
        # label.setFrameStyle(QFrame.Panel | QFrame.Raised)
        # label.setLineWidth(2)
        # layout.addWidget(label)
        # slider.sliderMoved.connect(label.setNum)

        # checkBox = QCheckBox("Выбери меня!")
        # layout.addWidget(checkBox)
        # label = QLabel()
        # label.setFrameStyle(QFrame.Panel | QFrame.Raised)
        # label.setLineWidth(2)
        # layout.addWidget(label)
        # checkBox.checkStateChanged.connect(lambda state: label.setText("Выбрано") if state == Qt.Checked else label.setText("Не выбрано"))

        # combo = QComboBox()
        # combo.addItems(['красный', 'зеленый', 'синий'])
        # layout.addWidget(combo)
        # label = QLabel()
        # label.setFrameStyle(QFrame.Panel | QFrame.Raised)
        # label.setLineWidth(2)
        # layout.addWidget(label)
        # combo.currentTextChanged.connect(label.setText)

        # radioRed = QRadioButton('красный')
        # radioRed.setChecked(True)
        # radioGreen = QRadioButton('зеленый')
        # radioBlue = QRadioButton('синий')
        # self.__group = QButtonGroup()
        # self.__group.addButton(radioRed, id=1)
        # self.__group.addButton(radioGreen, id=2)
        # self.__group.addButton(radioBlue, id=3)
        # layout.addWidget(radioRed)
        # layout.addWidget(radioGreen)
        # layout.addWidget(radioBlue)
        # self.__group.buttonClicked.connect(self.handle_radio_buttons)

        # groupBox = QGroupBox("Exclusive Radio Buttons")
        # groupBox.setAlignment(Qt.AlignHCenter)
        # layout.addWidget(groupBox)
        # groupLayout = QHBoxLayout()
        # radio1 = QRadioButton("Radio button 1")
        # radio2 = QRadioButton("Radio button 2")
        # radio3 = QRadioButton("Radio button 3")
        # radio1.setChecked(True)
        # groupLayout.addWidget(radio1)
        # groupLayout.addWidget(radio2)
        # groupLayout.addWidget(radio3)
        # groupBox.setLayout(groupLayout)

        # dial = QDial()
        # dial.setNotchesVisible(True)
        # dial.setRange(-50, 50)
        # layout.addWidget(dial)
        # label = QLabel()
        # label.setFrameStyle(QFrame.Panel | QFrame.Raised)
        # label.setLineWidth(2)
        # layout.addWidget(label)
        # dial.sliderMoved.connect(label.setNum)

        # spinBox = QSpinBox()
        # spinBox.setRange(1, 30)
        # spinBox.setSingleStep(2)
        # spinBox.setSuffix(' кг')
        # layout.addWidget(spinBox)

        # dateTimeEdit = QDateTimeEdit(QDate.currentDate())
        # dateTimeEdit.setMinimumDate(QDate.currentDate().addDays(-365))
        # dateTimeEdit.setMaximumDate(QDate.currentDate().addDays(365))
        # dateTimeEdit.setDisplayFormat("yyyy.MM.dd hh:mm")
        # dateTimeEdit.setCalendarPopup(True)
        # layout.addWidget(dateTimeEdit)


if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    app.exec()
