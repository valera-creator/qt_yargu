from PySide6.QtCore import QAbstractListModel, Qt, QModelIndex


class MyModel(QAbstractListModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.__data_model = []  # список кортежей: [(text, date), ...]

    def data(self, index, role=Qt.DisplayRole):
        """возвращает данные из модели для отображения или None"""
        if role == Qt.DisplayRole:
            elem = self.__data_model[index.row()]
            text, date = elem
            return f"Текст заметки: {text}\nВремя последнего изменения: {date}"
        return None

    def setData(self, index, value, role=Qt.EditRole):
        "редактирует элемент в модели"
        if role == Qt.EditRole:
            text, time = value[0], value[1].strftime('%d.%m.%Y %H:%M:%S')
            self.__data_model[index.row()] = (text, time)
            return True
        return False

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

    def append_data(self, text, date):
        if self.check_text(text):
            self.__data_model.append((text, date.strftime('%d.%m.%Y %H:%M:%S')))
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

    def get_text_by_index(self, row):
        return self.__data_model[row][0]
