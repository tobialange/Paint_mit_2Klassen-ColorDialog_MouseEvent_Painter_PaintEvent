from PySide6.QtWidgets import QMainWindow, QMenuBar
from DrawWidget import DrawWidget

class MyMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.draw_widget = DrawWidget(self)

        # See https://doc.qt.io/qtforpython/PySide6/QtWidgets/QMenuBar.html?highlight=qmenubar
        # for None parent
        self.menu_bar = QMenuBar(None)

        self.fileMenu = self.menu_bar.addMenu("Bilder")
        self.action_load_file = self.fileMenu.addAction("Bild öffnen", self.draw_widget.load_file)
        self.action_save_file = self.fileMenu.addAction("Bild speichern", self.draw_widget.save_file)

        self.fileMenu.addAction("Farbe", self.draw_widget.setColor)

        self.setMenuBar(self.menu_bar)
        self.setWindowTitle("M$ P41nt")
        self.setCentralWidget(self.draw_widget)
