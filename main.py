import os
import sys
from PySide6 import QtWidgets, QtCore
from PySide6.QtGui import QKeySequence, QShortcut
from window_generated import Ui_MainWindow
import keyboard
import provider
import deepl
import googletrans

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    toggle_visibility = QtCore.Signal()
    last_lang = ''

    def __init__(self, w_hotkey='alt+k', r_hotkey='Ctrl+Return', adapter=None, langs=['en']):
        super().__init__()
        self.setupUi(self)

        self.adapter = adapter
        self.last_lang = 'en'
        self.lang_select.addItems(langs)
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
            lang = self.lang_select.currentText()
            self.btn_trans.setEnabled(False)
            self.translation_thread = TranslationThread(self.adapter, text, lang)
            self.translation_thread.translation_finished.connect(self.update_translation_result)
            self.translation_thread.start()

    def update_translation_result(self, lang, result):
        self.btn_trans.setEnabled(True)
        self.last_lang = lang.lower()
        self.to_trans.setPlainText(result)

    def switch(self):
        p1 = self.from_trans.toPlainText()
        p2 = self.to_trans.toPlainText()
        self.from_trans.setPlainText(p2)
        self.to_trans.setPlainText(p1)

        f = self.lang_select.currentIndex()
        self.lang_select.setCurrentText(self.last_lang.lower())


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
        keyboard.add_hotkey(self.hotkey, self.emit_signal)

    def emit_signal(self):
        self.signal.emit()

    def stop(self):
        pass


class TranslationThread(QtCore.QThread):
    translation_finished = QtCore.Signal(str, str)

    def __init__(self, adapter, text, target_lang):
        super().__init__()
        self.adapter = adapter
        self.text = text
        self.target_lang = target_lang

    def run(self):
        try:
            lang, result = self.adapter.translate(self.text, self.target_lang)
            self.translation_finished.emit(lang, result)
        except Exception as e:
            if type(e) == deepl.exceptions.AuthorizationException:
                print("[DEEPL] Authorization error: API key is invalid")
                self.translation_finished.emit("en", "[DEEPL] Authorization error: API key is invalid")
            elif type(e) == deepl.exceptions.DeepLException:
                print("[DEEPL] This language is not supported")
                self.translation_finished.emit("en", "[DEEPL] This language is not supported")

            else:
                print(e)
                self.translation_finished.emit(str(e))


class Config:
    window_hide_hotkey = ''
    translate_hotkey = ''
    deepl_api_key = ''
    google_api_key = ''
    api = ''
    languages = []
    
    def parse(self, rec):
        for line in rec.splitlines():
            if line.startswith('#'):
                continue
            k, v = line.split('=')
            if k == 'window_hide_hotkey':
                self.window_hide_hotkey = v
            elif k == 'translate_hotkey':
                self.translate_hotkey = v
            elif k == 'deepl_api_key':
                self.deepl_api_key = v
            elif k == 'google_api_key':
                self.google_api_key = v
            elif k == 'api':
                self.api = v
            elif k == 'languages':
                self.languages = v.split(',')
            else:
                raise ValueError(f"Unknown config key: {k}")


class Translator:
    def run(self):
        app = QtWidgets.QApplication(sys.argv)
        """have mercy"""
        try:
            with open("trans.config", "r", encoding="utf-8") as f:
                config = Config()
                config.parse(f.read())
        except Exception as e:
            if type(e) == ValueError:
                self.invalid_config()
                return
            if type(e) == FileNotFoundError:
                try:
                    a = os.getenv('APPDATA')
                    with open(a + "/trans.config", "r", encoding="utf-8") as f:
                        config = Config()
                        config.parse(f.read())
                except Exception as e:
                    if type(e) == FileNotFoundError:
                        self.file_not_found()
                    if type(e) == ValueError:
                        self.invalid_config()
                    return

        adapter = None
        if config.api == 'deepl':
            adapter = provider.DeepLProvider(config.deepl_api_key)
        elif config.api == 'google':
            adapter = provider.GoogleProvider()

        window = MainWindow(config.window_hide_hotkey, config.translate_hotkey, adapter, config.languages)
        window.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        window.show()
        sys.exit(app.exec())

    def file_not_found(self):
        print("Config file (trans.config) not found")
        QtWidgets.QMessageBox.critical(None,'Config Error!',"Config file (trans.config) not found", QtWidgets.QMessageBox.Abort)
    
    def invalid_config(self):
        print("Invalid config file (trans.config)")
        QtWidgets.QMessageBox.critical(None,'Config Error!',"Config file (trans.config) is invalid", QtWidgets.QMessageBox.Abort)

t = Translator()
t.run()
