import sys

from PyQt5 import QtWidgets
import view, time, os
from lib.parser import *
# pyuic5 view.ui -o view.py


class Parser(QtWidgets.QMainWindow, view.Ui_MainWindow):
    openedFile = ''
    targetDir = ''

    def start_parser(self):
        if not self.openedFile:
            self.state.setStyleSheet("QLabel {  color : red; }")
            self.state.setText('Ошибка: Не выбран исходный файл')
            return False

        if not self.targetDir:
            self.state.setStyleSheet("QLabel {  color : red; }")
            self.state.setText('Ошибка: Не выбрана целевая директория')
            return False

        self.state.setStyleSheet("QLabel {  color : green; }")
        self.state.setText('Запущен: страницы раскладываются по папкам...')
        QtWidgets.QApplication.processEvents()

        self.extract_text(self.openedFile, self.targetDir)

        self.state.setStyleSheet("QLabel {  color : green; }")
        self.state.setText('Запущен: объединение файлов пользователей...')
        QtWidgets.QApplication.processEvents()

        self.merge_user_files()

        self.state.setStyleSheet("QLabel {  color : green; }")
        self.state.setText('Завершено')
        QtWidgets.QApplication.processEvents()

    def merge_user_files(self):
        dirs = os.listdir(self.targetDir)
        for dir in dirs:
            info = "[merge] User Code is {0}".format(dir)
            print(info)
            self.textActive.append(info)
            QtWidgets.QApplication.processEvents()
            merge_files(self.targetDir+'/'+dir)

    def extract_text(self, pdf_path, target_path):
        i = 0
        errors = []
        fh = open(pdf_path, 'rb')
        for page in extract_text_by_page(fh):
            i += 1
            parse_result = parseText(page)
            if not parse_result:
                errors.append('In page {0} bad User code'.format(i))
                continue
            filepath = target_path + '/' + parse_result[0]
            if not os.path.exists(filepath):
                os.mkdir(filepath)
            info = "[{2}] User Code is {0}, Legal ID is {1}".format(parse_result[0], parse_result[1], i)
            print(info)
            self.textActive.append(info)
            QtWidgets.QApplication.processEvents()
            safeFile(pdf_path, i-1, filepath + '/' + parse_result[1] + '.pdf')

        if len(errors) > 0:
            for err in errors:
                self.textActive.append('[ERROR] '+err)
                QtWidgets.QApplication.processEvents()

        self.textActive.append('[DONE] {0} pages parsed, {1} errors'.format(i, len(errors)))
        QtWidgets.QApplication.processEvents()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.outFileButton.clicked.connect(self.browse_folder_file)
        self.targetDirButton.clicked.connect(self.browse_folder_target)
        self.startParserButton.clicked.connect(self.start_parser)
        self.closeApp.clicked.connect(self.stop_end_close)

    def browse_folder_file(self):
        self.outputFIle.clear()  # На случай, если в текстовом поле что то есть
        file = QtWidgets.QFileDialog.getOpenFileName(self, "Выберите файл", "/home", "Text files (*.pdf)")
        # открыть диалог выбора файлв и установить значение переменной
        # равной пути к выбранной директории

        if file:
            self.openedFile = file[0]
            print("[i] Opened file is ", self.openedFile)
            self.outputFIle.setText(self.openedFile)

    def browse_folder_target(self):
        self.targetDirLine.clear()  # На случай, если в текстовом поле что то есть
        folder = QtWidgets.QFileDialog.getExistingDirectory(self,
                                                            "Выберите папку, в которую будут попадать файлы", "/home",
                                                            QtWidgets.QFileDialog.ShowDirsOnly)
        # открыть диалог выбора директории и установить значение переменной
        # равной пути к выбранной директории

        if folder:
            self.targetDir = folder
            print("[i] Opened file is ", self.targetDir)
            self.targetDirLine.setText(self.targetDir)

    def stop_end_close(self):
        self.close
        sys.exit(0)

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = Parser()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()