from PySide6 import QtCore, QtWidgets, QtGui
import functions

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.button = QtWidgets.QPushButton("Click me!")
        self.text = QtWidgets.QLabel("",
                                     alignment=QtCore.Qt.AlignCenter)
        #self.input = QtWidgets.QLineEdit("", alignment=QtCore.Qt.AlignCenter)
        #self.label = QtWidgets.QLabel("filename:")
        self.edit = QtWidgets.QTextEdit()
        self.edit.setText(functions.read_file("this.txt"))

        self.layout = QtWidgets.QVBoxLayout(self)
        #self.layout.addWidget(self.text)
        self.layout.addWidget(self.edit)
        #self.formLayout = QtWidgets.QHBoxLayout()
        #self.formLayout.addWidget(self.label)
        #self.formLayout.addWidget(self.input)
        #self.layout.addLayout(self.formLayout)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        self.text.setText("yay")
        functions.save("this.txt", self.edit.toPlainText())
        functions.do_thing("this.txt")

