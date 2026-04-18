from PySide6.QtCore import QAbstractTableModel, Qt, QModelIndex
from itertools import permutations
import random


class GameModel(QAbstractTableModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.__data_model = []
        self.__headers = ["№ попытки", "Игрок", "Число", "Быки", "Коровы"]

        self.__num_player1 = ""
        self.__num_player2 = ""

        self.__game_on = False  # активна ли игра
        self.__game_end = False  # закончена ли игра

        self.__all_combinations = ["".join(p) for p in permutations("0123456789", 4) if p[0] != '0']
        self.__combinations = self.__all_combinations.copy()

    def rowCount(self, parent=None):
        return len(self.__data_model)

    def columnCount(self, parent=None):
        return len(self.__headers)

    def insertRows(self, row, count, parent=QModelIndex()):
        if row < 0 or count < 1:
            return False
        self.beginInsertRows(parent, row, row + count - 1)
        self.endInsertRows()
        return True

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role != Qt.DisplayRole:
            return None
        if orientation == Qt.Horizontal:
            return self.__headers[section]
        return section

    def data(self, index, role=Qt.DisplayRole):
        """возврат данных для отображения"""
        if role == Qt.ItemDataRole.TextAlignmentRole:  # выравнивание
            return Qt.AlignmentFlag.AlignCenter

        if role == Qt.DisplayRole:
            row_value = self.__data_model[index.row()]
            return row_value[index.column()]
        return None

    def append_data(self, data_game):
        """добавление данных только в том случае, если идёт игра"""
        if self.__game_on:
            cur_attempt = len(self.__data_model) // 2 + 1
            row_value = (cur_attempt, *data_game)
            self.__data_model.append(row_value)
            self.insertRow(len(self.__data_model) - 1)

    def removeRows(self, row, count, parent=QModelIndex()):
        if row + count > len(self.__data_model) or count < 1:
            return False
        self.beginRemoveRows(parent, row, row + count - 1)
        del self.__data_model[row:row + count]
        self.endRemoveRows()
        return True

    def clear_data_game(self):
        """полное удаление всех данных о ходах и загаданных чисел"""
        self.removeRows(row=0, count=len(self.__data_model))
        self.__num_player1 = ""
        self.__num_player2 = ""

    @staticmethod
    def check_correct_num(num):
        """проверка, что введенное число четерёхзначное и состоит из уникальных цифр"""
        if len(num) != 4:
            return False, "Число должно быть четырёхзначным"
        if len(set(num)) != 4:
            return False, "Число должно состоять из уникальных цифр"
        return True,

    @staticmethod
    def get_name(name, default_num_player):
        """возвращает никнейм, если он не пустой, иначе вернет дефолтный никнейм"""
        text = "".join(name.split())
        text = text.replace("ㅤ", "")
        if text:
            return name
        else:
            return f"player {default_num_player}"

    def get_num_1(self):
        """возвращает загаданное число первого игрока"""
        return self.__num_player1

    def get_num_2(self):
        """возвращает загаданное число второго игрока"""
        return self.__num_player2

    def set_num_1(self, num):
        """устанавливает загаданное число первого игрока"""
        self.__num_player1 = num

    def set_num_2(self, num):
        """устанавливает загаданное число второго игрока"""
        self.__num_player2 = num

    def set_num_2_computer_make_combination(self, num):
        """устанавливает загаданное число компьютера и обновляет список комбинаций для компьютера"""
        self.__num_player2 = num
        self.__combinations = self.__all_combinations.copy()
        random.shuffle(self.__combinations)  # чтобы разные числа загадывались

    @staticmethod
    def __calculate_cows_bulls(num_input, player_num):
        """возврат количества быков и коров"""
        cows = 0
        bulls = 0
        for i in range(len(num_input)):
            if player_num[i] == num_input[i]:
                bulls += 1
            elif num_input[i] in player_num:
                cows += 1
        return bulls, cows

    def calculate_all_cows_bulls(self, input_num_player1, input_num_player2):
        """возврат количества быков и коров для каждого игрока"""
        first_player_res = self.__calculate_cows_bulls(input_num_player1, self.__num_player2)
        second_player_res = self.__calculate_cows_bulls(input_num_player2, self.__num_player1)
        return first_player_res, second_player_res

    def is_game_on(self):
        """проверяет, активна ли сейчас игра"""
        return self.__game_on

    def set_game_on(self, val):
        """устанавливает флаг активности игры"""
        self.__game_on = val

    def is_game_end(self):
        """проверяет, завершена ли игра"""
        return self.__game_end

    def set_game_end(self, val):
        """фиксирует факт завершения игры"""
        self.__game_end = val

    @staticmethod
    def check_game_over(bulls1, bulls2, issue):
        """возвращает, закончилась ли игра и исход игры"""
        if bulls1 == 4 and bulls2 == 4:
            return True, issue[0]
        elif bulls1 == 4:
            return True, issue[1]
        elif bulls2 == 4:
            return True, issue[2]
        else:
            return False, None

    @staticmethod
    def generate_num_for_computer():
        """возврат сгенерированного числа для компьютера"""
        digits = list("0123456789")
        random.shuffle(digits)
        if digits[0] == '0':
            digits[0], digits[1] = digits[1], digits[0]
        return "".join(digits[:4])

    def filter_combination(self, prev_guess, prev_bulls, prev_cows):
        """
        оставляет только те числа, в которых количество коров и быков совпадает с названным числом компьютера
        число коров и быков получены из игры: сколько быков и коров в числе, которое назвал компьютер
        """
        self.__combinations = list(
            filter(lambda x: self.__calculate_cows_bulls(x, prev_guess) == (prev_bulls, prev_cows),
                   self.__combinations))

    def make_action_computer(self, prev_guess=None, prev_bulls=None, prev_cows=None):
        """если параметры переданы, то пересчет комбинаций, а иначе ход"""
        if prev_guess is None or prev_bulls is None or prev_cows is None:
            return self.__combinations[0]
        else:
            self.filter_combination(prev_guess, prev_bulls, prev_cows)
