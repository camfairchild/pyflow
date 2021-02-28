import sys

from PySide6 import QtCore, QtGui, QtWidgets

from widgets import MyWidget

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec_())
