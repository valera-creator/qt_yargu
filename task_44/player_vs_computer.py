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
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)  # для отрисовки фона виджета
        self.setObjectName("widget_game")

        self.bot_name = "компьютер"

        self.model = GameModel()
        self.main_layout = QHBoxLayout()
        self.vertical_game_layout = QVBoxLayout()
        self.vertical_game_layout.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)

        self.view = QTableView()
        self.view.setModel(self.model)
        self.view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.view.verticalHeader().setVisible(False)

        # никнеймы игрока (lineedit, ввод)
        max_length = 16
        self.name_player_line_edit = QLineEdit()
        self.name_player_line_edit.setPlaceholderText(f"Ник игрока (макс {max_length} символов)")
        self.name_player_line_edit.setMaxLength(max_length)
        self.name_player_line_edit.setObjectName("edit_nickname")

        # никнеймы игроков (label, чтение)
        self.name_player_label = QLabel()
        self.name_player_label.setObjectName("label_nickname")

        # поля ввода
        regex_num = QRegularExpression(r"^[1-9]\d{3}$")
        self.num_player = QLineEdit()
        self.num_player.setPlaceholderText("Загадайте 4-значное число")
        self.num_player.setValidator(QRegularExpressionValidator(regex_num))
        self.num_player.setObjectName("num")

        # поля для сообщения некорректного ввода
        self.info_player = QLabel()
        self.info_player.setObjectName("info")
        self.info_player.setWordWrap(True)

        # кнопка запуска игры
        self.btn = QPushButton("Начать")
        self.btn.setObjectName("btn_game")
        self.btn.clicked.connect(self.btn_signal)

        self.vertical_game_layout.addWidget(self.name_player_line_edit)
        self.vertical_game_layout.addWidget(self.name_player_label)
        self.vertical_game_layout.addWidget(self.num_player)
        self.vertical_game_layout.addWidget(self.info_player)
        self.vertical_game_layout.addWidget(self.btn)

        self.main_layout.addWidget(self.view)
        self.main_layout.addLayout(self.vertical_game_layout)
        self.setLayout(self.main_layout)

    def notify_uncorrected(self, res_correct_player):
        """уведомление о неправильном вводе"""
        if not res_correct_player[0]:
            self.info_player.setText(res_correct_player[1])

    @Slot()
    def btn_signal(self):
        """
        подготовка виджетов и содержимое виджетов к игре
        если игра уже окончена, то можно только нажать "завершить" и начать заново
        если игра не окончена, то выполняется проверка корректности ввода и состояния игры: начало или продолжение хода
        """
        if not self.model.is_game_end():
            res_correct_player = self.model.check_correct_num(self.num_player.text())
            self.notify_uncorrected(res_correct_player)
            res_correct = res_correct_player[0]
            if res_correct and not self.model.is_game_on():
                self.start_game()

            elif res_correct and self.model.is_game_on():
                self.event_game()
        else:
            self.restart_game()

    def start_game(self):
        self.game_active_changed.emit(True)
        self.info_player.clear()

        self.model.set_num_1(self.num_player.text())
        num_pc = self.model.generate_num_for_computer()
        self.model.set_num_2(num_pc)

        self.num_player.clear()
        self.num_player.setPlaceholderText("Угадайте 4-значное число компьютера")

        self.name_player_label.setText(self.model.get_name(self.name_player_line_edit.text(), ""))
        self.name_player_line_edit.setVisible(False)
        self.name_player_line_edit.setEnabled(False)

        self.btn.setText("Сходить")

        self.model.set_game_on(True)
        self.model.set_game_end(False)

    def restart_game(self):
        """возвращение виджетов и состояний к стартовому состоянию, удаление истории ходов"""
        self.game_active_changed.emit(False)

        self.num_player.clear()
        self.num_player.setPlaceholderText("Загадайте 4-значное число")

        self.name_player_line_edit.setVisible(True)
        self.name_player_line_edit.setEnabled(True)

        self.btn.setText("Начать")
        self.info_player.clear()

        self.num_player.setEnabled(True)

        self.model.set_game_on(False)
        self.model.set_game_end(False)

        self.model.clear_data()

    def event_game(self):
        """обработка самой игры"""
        player_num = self.num_player.text()
        computer_num = self.model.generate_num_for_computer()  # случайное число для угадывания

        player_res, computer_res = self.model.calculate_cows_bulls(player_num, computer_num)
        self.model.append_data([self.name_player_label.text(), player_num, *player_res])
        self.model.append_data([self.bot_name, computer_num, *computer_res])

        self.info_player.clear()
        self.num_player.clear()

        bulls_player, cows_player = player_res
        bulls_computer, cows_computer = computer_res

        if bulls_player == 4 or bulls_computer == 4:
            self.make_game_over(bulls_player, bulls_computer)

    def make_game_over(self, bulls_player, bulls_computer):
        """вывод текста исхода игры, блокировка ввода, установка состояния завершения игры"""
        if bulls_player == 4 and bulls_computer == 4:
            self.info_player.setText("Ничья")
            self.num_player.setText(
                f"Ваше загаданное число: {self.model.get_num_1()}, "
                f"загаданное число компьютера: {self.model.get_num_2()}"
            )
        elif bulls_player == 4:
            self.info_player.setText("Победа!")
            self.num_player.setText(
                f"Ваше загаданное число: {self.model.get_num_1()}, "
                f"загаданное число компьютера: {self.model.get_num_2()}"
            )
        else:
            self.info_player.setText("Поражение!")
            self.num_player.setText(
                f"Ваше загаданное число: {self.model.get_num_1()}, "
                f"загаданное число компьютера: {self.model.get_num_2()}"
            )

        self.num_player.setEnabled(False)
        self.model.set_game_on(False)
        self.model.set_game_end(True)  # блокируем игровые события с кнопкой, можно только завершить игру
        self.btn.setText("Завершить")
