from PySide6.QtCore import QAbstractListModel, Qt, QModelIndex


class MyModel(QAbstractListModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.__data_model = []

    def data(self, index, role=Qt.DisplayRole):
        """возвращает данные из модели для отображения или None"""
        if role == Qt.DisplayRole:
            return self.__data_model[index.row()]
        return None

    def rowCount(self, parent=None):
        """возвращает количество строк, которые нужно отобразить"""
        return len(self.__data_model)

    def insertRows(self, row, count, parent=QModelIndex()):
        if row < 0 or count < 1:
            return False
        self.beginInsertRows(parent, row, row + count - 1)
        self.endInsertRows()
        return True

    def check_text(self, text):
        text = "".join(text.split())
        text = text.replace("ㅤ", "")
        return True if text else False

    def append_data(self, text):
        if self.check_text(text):
            self.__data_model.append(text.strip())
            self.insertRow(len(self.__data_model) - 1)
            return True
        return False

    def removeRows(self, row, count, parent=QModelIndex()):
        if row + count > len(self.__data_model) or count < 1:
            return False
        self.beginRemoveRows(parent, row, row + count - 1)
        del self.__data_model[row:row + count]
        self.endRemoveRows()
        return True
