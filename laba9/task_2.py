from PySide6.QtWidgets import QApplication, QMainWindow
import pandas as pd
import pyqtgraph as pg


def get_df(path_file):
    try:
        data = pd.read_csv(path_file)
        # проверка, что csv файл содержит правильный необходимые столбцы
        _ = data["ID"], data["Girth"], data["Height"], data["Volume"]
        return data
    except FileNotFoundError:
        quit(f"Ошибка: отсутствует файл по пути {path_file}")
    except pd.errors.EmptyDataError:
        quit("Ошибка: столбцы ID, Girth, Height или Volume отсутствуют в файле")
    except KeyError:
        quit("Ошибка: столбцы ID, Girth, Height или Volume отсутствуют в файле")


def check_correct_data(data):
    for elem in data:
        try:
            if elem < 0:
                quit("Показатель дерева не может быть отрицательным")
        except TypeError:
            quit(f"Показатель дерева {elem} в файле не является числом")


class ChartTrees(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(600, 500)
        self.setWindowTitle("Trees")
        df = get_df("trees.csv")

        self.girth = df["Girth"].tolist()
        self.height = df["Height"].tolist()
        self.volume = df["Volume"].tolist()

        self.layout = pg.GraphicsLayoutWidget()
        self.make_graphic("Girth", "Volume", self.girth, self.volume, "b", (0, 0))
        self.make_graphic("Girth", "Height", self.girth, self.height, "g", (0, 1))

        self.setCentralWidget(self.layout)

    def make_graphic(self, x_text, y_text, x_data, y_data, brush, pos_graph):
        plot_widget = self.layout.addPlot(*pos_graph)
        plot_widget.setLabel("bottom", x_text)
        plot_widget.setLabel("left", y_text)

        plot_widget.showGrid(x=True, y=True, alpha=0.5)

        check_correct_data(x_data)
        check_correct_data(y_data)

        scatter = pg.ScatterPlotItem(
            x=x_data,
            y=y_data,
            size=8,
            symbol='o',
            brush=brush,  # Цвет точек
            pen='k',  # Обводка
            pxMode=True
        )
        plot_widget.addItem(scatter)


if __name__ == "__main__":
    app = QApplication([])
    window = ChartTrees()
    window.show()
    app.exec()
