from PySide6.QtWidgets import QApplication, QStyledItemDelegate, QSpinBox, QTableView
from PySide6.QtGui import QStandardItemModel, Qt
from PySide6.QtCore import QModelIndex


class SpinBoxDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        super().__init__(parent)

    def createEditor(self, parent, option, index):
        editor = QSpinBox(parent)
        editor.setFrame(False)
        editor.setMinimum(0)
        editor.setMaximum(100)
        return editor

    def setEditorData(self, editor, index):
        value = index.model().data(index, Qt.EditRole)
        editor.setValue(value)

    def setModelData(self, editor, model, index):
        value = editor.value()
        model.setData(index, value, Qt.EditRole)


if __name__ == '__main__':
    app = QApplication([])
    model = QStandardItemModel(4, 2)
    tableView = QTableView()
    tableView.setModel(model)
    delegate = SpinBoxDelegate()
    tableView.setItemDelegate(delegate)
    tableView.horizontalHeader().setStretchLastSection(True)

    for row in range(4):
        for column in range(2):
            index = model.index(row, column, QModelIndex())
            value = (row + 1) * (column + 1)
            model.setData(index, value)

    tableView.setWindowTitle("Spin Box Delegate")
    tableView.show()
    app.exec()
