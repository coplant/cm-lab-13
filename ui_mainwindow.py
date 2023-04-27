################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QComboBox,
                               QFrame, QHBoxLayout, QHeaderView, QMainWindow,
                               QMenu, QMenuBar, QSizePolicy, QTableWidget,
                               QTableWidgetItem, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(750, 433)
        MainWindow.setMinimumSize(QSize(750, 433))
        MainWindow.setMaximumSize(QSize(750, 1000))
        self.action_analyse_text = QAction(MainWindow)
        self.action_analyse_text.setObjectName(u"action_analyse_text")
        self.action_decrypt = QAction(MainWindow)
        self.action_decrypt.setObjectName(u"action_decrypt")
        self.action_open_freq = QAction(MainWindow)
        self.action_open_freq.setObjectName(u"action_open_freq")
        self.action_open_cipher = QAction(MainWindow)
        self.action_open_cipher.setObjectName(u"action_open_cipher")
        self.action_save_cipher = QAction(MainWindow)
        self.action_save_cipher.setObjectName(u"action_save_cipher")
        self.action_save_freq = QAction(MainWindow)
        self.action_save_freq.setObjectName(u"action_save_freq")
        self.action_clear = QAction(MainWindow)
        self.action_clear.setObjectName(u"action_clear")
        self.action_analyse_freq = QAction(MainWindow)
        self.action_analyse_freq.setObjectName(u"action_analyse_freq")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.plain_text = QTextEdit(self.centralwidget)
        self.plain_text.setObjectName(u"plain_text")
        self.plain_text.setGeometry(QRect(220, 10, 521, 191))
        self.plain_text.setInputMethodHints(Qt.ImhMultiLine)
        self.cipher_text = QTextEdit(self.centralwidget)
        self.cipher_text.setObjectName(u"cipher_text")
        self.cipher_text.setGeometry(QRect(220, 210, 521, 191))
        self.table_stats = QTableWidget(self.centralwidget)
        if (self.table_stats.columnCount() < 3):
            self.table_stats.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_stats.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_stats.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_stats.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.table_stats.setObjectName(u"table_stats")
        self.table_stats.setGeometry(QRect(10, 40, 201, 161))
        self.table_stats.setMouseTracking(True)
        self.table_stats.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.table_stats.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.table_stats.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_stats.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table_stats.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_stats.setSortingEnabled(True)
        self.table_stats.setColumnCount(3)
        self.table_stats.horizontalHeader().setProperty("showSortIndicator", False)
        self.table_stats.verticalHeader().setVisible(False)
        self.table_replace = QTableWidget(self.centralwidget)
        if (self.table_replace.columnCount() < 2):
            self.table_replace.setColumnCount(2)
        self.table_replace.setObjectName(u"table_replace")
        self.table_replace.setGeometry(QRect(10, 210, 201, 192))
        self.table_replace.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.table_replace.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.table_replace.setEditTriggers(QAbstractItemView.DoubleClicked)
        self.table_replace.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table_replace.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_replace.setColumnCount(2)
        self.table_replace.horizontalHeader().setVisible(False)
        self.table_replace.verticalHeader().setVisible(False)
        self.horizontalFrame = QFrame(self.centralwidget)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        self.horizontalFrame.setGeometry(QRect(-30, 360, 811, 291))
        self.horizontalLayout = QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.combo = QComboBox(self.centralwidget)
        self.combo.addItem("")
        self.combo.addItem("")
        self.combo.addItem("")
        self.combo.setObjectName(u"combo")
        self.combo.setGeometry(QRect(10, 10, 201, 21))
        MainWindow.setCentralWidget(self.centralwidget)
        self.horizontalFrame.raise_()
        self.plain_text.raise_()
        self.cipher_text.raise_()
        self.table_stats.raise_()
        self.table_replace.raise_()
        self.combo.raise_()
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 750, 21))
        self.menu_text = QMenu(self.menuBar)
        self.menu_text.setObjectName(u"menu_text")
        self.menu_frequency = QMenu(self.menuBar)
        self.menu_frequency.setObjectName(u"menu_frequency")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menu_text.menuAction())
        self.menuBar.addAction(self.menu_frequency.menuAction())
        self.menu_text.addAction(self.action_analyse_text)
        self.menu_text.addAction(self.action_decrypt)
        self.menu_text.addSeparator()
        self.menu_text.addAction(self.action_open_cipher)
        self.menu_text.addAction(self.action_save_cipher)
        self.menu_frequency.addAction(self.action_analyse_freq)
        self.menu_frequency.addAction(self.action_clear)
        self.menu_frequency.addSeparator()
        self.menu_frequency.addAction(self.action_open_freq)
        self.menu_frequency.addAction(self.action_save_freq)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow",
                                                             u"\u041b\u0430\u0431\u043e\u0440\u0430\u0442\u043e\u0440\u043d\u0430\u044f \u0440\u0430\u0431\u043e\u0442\u0430 13: \u0427\u0430\u0441\u0442\u043e\u0442\u043d\u044b\u0439 \u043a\u0440\u0438\u043f\u0442\u043e\u0430\u043d\u0430\u043b\u0438\u0437",
                                                             None))
        self.action_analyse_text.setText(QCoreApplication.translate("MainWindow",
                                                                    u"\u0410\u043d\u0430\u043b\u0438\u0437\u0438\u0440\u043e\u0432\u0430\u0442\u044c",
                                                                    None))
        self.action_decrypt.setText(QCoreApplication.translate("MainWindow",
                                                               u"\u0420\u0430\u0441\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u0442\u044c",
                                                               None))
        self.action_open_freq.setText(
            QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c", None))
        self.action_open_cipher.setText(
            QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c", None))
        self.action_save_cipher.setText(
            QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.action_save_freq.setText(
            QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.action_clear.setText(
            QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
        self.action_analyse_freq.setText(QCoreApplication.translate("MainWindow",
                                                                    u"\u0410\u043d\u0430\u043b\u0438\u0437\u0438\u0440\u043e\u0432\u0430\u0442\u044c",
                                                                    None))
        ___qtablewidgetitem = self.table_stats.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(
            QCoreApplication.translate("MainWindow", u"\u0421\u0438\u043c\u0432\u043e\u043b", None));
        ___qtablewidgetitem1 = self.table_stats.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(
            QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e",
                                       None));
        ___qtablewidgetitem2 = self.table_stats.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"%", None));
        self.combo.setItemText(0, QCoreApplication.translate("MainWindow",
                                                             u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c\u0441\u043a\u0438\u0439",
                                                             None))
        self.combo.setItemText(1,
                               QCoreApplication.translate("MainWindow", u"\u0420\u0443\u0441\u0441\u043a\u0438\u0439",
                                                          None))
        self.combo.setItemText(2, QCoreApplication.translate("MainWindow",
                                                             u"\u0410\u043d\u0433\u043b\u0438\u0439\u0441\u043a\u0438\u0439",
                                                             None))

        self.menu_text.setTitle(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043a\u0441\u0442", None))
        self.menu_frequency.setTitle(
            QCoreApplication.translate("MainWindow", u"\u0427\u0430\u0441\u0442\u043e\u0442\u0430", None))
    # retranslateUi

