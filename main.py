import sys
from PySide6 import QtWidgets, QtCore
from PySide6.QtGui import QKeySequence, QShortcut
from window_generated import Ui_MainWindow
import deepl

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    toggle_visibility = QtCore.Signal()

    def __init__(self, w_hotkey='alt+k', r_hotkey='Ctrl+Return', adapter=None):
        super().__init__()
        self.setupUi(self)

        self.adapter = adapter

        self.btn_trans.clicked.connect(self.translate)
        self.btn_flip.clicked.connect(self.switch)

        self.s_update = QShortcut(QKeySequence(r_hotkey), self) # Ctrl+Enter -> Ctrl+Return
        self.s_update.activated.connect(self.translate)

        self.toggle_visibility.connect(self.flip_window)
        self.hotkey_thread = HotkeyThread(w_hotkey, self.toggle_visibility)
        self.hotkey_thread.start()

    def translate(self):
        text = self.from_trans.toPlainText()
        if len(text) > 0:
            s_lang = self.lang_select.currentText()
            if s_lang == 'English':
                lang = "EN-US"
            if s_lang == 'Russian':
                lang = "RU"
            self.btn_trans.setEnabled(False)
            self.translation_thread = TranslationThread(self.adapter, text, lang)
            self.translation_thread.translation_finished.connect(self.update_translation_result)
            self.translation_thread.start()

    def update_translation_result(self, result):
        self.btn_trans.setEnabled(True)
        self.to_trans.setPlainText(result)

    def switch(self):
        p1 = self.from_trans.toPlainText()
        p2 = self.to_trans.toPlainText()
        self.from_trans.setPlainText(p2)
        self.to_trans.setPlainText(p1)

        f = self.lang_select.currentIndex()
        self.lang_select.setCurrentIndex(1 - f)


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


class TranslationThread(QtCore.QThread):
    translation_finished = QtCore.Signal(str)

    def __init__(self, adapter, text, target_lang):
        super().__init__()
        self.adapter = adapter
        self.text = text
        self.target_lang = target_lang

    def run(self):
        try:
            result = self.adapter.translate(self.text, self.target_lang)
            self.translation_finished.emit(result)
        except deepl.exceptions.AuthorizationException as e:
            print("Authorization error: API key is invalid")
            self.translation_finished.emit("Authorization error: API key is invalid")


class DeepLAdapter:
    def __init__(self, auth_key):
        self.auth_key = auth_key
        self.deepl_client = deepl.Translator(self.auth_key)

    def translate(self, text, target_lang):
        result = self.deepl_client.translate_text(text, target_lang=target_lang)
        return result.text


def get_secret():
    with open(".secrets", "r") as f:
        return f.read()

class Config:
    window_hide_hotkey = ''
    translate_hotkey = ''
    deepl_api = ''

    def __init__(self):
        pass
    
    def parse(self, rec):
        for line in rec.splitlines():
            if line.startswith('#'):
                continue
            k, v = line.split('=')
            if k == 'window_hide_hotkey':
                self.window_hide_hotkey = v
            elif k == 'translate_hotkey':
                self.translate_hotkey = v
            elif k == 'deepl_api':
                self.deepl_api = v
            else:
                raise ValueError(f"Unknown config key: {k}")


class Translator:
    def __init__(self):
        pass

    def run(self):
        app = QtWidgets.QApplication(sys.argv)
        try:
            with open("something.config", "r") as f:
                config = Config()
                config.parse(f.read())
        except FileNotFoundError:
            print("Config file (something.config) not found")
            QtWidgets.QMessageBox.critical(None,'Config Error!',"Config file (something.config) not found", QtWidgets.QMessageBox.Abort)
            return
        window = MainWindow(config.window_hide_hotkey, config.translate_hotkey, DeepLAdapter(config.deepl_api))
        window.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        window.show()
        sys.exit(app.exec())

t = Translator()
t.run()