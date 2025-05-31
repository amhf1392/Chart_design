# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
import numpy as np

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1119, 859)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(810, 120, 231, 41))
        self.label.setStyleSheet("font: 22pt \"B Nazanin\";")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(150, 120, 751, 41))
        self.lineEdit.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 200, 751, 41))
        self.lineEdit_2.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(930, 200, 121, 41))
        self.label_2.setStyleSheet("font: 22pt \"B Nazanin\";")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(430, 370, 281, 111))
        self.pushButton.setStyleSheet("font: 36pt \"B Nazanin\";")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1119, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # اتصال دکمه به تابع plot_graph
        self.pushButton.clicked.connect(self.plot_graph)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "طراحی نمودار"))
        self.label.setText(_translate("MainWindow", " مقدار x :"))
        self.label_2.setText(_translate("MainWindow", " مقدار Y :"))
        self.pushButton.setText(_translate("MainWindow", "طراحی"))

    def plot_graph(self):
        # دریافت مقادیر از QLineEdit ها
        x_values_str = self.lineEdit.text()
        y_values_str = self.lineEdit_2.text()

        # تبدیل رشته ها به آرایه های numpy
        try:
            x_values = np.fromstring(x_values_str, sep=',')
            y_values = np.fromstring(y_values_str, sep=',')

            # رسم نمودار
            plt.plot(x_values, y_values)
            plt.xlabel("X")
            plt.ylabel("Y")
            plt.title("Chart")
            plt.grid(True)
            plt.show()

        except Exception as e:
            print(f"خطا در پردازش ورودی: {e}")
            QtWidgets.QMessageBox.warning(MainWindow, "خطا", "لطفاً مقادیر را به درستی وارد کنید (به عنوان مثال: 1,2,3)")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
