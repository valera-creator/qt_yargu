# https://doc.qt.io/qt-5/qtwidgets-graphicsview-anchorlayout-example.html
from PySide6.QtCore import Qt, QSizeF
from PySide6.QtWidgets import QApplication, QGraphicsView, \
    QGraphicsScene, QPushButton, QSizePolicy, QGraphicsProxyWidget, QGraphicsAnchorLayout, QGraphicsWidget


def createItem(minimum=QSizeF(100.0, 100.0),
               preferred=QSizeF(150.0, 100.0),
               maximum=QSizeF(200.0, 100.0),
               name="0"):
    w = QGraphicsProxyWidget()
    w.setWidget(QPushButton(name))
    w.setData(0, name)
    w.setMinimumSize(minimum)
    w.setPreferredSize(preferred)
    w.setMaximumSize(maximum)
    w.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
    return w


app = QApplication([])
scene = QGraphicsScene()
scene.setSceneRect(0, 0, 800, 480)
minSize = QSizeF(30, 100)
prefSize = QSizeF(210, 100)
maxSize = QSizeF(300, 100)
a = createItem(minSize, prefSize, maxSize, "A")
b = createItem(minSize, prefSize, maxSize, "B")
c = createItem(minSize, prefSize, maxSize, "C")
d = createItem(minSize, prefSize, maxSize, "D")
e = createItem(minSize, prefSize, maxSize, "E")
f = createItem(QSizeF(30, 50), QSizeF(150, 50), maxSize, "F (overflow)")
g = createItem(QSizeF(30, 50), QSizeF(30, 100), maxSize, "G (overflow)")
l = QGraphicsAnchorLayout()
l.setSpacing(0)
w = QGraphicsWidget(wFlags=Qt.Window)
w.setPos(20, 20)
w.setLayout(l)
l.addAnchor(a, Qt.AnchorTop, l, Qt.AnchorTop)
l.addAnchor(b, Qt.AnchorTop, l, Qt.AnchorTop)
l.addAnchor(c, Qt.AnchorTop, a, Qt.AnchorBottom)
l.addAnchor(c, Qt.AnchorTop, b, Qt.AnchorBottom)
l.addAnchor(c, Qt.AnchorBottom, d, Qt.AnchorTop)
l.addAnchor(c, Qt.AnchorBottom, e, Qt.AnchorTop)
l.addAnchor(d, Qt.AnchorBottom, l, Qt.AnchorBottom)
l.addAnchor(e, Qt.AnchorBottom, l, Qt.AnchorBottom)
l.addAnchor(c, Qt.AnchorTop, f, Qt.AnchorTop)
l.addAnchor(c, Qt.AnchorVerticalCenter, f, Qt.AnchorBottom)
l.addAnchor(f, Qt.AnchorBottom, g, Qt.AnchorTop)
l.addAnchor(c, Qt.AnchorBottom, g, Qt.AnchorBottom)

l.addAnchor(l, Qt.AnchorLeft, a, Qt.AnchorLeft)
l.addAnchor(l, Qt.AnchorLeft, d, Qt.AnchorLeft)
l.addAnchor(a, Qt.AnchorRight, b, Qt.AnchorLeft)

l.addAnchor(a, Qt.AnchorRight, c, Qt.AnchorLeft)
l.addAnchor(c, Qt.AnchorRight, e, Qt.AnchorLeft)

l.addAnchor(b, Qt.AnchorRight, l, Qt.AnchorRight)
l.addAnchor(e, Qt.AnchorRight, l, Qt.AnchorRight)
l.addAnchor(d, Qt.AnchorRight, e, Qt.AnchorLeft)

l.addAnchor(l, Qt.AnchorLeft, f, Qt.AnchorLeft)
l.addAnchor(l, Qt.AnchorLeft, g, Qt.AnchorLeft)
l.addAnchor(f, Qt.AnchorRight, g, Qt.AnchorRight)

scene.addItem(w)
scene.setBackgroundBrush(Qt.darkGreen)
view = QGraphicsView(scene)

view.show()
app.exec()
