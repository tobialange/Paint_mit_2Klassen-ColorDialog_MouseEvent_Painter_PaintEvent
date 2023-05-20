from PySide6.QtCore import QPoint, Slot
from PySide6.QtWidgets import QLabel, QColorDialog, QFileDialog
from PySide6.QtGui import QMouseEvent, QPainter, QPaintEvent, QPixmap, QColor, QImage


class DrawWidget(QLabel):
    setColor = Slot()
    loadFile = Slot()
    save_file = Slot()

    def __init__(self, parent):
        super(DrawWidget, self).__init__(parent)

        self.pos = None
        self.color = QColor("green")
        self.pixmap_from_image = None

    def setColor(self):
        selected_color = QColorDialog.getColor(self.color, self, "Farbe wählen")

        if selected_color.isValid():
            self.color = selected_color

    def mousePressEvent(self, ev: QMouseEvent) -> None:
        self.pos = ev.pos()

        self.update()

    def paintEvent(self, ev: QPaintEvent) -> None:
        painter = QPainter(self)

        if self.pixmap_from_image:
            painter.drawPixmap(QPoint(1, 1), self.pixmap_from_image)

        if self.pos:
            painter.setPen(self.color)
            painter.drawEllipse(self.pos, 20, 20)

        painter.end()

    def load_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Bild auswählen", "Bilder (*.png, *.jpg)")

        if file_name:
            self.image = QImage(file_name)
            self.pixmap_from_image = QPixmap(self.image)

            self.update()

    def save_file(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Bild speichern", "./", "Bilder (*.png, *.jpg)")

        if file_name:
            print(self.picture().size())
            my_pixmap = QPixmap(self.pixmap())
            print(my_pixmap.size())
            my_image = my_pixmap.toImage()

            if my_image.save(file_name):
                print("Success")
