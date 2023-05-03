import sys
#from tkinter.tix import DirList
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSlot as slot

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap

import numpy as np
import cv2

from TwoV import Ui_MainWindow as Design  # Это наш конвертированный файл дизайна

file = None


class ExampleApp(QtWidgets.QMainWindow, Design):
    # Основное поведение класса наследуется из Qt, а виджеты - из design.ui
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Этот метод из класса Design, он инициализирует виджеты
        self.file = None
        self.pushButton.clicked.connect(self.OpenFile)
        self.image = None
        self.image1 = None
        self.x = None
        self.y = None
        self.opening = None
        self.v1 = None
        self.v2 = None
        self.pushButton_2.clicked.connect(self.PrintImage)

    def LoadImage(self):
        self.image = cv2.imread(self.file, 0)
        self.image1 = cv2.imread(self.file, 1)
        self.x, self.y = self.image.shape

    def Processing(self):
        h= self.spinBox_3.value()
        w =self.spinBox_6.value()
        thresh = cv2.adaptiveThreshold(self.image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, h, w)
        cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        print(type(thresh))
        print(type(cnts[0]))
        self.opening = cnts
        cv2.drawContours(self.image1, cnts[0], -1, (255, 255, 255), -1)
        #qpix = QPixmap.fromImage(thresh)
        #qpix = qpix.scaled(QSize(self.label.width(), self.label.height()))
        #self.label_3.setPixmap(qpix)

        pass

    def PrintImage(self):
        self.Processing()

        # qimg = QImage(self.opening.data, self.opening.shape[1], self.opening.shape[0], QImage.Format_Grayscale8)
        qimg = QImage(self.image1.data, self.image1.shape[1], self.image1.shape[0], QImage.Format_Grayscale8)

        # Create a QPixmap from the QImage
        qpix = QPixmap.fromImage(qimg)
        qpix = qpix.scaled(QSize(self.label.width(), self.label.height()))
        self.label_2.setPixmap(qpix)

    def OpenFile(self):
        dirlist = QFileDialog.getOpenFileName(self, "Выбрать файл", ".")
        self.file = dirlist[0]
        self.label_3.setText("{}".format(self.file))
        pixmap = QPixmap(self.file)
        pixmap = pixmap.scaled(QSize(self.label.width(), self.label.height()))
        print(type(pixmap))
        self.label.setPixmap(pixmap)
        self.LoadImage()


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    app.setStyle(QtWidgets.QStyleFactory.create('Fusion'))  # Более современная тема оформления
    app.setPalette(QtWidgets.QApplication.style().standardPalette())  # Берём цвета из темы оформления

    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение
