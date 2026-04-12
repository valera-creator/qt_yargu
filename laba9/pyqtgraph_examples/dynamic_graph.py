from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication, QMainWindow
import pyqtgraph as pg
from random import randint


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        graphWidget = pg.PlotWidget()
        self.setCentralWidget(graphWidget)

        self.__x = list(range(100))
        self.__y = [randint(0, 100) for _ in range(100)]

        graphWidget.setBackground('w')

        pen = pg.mkPen(color=(255, 0, 0))
        self.__data_line = graphWidget.plot(self.__x, self.__y, pen=pen)

        timer = QTimer()
        timer.setInterval(50)
        timer.timeout.connect(self.update_plot_data)
        timer.start()

    def update_plot_data(self):
        self.__x = self.__x[1:]
        self.__x.append(self.__x[-1] + 1)

        self.__y = self.__y[1:]
        self.__y.append(randint(0, 100))

        self.__data_line.setData(self.__x, self.__y)


app = QApplication([])
w = MainWindow()
w.show()
app.exec()
