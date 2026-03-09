# import pandas as pd
# from PySide6.QtWidgets import QTableView, QWidget, QVBoxLayout, QLineEdit, QLabel, \
#     QComboBox, QPushButton, QMainWindow, QApplication, QFormLayout
# from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt, QSortFilterProxyModel, QRect
#
#
# class DataFrameModel(QAbstractTableModel):
#     def __init__(self):
#         super(DataFrameModel, self).__init__()
#         self.__oscarData = pd.read_csv('oscar_age_female.csv')
#
#     def rowCount(self, parent=QModelIndex()):
#         return len(self.__oscarData.index)
#
#     def columnCount(self, parent=QModelIndex()):
#         return len(self.__oscarData.columns.values)
#
#     def data(self, index, role=Qt.DisplayRole):
#         if role == Qt.DisplayRole:
#             return str(self.__oscarData.iloc[index.row(), index.column()])
#
#     def headerData(self, col, orientation, role=Qt.DisplayRole):
#         if len(self.__oscarData.columns) == 0:
#             return
#         if role == Qt.DisplayRole:
#             if orientation == Qt.Horizontal:
#                 return str(self.__oscarData.columns[col])
#             if orientation == Qt.Vertical:
#                 return str(self.__oscarData.index[col])
#         return None
#
#     def column_list(self):
#         return self.__oscarData.columns
#
#
# class DataFrameTable(QTableView):
#     def __init__(self, parent=None):
#         QTableView.__init__(self)
#         model = DataFrameModel()
#         self.__proxyModel = QSortFilterProxyModel()
#         self.__proxyModel.setSourceModel(model)
#         self.setModel(self.__proxyModel)
#         self.__proxyModel.sort(1, Qt.AscendingOrder)
#
#     def applyFilters(self, query):
#         self.__proxyModel.setFilterFixedString(query)
#         return
#
#
# class FilterWidget(QWidget):
#     def __init__(self, parent, table, title=None):
#         super(FilterWidget, self).__init__(parent)
#         self.__table = table
#         self.setWindowTitle('Поиск')
#         self.setMaximumHeight(200)
#         form = QFormLayout(self)
#         self.__queryedit = QLineEdit(self)
#         form.addRow(QLabel("Запрос:"), self.__queryedit)
#
#         self.__searchcolw = QComboBox()
#         cols = list(self.__table.model.column_list())
#         cols.insert(0, 'Везде')
#         self.__searchcolw.addItems(cols)
#         form.addRow(QLabel("Колонка:"), self.__searchcolw)
#         btn = QPushButton('Поиск')
#         btn.clicked.connect(self.apply)
#         form.addWidget(btn)
#
#     def apply(self):
#         proxy = self.__table.proxy
#         searchcol = self.__searchcolw.currentText()
#         text = self.__queryedit.text()
#         if searchcol == 'Везде':
#             proxy.setFilterKeyColumn(-1)
#         else:
#             c = self.__table.model.column_list().get_loc(searchcol)
#             proxy.setFilterKeyColumn(c)
#         proxy.setFilterCaseSensitivity(Qt.CaseInsensitive)
#         self.__table.applyFilters(text)
#         return
#
#     def clear(self):
#         self.__table.proxy.setFilterFixedString("")
#
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setGeometry(QRect(100, 100, 800, 500))
#         layout = QVBoxLayout()
#         table = DataFrameTable()
#         layout.addWidget(table)
#         filterw = FilterWidget(self, table)
#         layout.addWidget(filterw)
#
#         container = QWidget()
#         container.setLayout(layout)
#         self.setCentralWidget(container)
#
#
# app = QApplication([])
# window = MainWindow()
# window.show()
# app.exec()
