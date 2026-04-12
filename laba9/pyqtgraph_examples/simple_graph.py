from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        graphWidget = pg.PlotWidget()
        self.setCentralWidget(graphWidget)

        hour = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        temperature = [30, 32, 34, 32, 33, 31, 29, 32, 35, 45]

        # Белый фон
        graphWidget.setBackground('w')
        graphWidget.setTitle("График температуры", color="b", size="30pt")
        # Параметры для меток на осях
        styles = {"color": "#f00", "font-size": "20px"}
        graphWidget.setLabel("left", "Температура (°C)", **styles)
        graphWidget.setLabel("bottom", "Час", **styles)
        graphWidget.addLegend()
        # Сетка на плоскости с графиком
        graphWidget.showGrid(x=True, y=True)
        graphWidget.setXRange(0, 10, padding=0)
        graphWidget.setYRange(20, 55, padding=0)

        pen = pg.mkPen(color=(255, 0, 0), width=8, style=Qt.SolidLine)
        graphWidget.plot(hour, temperature, name="Датчик 1", pen=pen, symbol='+', symbolSize=30, symbolBrush='b')


if __name__ == '__main__':
    app = QApplication([])
    main = MainWindow()
    main.show()
    app.exec()
