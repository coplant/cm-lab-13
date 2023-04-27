import pickle
from enum import Enum

from PySide6 import QtCharts, QtCore
from PySide6.QtGui import QPainter, QBrush, QColor
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem
from ui_mainwindow import Ui_MainWindow


class Application(QMainWindow):
    class Language(Enum):
        RUSSIAN = 0
        ENGLISH = 1

    class Action(Enum):
        ENCRYPT = -1
        DECRYPT = 1

    def __init__(self):
        super(Application, self).__init__()
        self.is_decrypted = False
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

        self.data = None
        self.frequency = {}
        self.text_frequency = {}
        self.ru = "абвгдеёжзийклмнопрстуфхцчщшъыьэюя"
        self.en = "abcdefghijklmnopqrstuvwxyz"
        self.num = "0123456789"
        self.ru_abc = {
            "а": 0.07998, "б": 0.01592, "в": 0.04533, "г": 0.01687, "д": 0.02977,
            "е": 0.08483, "ё": 0.00013, "ж": 0.0094, "з": 0.01641, "и": 0.07367,
            "й": 0.01208, "к": 0.03486, "л": 0.04343, "м": 0.03203, "н": 0.067,
            "о": 0.10983, "п": 0.02804, "р": 0.04746, "с": 0.05473, "т": 0.06318,
            "у": 0.02615, "ф": 0.00267, "х": 0.00966, "ц": 0.00486, "ч": 0.0145,
            "ш": 0.00718, "щ": 0.00361, "ъ": 0.00037, "ы": 0.01898, "ь": 0.01735,
            "э": 0.00331, "ю": 0.00639, "я": 0.02001
        }
        self.en_abc = {
            "a": 0.0796, "b": 0.0160, "c": 0.0284, "d": 0.0401, "e": 0.1286,
            "f": 0.0262, "g": 0.0199, "h": 0.0539, "i": 0.0777, "j": 0.0016,
            "k": 0.0041, "l": 0.0351, "m": 0.0243, "n": 0.0751, "o": 0.0662,
            "p": 0.0181, "q": 0.0017, "r": 0.0683, "s": 0.0662, "t": 0.0972,
            "u": 0.0248, "v": 0.0115, "w": 0.0180, "x": 0.0017, "y": 0.0152,
            "z": 0.0005
        }
        self.abc = [self.ru_abc, self.en_abc]
        self.ui.combo.view().pressed.connect(lambda x: self.handle_language(x.row()))
        self.ui.table_replace.cellChanged.connect(self.handle_replace)
        self.ui.action_decrypt.triggered.connect(self.decrypt_text)
        self.ui.action_analyse_text.triggered.connect(self.analyze_ciphertext)
        self.ui.action_analyse_freq.triggered.connect(self.analyze_plaintext)

        self.ui.action_clear.triggered.connect(self.clear)

        self.ui.action_open_cipher.triggered.connect(self.open_text)
        self.ui.action_save_cipher.triggered.connect(self.save_text)
        self.ui.action_open_freq.triggered.connect(self.open_frequency)
        self.ui.action_save_freq.triggered.connect(self.save_frequency)

        self.handle_language(self.ui.combo.currentIndex())

    def handle_replace(self, row, column):
        if self.is_decrypted:
            print(row, column)

    def set_text_frequency(self, choice):
        self.ui.table_stats.setRowCount(len(self.abc[choice]))
        index = 0
        for i in range(len(self.text_frequency.items())):
            text_frequency = list(self.text_frequency.items())
            if text_frequency[i][0].lower() in self.abc[choice].keys():
                letter = text_frequency[i][0]
                count, frequency = text_frequency[i][1]
                self.ui.table_stats.setItem(index, 0, QTableWidgetItem(letter.upper()))
                self.ui.table_stats.setItem(index, 1, QTableWidgetItem(f"{count}"))
                self.ui.table_stats.setItem(index, 2, QTableWidgetItem(f"{frequency * 100:g}"))
                self.ui.table_replace.setItem(index, 0, QTableWidgetItem(f"{letter.upper()} - {frequency * 100:g}"))
                index += 1
        self.ui.table_stats.resizeColumnsToContents()

    def set_frequency(self, choice):
        self.ui.table_replace.setRowCount(len(self.abc[choice]))
        index = 0
        for i in range(len(self.frequency)):
            text_frequency = list(self.frequency.items())
            if text_frequency[i][0].lower() in self.abc[choice].keys():
                letter, frequency = list(self.frequency.items())[i]
                self.ui.table_replace.setItem(index, 1, QTableWidgetItem(f"{letter.upper()} - {frequency * 100:g}"))
                index += 1

    def handle_language(self, x):
        ru_abc = {k: v for k, v in sorted(self.ru_abc.items(), key=lambda item: item[1], reverse=True)}
        en_abc = {k: v for k, v in sorted(self.en_abc.items(), key=lambda item: item[1], reverse=True)}
        if x == self.Language.RUSSIAN.value:
            if not self.frequency or self.frequency == en_abc:
                self.frequency = ru_abc
        elif x == self.Language.ENGLISH.value:
            if not self.frequency or self.frequency == ru_abc:
                self.frequency = en_abc
        self.set_frequency(x)
        if self.text_frequency:
            self.set_text_frequency(x)

    def decrypt_text(self):
        text = self.ui.plain_text.toPlainText()
        size = self.ui.table_replace.rowCount()
        replace = {}
        decrypted = ""
        for i in range(size):
            replace[self.ui.table_replace.item(i, 0).text()[0].lower()] = self.ui.table_replace.item(i, 1).text()[
                0].lower()
        for char in text:
            to_add = replace.get(char.lower(), char)
            if char.isupper():
                to_add = to_add.upper()
            decrypted += to_add
        self.ui.cipher_text.setText(decrypted)
        self.is_decrypted = True

    def clear(self):
        self.ui.table_stats.clearContents()
        self.ui.table_stats.setRowCount(0)
        self.ui.table_replace.clearContents()
        self.ui.table_replace.setRowCount(0)
        self.frequency = {}
        self.text_frequency = {}
        self.is_decrypted = False

    def draw_chart(self, choice):
        # построение гистограммы
        if not self.frequency:
            return QMessageBox.information(self, "Ошибка", "Некорректные значения частот")
        layout = self.ui.horizontalLayout.takeAt(0)
        if layout:
            layout.widget().deleteLater()
        self.setFixedHeight(650)
        axis_x = QtCharts.QBarCategoryAxis()
        axis_y = QtCharts.QValueAxis()
        series = QtCharts.QBarSeries()
        practical = QtCharts.QBarSet("Текущее")
        practical.setColor(QColor(163, 74, 236, 255))
        practical.setBorderColor(QColor(255, 255, 255, 255))
        theory = QtCharts.QBarSet("Ожидаемое")
        theory.setColor(QColor(98, 235, 56, 255))
        for i in self.abc[choice]:
            axis_x.append(i.upper())
            practical.append(self.text_frequency.get(i)[1])
            theory.append(self.frequency.get(i))
        series.append(practical)
        series.append(theory)
        chart = QtCharts.QChart()
        chart.addAxis(axis_x, QtCore.Qt.AlignmentFlag.AlignBottom)
        chart.addSeries(series)
        max_value_freq = max(self.frequency.items(), key=lambda x: x[1])[1]
        max_value_text = max(self.text_frequency.items(), key=lambda x: x[1][1])[1][1]
        axis_y.setRange(0, max(max_value_freq, max_value_text))
        chart.addAxis(axis_y, QtCore.Qt.AlignmentFlag.AlignLeft)
        series.attachAxis(axis_y)
        chart_view = QtCharts.QChartView(chart)
        chart_view.setRenderHint(QPainter.Antialiasing)
        chart_view.chart().setBackgroundBrush(QBrush(QColor(0, 0, 0, 0)))
        self.ui.horizontalLayout.addWidget(chart_view)

    def analyze_ciphertext(self):
        # анализируем шифротекст, получаем вероятности
        self.ui.table_stats.clearContents()
        self.ui.table_stats.setRowCount(0)
        self.text_frequency = {}
        text = self.ui.plain_text.toPlainText().lower().replace("\n", "").replace("\r", "").replace(" ", "")
        if not text:
            return QMessageBox.information(self, "Ошибка", "Текст не найден")
        for abc in self.abc:
            for char in abc:
                self.text_frequency[char] = (text.count(char), text.count(char) / len(text))
        self.text_frequency = {k: v for k, v in
                               sorted(self.text_frequency.items(), key=lambda item: item[1][1], reverse=True)}
        self.set_text_frequency(self.ui.combo.currentIndex())
        if self.frequency:
            self.set_frequency(self.ui.combo.currentIndex())
        self.draw_chart(self.ui.combo.currentIndex())

    def analyze_plaintext(self):
        # анализируем открытый, получаем вероятности символов для каждого автора
        self.ui.table_replace.clearContents()
        self.ui.table_replace.setRowCount(0)
        self.frequency = {}
        text = self.ui.plain_text.toPlainText().lower().replace("\n", "").replace("\r", "").replace(" ", "")
        if not text:
            return QMessageBox.information(self, "Ошибка", "Текст не найден")
        for abc in self.abc:
            for char in abc:
                self.frequency[char] = text.count(char) / len(text)
        self.frequency = {k: v for k, v in sorted(self.frequency.items(), key=lambda item: item[1], reverse=True)}
        self.set_frequency(self.ui.combo.currentIndex())
        if self.text_frequency:
            self.set_text_frequency(self.ui.combo.currentIndex())

    def open_text(self):
        file_name = QFileDialog.getOpenFileName(self, "Открыть файл", ".", "All Files (*)")
        if file_name[0]:
            self.is_decrypted = False
            with open(file_name[0], "r", encoding="utf-8") as file:
                self.data = file.read()
                self.ui.plain_text.setText(self.data)
        else:
            QMessageBox.information(self, "Ошибка", "Файл не выбран")

    def save_text(self):
        file_name = QFileDialog.getSaveFileName(self, "Сохранить файл", ".", "All Files (*)")
        if file_name[0]:
            with open(file_name[0], "w") as file:
                file.write(self.ui.cipher_text.toPlainText())
        else:
            QMessageBox.information(self, "Ошибка", "Файл не выбран")

    def open_frequency(self):
        file_name = QFileDialog.getOpenFileName(self, "Открыть файл", ".", "All Files (*)")
        if file_name[0]:
            self.clear()
            with open(file_name[0], "rb") as file:
                self.frequency = pickle.load(file)
                self.set_frequency(self.ui.combo.currentIndex())
        else:
            QMessageBox.information(self, "Ошибка", "Файл не выбран")

    def save_frequency(self):
        file_name = QFileDialog.getSaveFileName(self, "Сохранить файл", ".", "All Files (*)")
        if file_name[0]:
            with open(file_name[0], "wb") as file:
                pickle.dump(self.frequency, file)
        else:
            QMessageBox.information(self, "Ошибка", "Файл не выбран")


if __name__ == "__main__":
    app = QApplication()
    window = Application()
    app.exec()
