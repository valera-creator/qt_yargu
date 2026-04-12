import pyqtgraph as pg
from PySide6.QtWidgets import QApplication
# pip install PyOpenGL
import pyqtgraph.opengl as gl

app = QApplication([])
# 3d-виджет
view = gl.GLViewWidget()
view.show()

# Создаются три сетки координат
xgrid = gl.GLGridItem()
ygrid = gl.GLGridItem()
zgrid = gl.GLGridItem()
view.addItem(xgrid)
view.addItem(ygrid)
view.addItem(zgrid)

# Поворачиваются сетки x и y так, чтобы они смотрели в правильном направлении
xgrid.rotate(90, 0, 1, 0)
ygrid.rotate(90, 1, 0, 0)

# Каждая сетка масштабируется отдельно
xgrid.scale(0.2, 0.1, 0.1)
ygrid.scale(0.2, 0.1, 0.1)
zgrid.scale(0.1, 0.2, 0.1)

app.exec()
