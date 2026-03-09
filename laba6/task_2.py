import datetime

from PySide6.QtWidgets import (QMainWindow, QApplication, QPushButton, QVBoxLayout, QLabel, QWidget, QListView,
                               QMenuBar, QMenu)
from PySide6.QtGui import QAction
from PySide6.QtCore import Slot, Qt
from task_2_dialog import CustomDialog
from task_2_model import MyModel


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Заметки")
        self.setMinimumSize(330, 330)

        self.v_layout = QVBoxLayout()
        self.model = MyModel()

        # верхнее меню
        self.add_up_menu()

        self.view = QListView()
        self.view.setMinimumWidth(300)
        self.view.setMaximumHeight(225)
        self.view.setModel(self.model)
        self.v_layout.addWidget(self.view)

        # кастомное меню с сигналом для редактирования
        self.view.setContextMenuPolicy(Qt.CustomContextMenu)
        self.view.customContextMenuRequested.connect(self.event_context_menu_view)

        self.widget = QWidget()
        self.widget.setLayout(self.v_layout)
        self.setCentralWidget(self.widget)
        self.setLayout(self.v_layout)

    def add_up_menu(self):
        menubar = self.menuBar()
        menu_create = menubar.addMenu("Меню")
        action_create_menu = menu_create.addAction("Создать")
        action_create_menu.triggered.connect(self.create_note)

    def contextMenuEvent(self, e):
        context = QMenu(self)
        create = QAction("Создать", self)
        create.triggered.connect(self.create_note)
        context.addAction(create)
        context.exec(e.globalPos())

    @Slot()
    def create_note(self):
        dlg = CustomDialog("Создание")
        if dlg.exec():
            text = dlg.get_text()
            time = datetime.datetime.now()
            self.model.append_data(text, time)

    @Slot()
    def edit_note(self):
        cur_row = self.view.currentIndex().row()
        text = self.model.get_text_by_index(cur_row)
        dlg = CustomDialog("Редактирование", text)
        if dlg.exec():
            text = dlg.get_text()
            time = datetime.datetime.now()
            self.model.setData(self.view.currentIndex(), (text, time))

    @Slot()
    def event_context_menu_view(self, position):
        context = QMenu(self)
        if self.view.currentIndex().isValid():
            edit = QAction("Редактировать", self)
            context.addAction(edit)
            edit.triggered.connect(self.edit_note)
        else:
            create = QAction("Создать", self)
            create.triggered.connect(self.create_note)
            context.addAction(create)
        context.exec(self.view.viewport().mapToGlobal(position))


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    app.exec()
