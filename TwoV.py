# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TwoV.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 648)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, -1, 781, 591))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setMidLineWidth(0)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setHorizontalSpacing(6)
        self.gridLayout_2.setVerticalSpacing(2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.spinBox_2 = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.spinBox_2.setMaximum(255)
        self.spinBox_2.setSingleStep(2)
        self.spinBox_2.setProperty("value", 21)
        self.spinBox_2.setObjectName("spinBox_2")
        self.gridLayout_2.addWidget(self.spinBox_2, 1, 6, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 0, 5, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 4, 1, 1)
        self.spinBox_4 = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.spinBox_4.setProperty("value", 6)
        self.spinBox_4.setObjectName("spinBox_4")
        self.gridLayout_2.addWidget(self.spinBox_4, 2, 6, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 0, 0, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.spinBox.setMaximum(255)
        self.spinBox.setSingleStep(2)
        self.spinBox.setProperty("value", 19)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout_2.addWidget(self.spinBox, 1, 3, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 1)
        self.spinBox_5 = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.spinBox_5.setProperty("value", 6)
        self.spinBox_5.setObjectName("spinBox_5")
        self.gridLayout_2.addWidget(self.spinBox_5, 2, 5, 1, 1)
        self.spinBox_3 = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.spinBox_3.setSingleStep(2)
        self.spinBox_3.setProperty("value", 7)
        self.spinBox_3.setObjectName("spinBox_3")
        self.gridLayout_2.addWidget(self.spinBox_3, 2, 3, 1, 1)
        self.spinBox_6 = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.spinBox_6.setSingleStep(2)
        self.spinBox_6.setProperty("value", 7)
        self.spinBox_6.setObjectName("spinBox_6")
        self.gridLayout_2.addWidget(self.spinBox_6, 2, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 2, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 2, 0, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_2.setText(_translate("MainWindow", "Выполнить"))
        self.label_4.setText(_translate("MainWindow", "GaussianBlur 2"))
        self.pushButton.setText(_translate("MainWindow", "Открыть"))
        self.label_6.setText(_translate("MainWindow", "Height"))
        self.label_7.setText(_translate("MainWindow", "Width"))
        self.label_5.setText(_translate("MainWindow", "GaussianBlur 1"))
        self.label_3.setText(_translate("MainWindow", "TextLabel"))