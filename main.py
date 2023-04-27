import string
from enum import Enum

from PySide6.QtCore import QModelIndex
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from ui_mainwindow import Ui_MainWindow


class Application(QMainWindow):
    class Language(Enum):
        USER = 0
        RUSSIAN = 1
        ENGLISH = 2

    class Action(Enum):
        ENCRYPT = -1
        DECRYPT = 1

    def __init__(self):
        super(Application, self).__init__()
        self.data = None
        self.cipher_data = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

        self.ui.btn_enc.setChecked(True)

        self.en_abc = "abcdefghijklmnopqrstuvwxyz"
        self.ru_abc = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

        self.ui.combo.view().pressed.connect(lambda x: self.handle_language(x.row()))
        self.ui.proc_button.clicked.connect(self.process_data)
        self.ui.open_file.triggered.connect(self.open)
        self.ui.save_file.triggered.connect(self.save)

    def handle_language(self, x):
        if x == self.Language.RUSSIAN.value:
            self.ui.line_outer.setText(self.ru_abc.upper())
            self.ui.line_inner.setText(self.ru_abc.upper())
        elif x == self.Language.ENGLISH.value:
            self.ui.line_outer.setText(self.en_abc.upper())
            self.ui.line_inner.setText(self.en_abc.upper())

    def process_data(self):
        ...

    def open(self):
        file_name = QFileDialog.getOpenFileName(self, "Открыть файл", ".", "All Files (*)")
        if file_name[0]:
            with open(file_name[0], "r") as file:
                self.data = file.read()
                self.ui.plain_text.setText(self.data)
        else:
            QMessageBox.information(self, "Ошибка", "Файл не выбран", QMessageBox.Ok)

    def save(self):
        file_name = QFileDialog.getSaveFileName(self, "Сохранить файл", ".", "All Files (*)")
        if file_name[0]:
            with open(file_name[0], "w") as file:
                file.write(self.ui.cipher_text.toPlainText())
        else:
            QMessageBox.information(self, "Ошибка", "Файл не выбран", QMessageBox.Ok)


if __name__ == "__main__":
    app = QApplication()
    window = Application()
    app.exec()
