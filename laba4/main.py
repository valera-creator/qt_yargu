from Univer import University
from Form import Form
from Mouse_work import Mouse

from PySide6.QtWidgets import QMainWindow, QTabWidget, QApplication


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Вкладки")

        self.tab = QTabWidget()

        # вкладка с расписанием
        self.university_tab_widget = University()  # окно типа QWidget вкладки для университета
        self.tab.addTab(self.university_tab_widget, "Расписание")

        # вкладка с формой
        self.form_account_widget = Form()
        self.tab.addTab(self.form_account_widget, "Форма")

        # вкладка с виджетом по клику
        self.widget_click_mouse = Mouse()
        self.tab.addTab(self.widget_click_mouse, "Виджет по клику мыши")

        self.setCentralWidget(self.tab)


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    app.exec()
