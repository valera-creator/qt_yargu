from PySide6.QtCore import QAbstractTableModel, Qt, QModelIndex
import random


def generate_num_for_computer():
    digits = list("0123456789")
    random.shuffle(digits)
    if digits[0] == '0':
        digits[0], digits[1] = digits[1], digits[0]
    return "".join(digits[:4])


class GameModel(QAbstractTableModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.__data_model = []
        self.__headers = ["№ попытки", "Игрок", "Число", "Быки", "Коровы"]

        self.__num_player1 = ""
        self.__num_player2 = ""

        self.__game_on = False

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
        if orientation == Qt.Vertical:
            return f"{section + 1}"  # Нумерация с 1
        return section

    def data(self, index, role=Qt.DisplayRole):
        """возврат данных для отображения"""
        if role == Qt.DisplayRole:
            row_value = self.__data_model[index.row()]
            return row_value[index.column()]
        return None

    def append_data(self, data_game):
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

    def clear_data(self):
        """полное удаление всех данных о ходах"""
        self.removeRows(row=0, count=len(self.__data_model))

    @staticmethod
    def check_correct_num(num):
        if len(num) != 4:
            return False, "Число должно быть четырёхзначным"
        if len(set(num)) != 4:
            return False, "Число должно состоять из уникальных цифр"
        return True,

    def calculate_cows_bulls(self):
        pass

    def is_game_on(self):
        return self.__game_on
