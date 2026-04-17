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
        self.name_player1_line_edit.setPlaceholderText(f"Ник 1-го игрока (макс {max_length} символов)")
        self.name_player1_line_edit.setMaxLength(max_length)
        self.name_player1_line_edit.setObjectName("edit_nickname")
        self.name_player2_line_edit = QLineEdit()
        self.name_player2_line_edit.setPlaceholderText(f"Ник 2-го игрока (макс {max_length} символов)")
        self.name_player2_line_edit.setMaxLength(max_length)
        self.name_player2_line_edit.setObjectName("edit_nickname")

        # никнеймы игроков (label, чтение)
        self.name_player1_label = QLabel()
        self.name_player1_label.setObjectName("label_nickname")
        self.name_player2_label = QLabel()
        self.name_player2_label.setObjectName("label_nickname")

        # поля ввода
        regex_num = QRegularExpression(r"^[1-9]\d{3}$")
        self.num_player1 = QLineEdit()
        self.num_player1.setPlaceholderText("Загадайте 4-значное число")
        self.num_player1.setValidator(QRegularExpressionValidator(regex_num))
        self.num_player1.setObjectName("num")
        self.num_player1.setEchoMode(QLineEdit.Password)
        self.num_player2 = QLineEdit()
        self.num_player2.setPlaceholderText("Загадайте 4-значное число")
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
        self.btn = QPushButton("Начать")
        self.btn.clicked.connect(self.btn_signal)

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

        self.vertical_game_layout.addWidget(self.btn)
        self.setLayout(self.main_layout)

    def notify_uncorrected(self, res_correct_player1, res_correct_player2):
        """уведомление о неправильном вводе"""
        if not res_correct_player1[0]:
            self.info_player1.setText(res_correct_player1[1])
        if not res_correct_player2[0]:
            self.info_player2.setText(res_correct_player2[1])

    @Slot()
    def btn_signal(self):
        """
        подготовка виджетов и содержимое виджетов к игре
        если игра уже окончена, то пользователь может только нажать "завершить" и начать заново
        если игра не окончена, то пользователь может или начать её, или продолжить ходить
        """
        if not self.model.is_game_end():
            res_correct_player1 = self.model.check_correct_num(self.num_player1.text())
            res_correct_player2 = self.model.check_correct_num(self.num_player2.text())

            self.notify_uncorrected(res_correct_player1, res_correct_player2)
            res_correct = res_correct_player1[0] and res_correct_player2[0]

            if res_correct and not self.model.is_game_on():
                self.start_game()

            elif res_correct and self.model.is_game_on():
                self.event_game()
        else:
            self.restart_game()

    def start_game(self):
        """настройка для запуска игры, переход в режим начала игры"""
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

        self.btn.setText("Сходить")

        self.num_player1.setPlaceholderText(f"Угадайте 4-значное число {self.name_player2_label.text()}")
        self.num_player2.setPlaceholderText(f"Угадайте 4-значное число {self.name_player1_label.text()}")

        self.model.set_game_on(True)
        self.model.set_game_end(False)

    def restart_game(self):
        """возвращение виджетов к стартовому состоянию, удаление истории ходов"""
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

        self.name_player1_label.clear()
        self.name_player2_label.clear()

        self.btn_view_num_player1.setEnabled(True)
        self.btn_view_num_player2.setEnabled(True)

        self.btn.setText("Начать")

        self.num_player1.setPlaceholderText("Загадайте 4-значное число")
        self.num_player2.setPlaceholderText("Загадайте 4-значное число")

        self.num_player1.setEnabled(True)
        self.num_player2.setEnabled(True)

        self.model.set_game_end(False)
        self.model.clear_data()

    def event_game(self):
        """обработка самой игры"""
        first_num = self.num_player1.text()
        second_num = self.num_player2.text()

        self.info_player1.clear()
        self.info_player2.clear()

        first_player_res, second_player_res = self.model.calculate_cows_bulls(first_num, second_num)
        self.model.append_data([self.name_player1_label.text(), first_num, *first_player_res])
        self.model.append_data([self.name_player2_label.text(), second_num, *second_player_res])

        self.num_player1.clear()
        self.num_player2.clear()

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
        """вывод текста исхода игры, блокировка ввода, установка состояния завершения игры"""
        if bulls1 == 4 and bulls2 == 4:
            self.info_player1.setText("Ничья")
            self.info_player2.setText("Ничья")
            self.num_player1.setText("Ничья")
            self.num_player2.setText("Ничья")
        elif bulls1 == 4:
            self.info_player1.setText("Победа!")
            self.info_player2.setText("Поражение!")
            self.num_player1.setText("Победа!")
            self.num_player2.setText("Поражение!")
        else:
            self.info_player1.setText("Поражение!")
            self.info_player2.setText("Победа!")
            self.num_player1.setText("Поражение!")
            self.num_player2.setText("Победа!")

        self.num_player1.setEnabled(False)
        self.num_player2.setEnabled(False)

        self.model.set_game_on(False)
        self.model.set_game_end(True)  # блокируем игровые события с кнопкой, можно только завершить игру
        self.btn.setText("Завершить")
