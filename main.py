import sys
from PySide6 import QtWidgets, QtCore
from window import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    toggle_visibility = QtCore.Signal()

    def __init__(self, hotkey='alt+k'):
        super().__init__()
        self.setupUi(self)
        
        self.btn_trans.clicked.connect(self.translate)
        self.btn_flip.clicked.connect(self.switch)
        
        self.toggle_visibility.connect(self.flip_window)
        
        self.hotkey_thread = HotkeyThread(hotkey, self.toggle_visibility)
        self.hotkey_thread.start()

    def translate(self):
        self.to_trans.setPlainText("DEBUG: " + self.from_trans.toPlainText())
    
    def switch(self):
        p1 = self.from_trans.toPlainText()
        p2 = self.to_trans.toPlainText()
        self.from_trans.setPlainText(p2)
        self.to_trans.setPlainText(p1)

    def flip_window(self):
        if self.isVisible():
            self.hide()
        else:
            self.show()
            self.activateWindow()
            a = self.from_trans.toPlainText()
            if len(a) > 0:
                self.from_trans.setPlainText(a[:-1])


    def closeEvent(self, event):
        self.hotkey_thread.stop()
        super().closeEvent(event)

class HotkeyThread(QtCore.QThread):
    def __init__(self, hotkey, signal):
        super().__init__()
        self.hotkey = hotkey
        self.signal = signal

    def run(self):
        import keyboard
        keyboard.add_hotkey(self.hotkey, self.emit_signal)

    def emit_signal(self):
        self.signal.emit()

    def stop(self):
        pass

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    window.show()
    sys.exit(app.exec())