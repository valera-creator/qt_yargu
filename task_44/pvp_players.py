from PySide6.QtCore import QRegularExpression, Slot, Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QTableView, QHeaderView, QLineEdit, QPushButton, QLabel
from PySide6.QtGui import QRegularExpressionValidator
from model_game import GameModel


class PvpPlayers(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PVP")
        self.main_layout = QHBoxLayout()
        self.vertical_game_layout = QVBoxLayout()
        self.vertical_game_layout.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
        self.h_game_layout = QHBoxLayout()
        self.v_player1_layout = QVBoxLayout()
        self.v_player2_layout = QVBoxLayout()

        # модель и таблица
        self.model = GameModel()
        self.view = QTableView()
        self.view.setModel(self.model)
        self.view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.view.verticalHeader().setVisible(False)

        # никнеймы игроков (lineedit, ввод)
        self.name_player1_line_edit = QLineEdit()
        self.name_player1_line_edit.setPlaceholderText("ник 1-го игрока (макс 20 символов)")
        self.name_player1_line_edit.setMaxLength(20)
        self.name_player1_line_edit.setObjectName("edit_nickname")
        self.name_player2_line_edit = QLineEdit()
        self.name_player2_line_edit.setPlaceholderText("ник 2-го игрока (макс 20 символов)")
        self.name_player2_line_edit.setMaxLength(20)
        self.name_player2_line_edit.setObjectName("edit_nickname")

        # никнеймы игроков (label, чтение)
        self.name_player1_label = QLabel("player 1")
        self.name_player1_label.setObjectName("label_nickname")
        self.name_player2_label = QLabel("player 2")
        self.name_player2_label.setObjectName("label_nickname")

        # поля ввода
        regex_num = QRegularExpression(r"^[1-9]\d{3}$")
        self.num_player1 = QLineEdit()
        self.num_player1.setPlaceholderText("введите 4-значное число")
        self.num_player1.setValidator(QRegularExpressionValidator(regex_num))
        self.num_player1.setObjectName("num")
        self.num_player1.setEchoMode(QLineEdit.Password)
        self.num_player2 = QLineEdit()
        self.num_player2.setPlaceholderText("введите 4-значное число")
        self.num_player2.setValidator(QRegularExpressionValidator(regex_num))
        self.num_player2.setObjectName("num")
        self.num_player2.setEchoMode(QLineEdit.Password)

        # поля для сообщения некорректного ввода
        self.err_player1 = QLabel()
        self.err_player1.setObjectName("error")
        self.err_player1.setWordWrap(True)
        self.err_player2 = QLabel()
        self.err_player2.setObjectName("error")
        self.err_player2.setWordWrap(True)

        # кнопка запуска игры
        self.btn_start = QPushButton("start")
        self.btn_start.clicked.connect(self.start)

        self.v_player1_layout.addWidget(self.name_player1_line_edit)
        self.v_player1_layout.addWidget(self.name_player1_label)
        self.v_player1_layout.addWidget(self.num_player1)
        self.v_player1_layout.addWidget(self.err_player1)
        self.v_player2_layout.addWidget(self.name_player2_line_edit)
        self.v_player2_layout.addWidget(self.name_player2_label)
        self.v_player2_layout.addWidget(self.num_player2)
        self.v_player2_layout.addWidget(self.err_player2)

        self.h_game_layout.addLayout(self.v_player1_layout)
        self.h_game_layout.addLayout(self.v_player2_layout)

        self.vertical_game_layout.addLayout(self.h_game_layout)

        self.main_layout.addWidget(self.view)
        self.main_layout.addLayout(self.vertical_game_layout)

        self.vertical_game_layout.addWidget(self.btn_start)
        self.setLayout(self.main_layout)

    @Slot()
    def start(self):
        res1 = self.model.check_correct_num(self.num_player1.text())
        res2 = self.model.check_correct_num(self.num_player2.text())
        if not res1[0]:
            self.err_player1.setText(res1[1])
        if not res2[0]:
            self.err_player2.setText(res2[1])
        else:
            res = res1[0] and res2[0]

    def restart(self):
        pass

    def make_game_over(self):
        pass

    def is_game_on(self):
        """возвращает bool значение, закончилась игра или нет"""
        return self.model.is_game_on()

    def clear_data(self):
        """очистка всей статистики ходов"""
        self.model.clear_data()
