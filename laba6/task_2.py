from PySide6.QtWidgets import (QMainWindow, QApplication, QPushButton, QVBoxLayout, QLabel, QWidget, QListView,
                               QMenuBar, QMenu)
from PySide6.QtGui import QAction
from PySide6.QtCore import Slot, Qt, QModelIndex
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
        click_pos = self.view.viewport().mapFromGlobal(e.globalPos())  # пересчет на координаты окна в виджете
        index = self.view.indexAt(click_pos)  # элемент в view по координатам

        if index.isValid():
            edit = QAction("Редактировать", self)
            context.addAction(edit)
            edit.triggered.connect(lambda: self.edit_note(index))
        else:
            self.view.clearSelection()  # Убирает синюю подсветку
            self.view.setCurrentIndex(QModelIndex())

            create = QAction("Создать", self)
            create.triggered.connect(self.create_note)
            context.addAction(create)
        context.exec(e.globalPos())

    @Slot()
    def create_note(self):
        dlg = CustomDialog("Создание")
        if dlg.exec():
            text = dlg.get_text()
            self.model.append_data(text)

    @Slot()
    def edit_note(self, cur_row):
        text = self.model.get_text_by_index(cur_row.row())
        dlg = CustomDialog("Редактирование", text)
        if dlg.exec():
            text = dlg.get_text()
            self.model.setData(self.view.currentIndex(), text)


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    app.exec()
