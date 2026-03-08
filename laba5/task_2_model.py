from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt

from laba5.task_2_product import Product


class TableModelProduct(QAbstractTableModel):
    def __init__(self):
        super(TableModelProduct, self).__init__()
        self.__product_list = self.__create_default_data()
        self.__headers = ['Название', 'Количество', 'Единиц, кг']

    def __create_default_data(self):
        return [
            Product("Виноград", 10, 20),
            Product("Сливы", 20, 30),
            Product("Яблоки зелёные", 30, 40)
        ]

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None
        if role == Qt.DisplayRole:
            product = self.__product_list[index.row()]
            if index.column() == 0:
                return product.get_name()
            elif index.column() == 1:
                return product.get_cnt()
            elif index.column() == 2:
                return product.get_weight()
        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role != Qt.DisplayRole:
            return None
        if orientation == Qt.Horizontal:
            return self.__headers[section]
        if orientation == Qt.Vertical:
            return f"{section + 1}"  # Нумерация с 1
        return section

    def rowCount(self, parent=None):
        return len(self.__product_list)

    def columnCount(self, parent=None):
        return len(self.__headers)

    def insertRows(self, row, count, parent=QModelIndex()):
        if row < 0 or count < 1:
            return False
        self.beginInsertRows(parent, row, row + count - 1)
        self.endInsertRows()
        return True

    def append_data(self, name, cnt, weight):
        try:
            product = Product(name, cnt, weight)
        except ValueError as e:
            return False, e

        self.__product_list.append(product)
        self.insertRow(len(self.__product_list) - 1)
        return True,

    def get_total_weight(self):
        weight = 0
        for elem in self.__product_list:
            weight += elem.get_weight() * elem.get_cnt()
        return weight
