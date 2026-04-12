from PySide6.QtWidgets import QApplication, QMainWindow
import pandas as pd
import pyqtgraph as pg


def get_df(path_file):
    try:
        data = pd.read_csv(path_file)
        _ = data["2007"]
        return data
    except FileNotFoundError:
        quit(f"Ошибка: отсутствует файл по пути {path_file}")
    except pd.errors.EmptyDataError:
        quit("Ошибка: в файле отсутствует информация про 2007 год")
    except KeyError:
        quit("Ошибка: в файле отсутствует информация про 2007 год")


def check_correct_data(data):
    for elem in data:
        try:
            int(elem)
        except ValueError:
            quit(f"{elem} в файле не является числом")


class Hurricanes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(750, 600)
        self.setWindowTitle("Hurricanes")
        self.df = get_df("hurricanes.csv")

        self.month = self.df["Month"].tolist()
        self.year_2007 = self.df["2007"].tolist()

        self.layout = pg.GraphicsLayoutWidget()
        self.make_graphic_hurricanes_2007()
        self.make_graphic_summ_hurricanes()

        self.setCentralWidget(self.layout)

    def make_graphic_hurricanes_2007(self):
        check_correct_data(self.year_2007)

        plot_widget = self.layout.addPlot(0, 0)
        plot_widget.showGrid(x=True, y=True, alpha=0.5)
        x = [i + 1 for i in range(len(self.month))]
        bargraph = pg.BarGraphItem(x=x, height=self.year_2007, width=0.6, brush='g', pen="k")

        # месяцы внизу
        ax = plot_widget.getAxis('bottom')
        ticks = [list(zip(x, self.month))]
        ax.setTicks(ticks)

        plot_widget.setLabel("bottom", "Месяц")
        plot_widget.setLabel("left", "Количество ураганов за месяц")

        plot_widget.setTitle("График ураганов за 2007 год")
        plot_widget.addItem(bargraph)

    def get_info_years_hurricanes(self):
        """метод возвращает список годов и список количества ураганов или сообщает об ошибки некорректности данных"""
        hurricanes_per_years = []
        for i in range(2, len(self.df.columns)):
            try:
                cnt_hurricane_cur_year = sum(self.df.iloc[:, i].values.tolist())
                hurricanes_per_years.append(cnt_hurricane_cur_year)
            except TypeError:
                quit(f"Ошибка: нашлось не числовое значение в файле в количестве ураганов")

        try:
            years = list(map(int, self.df.columns[2:].values.tolist()))
        except ValueError:
            quit(f"Ошибка: нашлось не числовое значение года в файле")

        return years, hurricanes_per_years

    def make_graphic_summ_hurricanes(self):
        plot_widget = self.layout.addPlot(1, 0)
        plot_widget.showGrid(x=True, y=True, alpha=0.5)

        years, hurricanes_per_years = self.get_info_years_hurricanes()
        bargraph = pg.BarGraphItem(x=years, height=hurricanes_per_years, width=0.6, brush='g', pen="k")

        plot_widget.setLabel("bottom", "Год")
        plot_widget.setLabel("left", "Количество ураганов за год")

        plot_widget.setTitle("Сумма ураганов по годам")
        plot_widget.addItem(bargraph)


if __name__ == "__main__":
    app = QApplication([])
    window = Hurricanes()
    window.show()
    app.exec()
