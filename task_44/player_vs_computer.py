from PySide6.QtCore import QRegularExpression, Slot, Qt, Signal
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QTableView, QHeaderView, QLineEdit, QLabel, QPushButton
from model_game import GameModel


class PlayerVsComputer(QWidget):
    # сигнал для того, чтобы в главном окне отключить переключение вкладок
    game_active_changed = Signal(bool)

    def __init__(self):
        super().__init__()
        self.setMinimumSize(700, 500)
        self.setWindowTitle("PVC")

        self.model = GameModel()
        self.main_layout = QHBoxLayout()
        self.vertical_game_layout = QVBoxLayout()
        self.vertical_game_layout.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)

        self.view = QTableView()
        self.view.setMinimumWidth(300)
        self.view.setModel(self.model)
        self.view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.view.verticalHeader().setVisible(False)

        # никнеймы игрока (lineedit, ввод)
        max_length = 16
        self.name_player1_line_edit = QLineEdit()
        self.name_player1_line_edit.setPlaceholderText(f"ник 1-го игрока (макс {max_length} символов)")
        self.name_player1_line_edit.setMaxLength(max_length)
        self.name_player1_line_edit.setObjectName("edit_nickname")

        # никнеймы игроков (label, чтение)
        self.name_player1_label = QLabel("player 1")
        self.name_player1_label.setObjectName("label_nickname")

        # поля ввода
        regex_num = QRegularExpression(r"^[1-9]\d{3}$")
        self.num_player1 = QLineEdit()
        self.num_player1.setPlaceholderText("загадайте 4-значное число")
        self.num_player1.setValidator(QRegularExpressionValidator(regex_num))
        self.num_player1.setObjectName("num")
        self.num_player1.setEchoMode(QLineEdit.Password)

        # поля для сообщения некорректного ввода
        self.err_player1 = QLabel()
        self.err_player1.setObjectName("error")
        self.err_player1.setWordWrap(True)

        # кнопка запуска игры
        self.btn_start = QPushButton("start")
        self.btn_start.clicked.connect(self.start)

        self.vertical_game_layout.addWidget(self.name_player1_line_edit)
        self.vertical_game_layout.addWidget(self.name_player1_label)
        self.vertical_game_layout.addWidget(self.num_player1)
        self.vertical_game_layout.addWidget(self.btn_start)
        self.vertical_game_layout.addWidget(self.err_player1)

        self.main_layout.addWidget(self.view)
        self.main_layout.addLayout(self.vertical_game_layout)
        self.setLayout(self.main_layout)

    @Slot()
    def start(self):
        self.game_active_changed.emit(True)

    def restart_game(self):
        self.game_active_changed.emit(False)
        self.model.clear_data()
