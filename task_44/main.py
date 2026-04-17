from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMainWindow, QApplication, QTabWidget
from pvp_players import PvpPlayers
from player_vs_computer import PlayerVsComputer
from rules_dialog import RulesDialog


def get_text_rules(filename):
    try:
        with open(filename, mode='r', encoding="utf-8") as file:
            return " ".join(file.readlines())
    except FileNotFoundError:
        exit(f"Ошибка: файл {filename} отсутствует")


def get_style(filename):
    try:
        with open(filename, "r") as f:
            data = f.read()
        return data
    except FileNotFoundError:
        exit(f"Ошибка: файл  {filename} отсутствует")


class CowsBulls(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(1210, 500)
        self.setWindowTitle("Коровы и быки")

        self.text_rules = get_text_rules("text_rules.txt")

        self.tab = QTabWidget()

        self.pvp_players = PvpPlayers()
        self.tab.addTab(self.pvp_players, "режим PVP")

        self.player_vs_computer = PlayerVsComputer()
        self.tab.addTab(self.player_vs_computer, "режим PVC")

        self.add_up_menu()
        self.setCentralWidget(self.tab)

        self.pvp_players.game_active_changed.connect(self.toggle_tabs)
        self.player_vs_computer.game_active_changed.connect(self.toggle_tabs)

    @Slot(bool)
    def toggle_tabs(self, is_active):
        self.tab.tabBar().setEnabled(not is_active)

    def add_up_menu(self):
        """создание верхнего меню в главном окне"""
        menubar = self.menuBar()
        menu_create = menubar.addMenu("Меню игры")
        action_new_game_menu = menu_create.addAction("Новая игра")
        action_new_game_menu.triggered.connect(self.make_new_game)

        action_check_rules_menu = menu_create.addAction("Правила игры")
        action_check_rules_menu.triggered.connect(self.check_rules)

    def make_new_game(self):
        active_widget = self.tab.currentWidget()
        active_widget.restart_game()

    def check_rules(self):
        """открывается диалог с текстом правил игры"""
        dl = RulesDialog(self.text_rules)
        dl.exec()


if __name__ == "__main__":
    app = QApplication([])
    window = CowsBulls()
    window.show()
    style = get_style("task_44_style.qss")
    app.setStyleSheet(style)
    app.exec()
