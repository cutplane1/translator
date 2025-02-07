import sys, keyboard
from PySide6 import QtWidgets
from PySide6.QtGui import QKeySequence, QShortcut

from window import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btn_trans.clicked.connect(self.translate)
        self.btn_flip.clicked.connect(self.switch)

    def translate(self):
        self.to_trans.setPlainText("DEBUG: " + self.from_trans.toPlainText())
    
    def switch(self):
        p1 = self.from_trans.toPlainText()
        p2 = self.to_trans.toPlainText()
        self.from_trans.setPlainText(p2)
        self.to_trans.setPlainText(p1)


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()

is_hidden = False
def flip_window():
    global is_hidden
    if is_hidden:
        window.show()
        is_hidden = False
    else:
        window.hide()
        is_hidden = True

keyboard.add_hotkey("alt+k", flip_window)

window.show()
app.exec()
