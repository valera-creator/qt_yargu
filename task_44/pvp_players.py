from PySide6.QtCore import QRegularExpression, Slot, Qt, Signal
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QTableView, QHeaderView, QLineEdit, QPushButton, QLabel
from PySide6.QtGui import QRegularExpressionValidator

from model_game import GameModel


class PvpPlayers(QWidget):
    # сигнал для того, чтобы в главном окне отключить переключение вкладок
    game_active_changed = Signal(bool)

    def __init__(self):
        super().__init__()

        self.setWindowTitle("PVP")

        # layouts
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
        max_length = 16
        self.name_player1_line_edit = QLineEdit()
        self.name_player1_line_edit.setPlaceholderText(f"ник 1-го игрока (макс {max_length} символов)")
        self.name_player1_line_edit.setMaxLength(max_length)
        self.name_player1_line_edit.setObjectName("edit_nickname")
        self.name_player2_line_edit = QLineEdit()
        self.name_player2_line_edit.setPlaceholderText(f"ник 2-го игрока (макс {max_length} символов)")
        self.name_player2_line_edit.setMaxLength(max_length)
        self.name_player2_line_edit.setObjectName("edit_nickname")

        # никнеймы игроков (label, чтение)
        self.name_player1_label = QLabel("player 1")
        self.name_player1_label.setObjectName("label_nickname")
        self.name_player2_label = QLabel("player 2")
        self.name_player2_label.setObjectName("label_nickname")

        # поля ввода
        regex_num = QRegularExpression(r"^[1-9]\d{3}$")
        self.num_player1 = QLineEdit()
        self.num_player1.setPlaceholderText("загадайте 4-значное число")
        self.num_player1.setValidator(QRegularExpressionValidator(regex_num))
        self.num_player1.setObjectName("num")
        self.num_player1.setEchoMode(QLineEdit.Password)
        self.num_player2 = QLineEdit()
        self.num_player2.setPlaceholderText("загадайте 4-значное число")
        self.num_player2.setValidator(QRegularExpressionValidator(regex_num))
        self.num_player2.setObjectName("num")
        self.num_player2.setEchoMode(QLineEdit.Password)

        # поля для сообщения некорректного ввода
        self.info_player1 = QLabel()
        self.info_player1.setObjectName("error")
        self.info_player1.setWordWrap(True)
        self.info_player2 = QLabel()
        self.info_player2.setObjectName("error")
        self.info_player2.setWordWrap(True)

        # кнопки для показа введенного числа перед игрой
        self.btn_view_num_player1 = QPushButton("Показать")
        self.btn_view_num_player1.clicked.connect(lambda: self.view_num(self.btn_view_num_player1, self.num_player1))
        self.btn_view_num_player2 = QPushButton("Показать")
        self.btn_view_num_player2.clicked.connect(lambda: self.view_num(self.btn_view_num_player2, self.num_player2))

        # кнопка запуска игры
        self.btn_start = QPushButton("start")
        self.btn_start.clicked.connect(self.start_game)

        # кнопка для хода игры
        self.btn_make_move = QPushButton("сходить")
        self.btn_make_move.setVisible(False)
        self.btn_make_move.setEnabled(False)
        self.btn_make_move.clicked.connect(self.event_game)

        self.v_player1_layout.addWidget(self.name_player1_line_edit)
        self.v_player1_layout.addWidget(self.name_player1_label)
        self.v_player1_layout.addWidget(self.num_player1)
        self.v_player1_layout.addWidget(self.btn_view_num_player1)
        self.v_player1_layout.addWidget(self.info_player1)
        self.v_player2_layout.addWidget(self.name_player2_line_edit)
        self.v_player2_layout.addWidget(self.name_player2_label)
        self.v_player2_layout.addWidget(self.num_player2)
        self.v_player2_layout.addWidget(self.btn_view_num_player2)
        self.v_player2_layout.addWidget(self.info_player2)

        self.h_game_layout.addLayout(self.v_player1_layout)
        self.h_game_layout.addLayout(self.v_player2_layout)

        self.vertical_game_layout.addLayout(self.h_game_layout)

        self.main_layout.addWidget(self.view)
        self.main_layout.addLayout(self.vertical_game_layout)

        self.vertical_game_layout.addWidget(self.btn_start)
        self.vertical_game_layout.addWidget(self.btn_make_move)
        self.setLayout(self.main_layout)

    def action_labels_info(self, res_correct_player1, res_correct_player2):
        # очистка текста в случае корректного ввода
        if res_correct_player1[0]:
            self.info_player1.clear()
        if res_correct_player2[0]:
            self.info_player2.clear()

        # уведомление о неправильном вводе
        if not res_correct_player1[0]:
            self.info_player1.setText(res_correct_player1[1])
        if not res_correct_player2[0]:
            self.info_player2.setText(res_correct_player2[1])

    @Slot()
    def start_game(self):
        """подготовка виджетов и содержимое виджетов к игре"""

        res_correct_player1 = self.model.check_correct_num(self.num_player1.text())
        res_correct_player2 = self.model.check_correct_num(self.num_player2.text())

        self.action_labels_info(res_correct_player1, res_correct_player2)
        res_correct = res_correct_player1[0] and res_correct_player2[0]

        # начало игры
        if res_correct:
            self.game_active_changed.emit(True)
            self.name_player1_line_edit.setReadOnly(True)
            self.name_player2_line_edit.setReadOnly(True)
            self.name_player1_line_edit.setVisible(False)
            self.name_player2_line_edit.setVisible(False)

            self.info_player1.clear()
            self.info_player2.clear()

            self.model.set_num_1(self.num_player1.text())
            self.model.set_num_2(self.num_player2.text())

            self.name_player1_label.setText(self.model.get_name(self.name_player1_line_edit.text(), "1"))
            self.name_player2_label.setText(self.model.get_name(self.name_player2_line_edit.text(), "2"))

            self.num_player1.clear()
            self.num_player2.clear()
            self.num_player1.setEchoMode(QLineEdit.Normal)
            self.num_player2.setEchoMode(QLineEdit.Normal)

            self.btn_view_num_player1.setVisible(False)
            self.btn_view_num_player1.setEnabled(False)
            self.btn_view_num_player2.setVisible(False)
            self.btn_view_num_player2.setEnabled(False)

            self.btn_start.setVisible(False)
            self.btn_start.setEnabled(False)

            self.btn_make_move.setVisible(True)
            self.btn_make_move.setEnabled(True)
            self.num_player1.setPlaceholderText(f"угадайте 4-значное число {self.name_player2_label.text()}")
            self.num_player2.setPlaceholderText(f"угадайте 4-значное число {self.name_player1_label.text()}")

    def restart_game(self):
        """возвращение виджетов к доигровому состоянию, удаление истории ходов"""
        self.game_active_changed.emit(False)
        self.name_player1_line_edit.setReadOnly(False)
        self.name_player2_line_edit.setReadOnly(False)
        self.name_player1_line_edit.setVisible(True)
        self.name_player2_line_edit.setVisible(True)

        self.btn_view_num_player1.setVisible(True)
        self.btn_view_num_player2.setVisible(True)

        self.num_player1.setEchoMode(QLineEdit.Password)
        self.num_player2.setEchoMode(QLineEdit.Password)
        self.num_player1.clear()
        self.num_player2.clear()

        self.info_player1.clear()
        self.info_player2.clear()

        self.btn_view_num_player1.setText("Показать")
        self.btn_view_num_player2.setText("Показать")

        self.btn_view_num_player1.setEnabled(True)
        self.btn_view_num_player2.setEnabled(True)

        self.btn_start.setVisible(True)
        self.btn_start.setEnabled(True)

        self.btn_make_move.setVisible(False)
        self.btn_make_move.setEnabled(False)

        self.num_player1.setPlaceholderText("загадайте 4-значное число")
        self.num_player2.setPlaceholderText("загадайте 4-значное число")

        self.num_player1.setEnabled(True)
        self.num_player2.setEnabled(True)

        self.model.clear_data()

    @Slot()
    def event_game(self):
        """обработчка самой игры"""
        first_num = self.num_player1.text()
        second_num = self.num_player2.text()

        res_correct_player1 = self.model.check_correct_num(first_num)
        res_correct_player2 = self.model.check_correct_num(second_num)

        self.action_labels_info(res_correct_player1, res_correct_player2)
        res_correct = res_correct_player1[0] and res_correct_player2[0]

        # продолжение игры
        if res_correct:
            self.info_player1.clear()
            self.info_player2.clear()

            first_player_res, second_player_res = self.model.calculate_cows_bulls(first_num, second_num)
            self.model.append_data([self.name_player1_label.text(), first_num, *first_player_res])
            self.model.append_data([self.name_player2_label.text(), second_num, *second_player_res])

            bulls1, cows1 = first_player_res
            bulls2, cows2 = second_player_res

            if bulls1 == 4 or bulls2 == 4:
                self.make_game_over(bulls1, bulls2)

    @Slot()
    def view_num(self, btn, num):
        """метод меняет текст на кнопке и показывает/скрывает введенное число"""
        if num.echoMode() == QLineEdit.EchoMode.Password:
            btn.setText("Скрыть")
            num.setEchoMode(QLineEdit.Normal)
        else:
            btn.setText("Показать")
            num.setEchoMode(QLineEdit.Password)

    def make_game_over(self, bulls1, bulls2):
        if bulls1 == 4 and bulls2 == 4:
            self.info_player1.setText("ничья")
            self.info_player2.setText("ничья")
        elif bulls1 == 4:
            self.info_player1.setText("победа!")
            self.info_player2.setText("поражение!")
        else:
            self.info_player1.setText("поражение!")
            self.info_player2.setText("победа!")

        self.num_player1.setEnabled(False)
        self.num_player2.setEnabled(False)
