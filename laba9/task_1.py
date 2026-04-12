import math

from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtCharts import QChart, QChartView, QSplineSeries


class ChartSinCos(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(700, 500)
        self.setWindowTitle("График синуса и косинуса")

        self.series_sin = QSplineSeries()
        self.series_sin.setName("Синусоида")

        self.series_cos = QSplineSeries()
        self.series_cos.setName("Косинусоида")

        self.create_points()

        self.chart = QChart()
        self.chart.addSeries(self.series_sin)
        self.chart.addSeries(self.series_cos)
        self.chart.createDefaultAxes()
        self.chart.setTitle("График синуса и косинуса")

        self._chart_view = QChartView(self.chart)
        self.setCentralWidget(self._chart_view)

    def create_points(self):
        for i in range(-180, 181, 10):
            sin = math.sin(math.radians(i))
            cos = math.cos(math.radians(i))
            self.series_sin.append(i, sin)
            self.series_cos.append(i, cos)


if __name__ == "__main__":
    app = QApplication([])

    window = ChartSinCos()
    window.show()
    app.exec()
