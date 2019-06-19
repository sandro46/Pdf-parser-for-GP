# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(449, 464)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(370, 540, 88, 34))
        self.pushButton.setObjectName("pushButton")
        self.outputFIle = QtWidgets.QLineEdit(self.centralwidget)
        self.outputFIle.setGeometry(QtCore.QRect(10, 60, 371, 32))
        self.outputFIle.setObjectName("outputFIle")
        self.outFileButton = QtWidgets.QToolButton(self.centralwidget)
        self.outFileButton.setGeometry(QtCore.QRect(390, 60, 33, 31))
        self.outFileButton.setObjectName("outFileButton")
        self.closeApp = QtWidgets.QPushButton(self.centralwidget)
        self.closeApp.setGeometry(QtCore.QRect(330, 370, 88, 34))
        self.closeApp.setObjectName("closeApp")
        self.startParserButton = QtWidgets.QPushButton(self.centralwidget)
        self.startParserButton.setGeometry(QtCore.QRect(230, 370, 88, 34))
        self.startParserButton.setObjectName("startParserButton")
        self.targetDirLine = QtWidgets.QLineEdit(self.centralwidget)
        self.targetDirLine.setGeometry(QtCore.QRect(10, 110, 371, 32))
        self.targetDirLine.setObjectName("targetDirLine")
        self.targetDirButton = QtWidgets.QToolButton(self.centralwidget)
        self.targetDirButton.setGeometry(QtCore.QRect(390, 110, 33, 31))
        self.targetDirButton.setObjectName("targetDirButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 40, 111, 18))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 141, 18))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 61, 18))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.state = QtWidgets.QLabel(self.centralwidget)
        self.state.setGeometry(QtCore.QRect(80, 10, 361, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.state.setFont(font)
        self.state.setStyleSheet("color : green;")
        self.state.setObjectName("state")
        self.textActive = QtWidgets.QTextBrowser(self.centralwidget)
        self.textActive.setGeometry(QtCore.QRect(10, 150, 411, 192))
        self.textActive.setObjectName("textActive")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 449, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Gp_parser"))
        self.pushButton.setText(_translate("MainWindow", "Close"))
        self.outFileButton.setText(_translate("MainWindow", "..."))
        self.closeApp.setText(_translate("MainWindow", "Close"))
        self.startParserButton.setText(_translate("MainWindow", "Go"))
        self.targetDirButton.setText(_translate("MainWindow", "..."))
        self.label.setText(_translate("MainWindow", "Исходный файл"))
        self.label_2.setText(_translate("MainWindow", "Папка с результатом"))
        self.label_3.setText(_translate("MainWindow", "Состояние:"))
        self.state.setText(_translate("MainWindow", "готов"))


