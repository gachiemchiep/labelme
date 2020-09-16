from python_qt_binding.QtCore import Qt
from python_qt_binding import QtWidgets


class EscapableQListWidget(QtWidgets.QListWidget):
    def keyPressEvent(self, event):
        super(EscapableQListWidget, self).keyPressEvent(event)
        if event.key() == Qt.Key_Escape:
            self.clearSelection()
