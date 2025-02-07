# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QMainWindow,
    QMenu, QMenuBar, QPlainTextEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(739, 246)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.actionGoogle = QAction(MainWindow)
        self.actionGoogle.setObjectName(u"actionGoogle")
        self.actionDeepL = QAction(MainWindow)
        self.actionDeepL.setObjectName(u"actionDeepL")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 10, 711, 191))
        self.h_grid = QHBoxLayout(self.horizontalLayoutWidget)
        self.h_grid.setObjectName(u"h_grid")
        self.h_grid.setContentsMargins(0, 0, 0, 0)
        self.textboxes_grid = QVBoxLayout()
        self.textboxes_grid.setObjectName(u"textboxes_grid")
        self.from_trans = QPlainTextEdit(self.horizontalLayoutWidget)
        self.from_trans.setObjectName(u"from_trans")

        self.textboxes_grid.addWidget(self.from_trans)

        self.to_trans = QPlainTextEdit(self.horizontalLayoutWidget)
        self.to_trans.setObjectName(u"to_trans")

        self.textboxes_grid.addWidget(self.to_trans)


        self.h_grid.addLayout(self.textboxes_grid)

        self.buttons_grid = QVBoxLayout()
        self.buttons_grid.setObjectName(u"buttons_grid")
        self.btn_trans = QPushButton(self.horizontalLayoutWidget)
        self.btn_trans.setObjectName(u"btn_trans")

        self.buttons_grid.addWidget(self.btn_trans)

        self.btn_flip = QPushButton(self.horizontalLayoutWidget)
        self.btn_flip.setObjectName(u"btn_flip")

        self.buttons_grid.addWidget(self.btn_flip)

        self.lang_select = QComboBox(self.horizontalLayoutWidget)
        self.lang_select.addItem("")
        self.lang_select.addItem("")
        self.lang_select.setObjectName(u"lang_select")

        self.buttons_grid.addWidget(self.lang_select)


        self.h_grid.addLayout(self.buttons_grid)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 739, 22))
        self.menutest = QMenu(self.menubar)
        self.menutest.setObjectName(u"menutest")
        self.menuProvider = QMenu(self.menutest)
        self.menuProvider.setObjectName(u"menuProvider")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menutest.menuAction())
        self.menutest.addAction(self.menuProvider.menuAction())
        self.menuProvider.addAction(self.actionGoogle)
        self.menuProvider.addAction(self.actionDeepL)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionGoogle.setText(QCoreApplication.translate("MainWindow", u"Google", None))
        self.actionDeepL.setText(QCoreApplication.translate("MainWindow", u"DeepL", None))
        self.btn_trans.setText(QCoreApplication.translate("MainWindow", u"Translate", None))
        self.btn_flip.setText(QCoreApplication.translate("MainWindow", u"Flip", None))
        self.lang_select.setItemText(0, QCoreApplication.translate("MainWindow", u"English", None))
        self.lang_select.setItemText(1, QCoreApplication.translate("MainWindow", u"Russian", None))

        self.menutest.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.menuProvider.setTitle(QCoreApplication.translate("MainWindow", u"Provider", None))
    # retranslateUi

