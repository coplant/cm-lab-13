import string
from enum import Enum

from PySide6.QtCore import QModelIndex
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem
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
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

        self.data = None
        self.frequency = None
        self.num = "0123456789"
        self.en_abc = {
            "a": 0.0796, "b": 0.0160, "c": 0.0284, "d": 0.0401, "e": 0.1286,
            "f": 0.0262, "g": 0.0199, "h": 0.0539, "i": 0.0777, "j": 0.0016,
            "k": 0.0041, "l": 0.0351, "m": 0.0243, "n": 0.0751, "o": 0.0662,
            "p": 0.0181, "q": 0.0017, "r": 0.0683, "s": 0.0662, "t": 0.0972,
            "u": 0.0248, "v": 0.0115, "w": 0.0180, "x": 0.0017, "y": 0.0152,
            "z": 0.0005
        }
        self.ru_abc = {
            "а": 0.07998, "б": 0.01592, "в": 0.04533, "г": 0.01687, "д": 0.02977,
            "е": 0.08483, "ё": 0.00013, "ж": 0.0094, "з": 0.01641, "и": 0.07367,
            "й": 0.01208, "к": 0.03486, "л": 0.04343, "м": 0.03203, "н": 0.067,
            "о": 0.10983, "п": 0.02804, "р": 0.04746, "с": 0.05473, "т": 0.06318,
            "у": 0.02615, "ф": 0.00267, "х": 0.00966, "ц": 0.00486, "ч": 0.0145,
            "ш": 0.00718, "щ": 0.00361, "ъ": 0.00037, "ы": 0.01898, "ь": 0.01735,
            "э": 0.00331, "ю": 0.00639, "я": 0.02001
        }

        self.ui.combo.view().pressed.connect(lambda x: self.handle_language(x.row()))
        # self.ui.proc_button.clicked.connect(self.process_data)
        # self.ui.open_file.triggered.connect(self.open)
        # self.ui.save_file.triggered.connect(self.save)

    def handle_language(self, x):
        if x == self.Language.RUSSIAN.value:
            self.frequency = {k: v for k, v in sorted(self.ru_abc.items(), key=lambda item: item[1], reverse=True)}
            self.ui.table_replace.setRowCount(len(self.ru_abc))
            for i in range(len(self.ru_abc)):
                letter, frequency = list(self.frequency.items())[i]
                self.ui.table_replace.setItem(i, 1, QTableWidgetItem(f"{letter.upper()} - {frequency}"))
        elif x == self.Language.ENGLISH.value:
            self.frequency = {k: v for k, v in sorted(self.en_abc.items(), key=lambda item: item[1], reverse=True)}
            self.ui.table_replace.setRowCount(len(self.en_abc))
            for i in range(len(self.en_abc)):
                letter, frequency = list(self.frequency.items())[i]
                self.ui.table_replace.setItem(i, 1, QTableWidgetItem(f"{letter.upper()} - {frequency}"))
        elif x == self.Language.USER.value:
            # self.ui.table_replace.clear()
            self.frequency = {}
            ...

    def clear(self):
        # is_decrypted = False
        self.ui.table_stats.clearContents()
        self.ui.table_stats.setRowCount(0)
        self.ui.table_replace.clearContents()
        self.ui.table_replace.setRowCount(0)

    def process_data(self):
        self.clear()

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