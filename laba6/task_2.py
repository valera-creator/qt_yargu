from PySide6.QtWidgets import (QMainWindow, QApplication, QVBoxLayout, QWidget, QListView, QMenu)
from PySide6.QtGui import QAction
from PySide6.QtCore import Slot, QModelIndex
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

        # изменение редактирования в верхней панели
        # срабатывает в любом случае, когда меняется текущий индекс currentIndex
        self.view.selectionModel().currentChanged.connect(self.update_edit_menu_state)

    def add_up_menu(self):
        menubar = self.menuBar()
        menu_create = menubar.addMenu("Меню")
        action_create_menu = menu_create.addAction("Создать")
        action_create_menu.triggered.connect(self.create_note)

        # редактировать в верхнем меню
        self.action_edit = menu_create.addAction("Редактировать")
        self.action_edit.triggered.connect(lambda: self.edit_note(self.view.currentIndex()))
        self.action_edit.setEnabled(False)  # по умолчанию неактивен
        self.action_edit.setVisible(False)  # по умолчанию невидимый

    @Slot()
    def update_edit_menu_state(self):
        # Обновляет доступность пункта "Редактировать" в верхнем меню, если есть выделенный элемент
        has_selection = self.view.currentIndex().isValid()
        self.action_edit.setEnabled(has_selection)
        self.action_edit.setVisible(has_selection)

    def contextMenuEvent(self, e):
        context = QMenu(self)
        click_pos = self.view.viewport().mapFromGlobal(e.globalPos())  # пересчет на координаты окна в виджете, где клик
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
            date = dlg.get_date()
            self.model.append_data(text, date)

    @Slot()
    def edit_note(self, index):
        text = self.model.get_text_by_index(index.row())
        date = self.model.get_date_by_index(index.row())
        dlg = CustomDialog("Редактирование", text, date)
        if dlg.exec():
            text = dlg.get_text()
            date = dlg.get_date()
            self.model.setData(index, (text, date))


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    app.exec()
