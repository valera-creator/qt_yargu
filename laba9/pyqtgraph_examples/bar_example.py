from PySide6.QtWidgets import QApplication, QMainWindow
import pyqtgraph as pg
import pandas as pd


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        plot = pg.plot()
        df = pd.read_csv("biostats.csv")
        ages = df.iloc[:, 2].values.flatten().tolist()
        x = [i + 1 for i in range(len(ages))]
        bargraph = pg.BarGraphItem(x=x, height=ages, width=0.6, brush='g')
        plot.addItem(bargraph)
        self.setCentralWidget(plot)
        ax = plot.getAxis('bottom')
        xlab = df.iloc[:, 0].values.flatten().tolist()
        ticks = [list(zip(x, xlab))]
        ax.setTicks(ticks)


if __name__ == '__main__':
    app = QApplication([])
    main = MainWindow()
    main.show()
    app.exec()
