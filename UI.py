# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ra-223UI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(751, 643)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.RefLabel = QtWidgets.QLabel(self.centralwidget)
        self.RefLabel.setGeometry(QtCore.QRect(110, 0, 181, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.RefLabel.setFont(font)
        self.RefLabel.setObjectName("RefLabel")
        self.CureLabel = QtWidgets.QLabel(self.centralwidget)
        self.CureLabel.setGeometry(QtCore.QRect(480, 0, 181, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.CureLabel.setFont(font)
        self.CureLabel.setObjectName("CureLabel")
        self.RefcalendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.RefcalendarWidget.setGeometry(QtCore.QRect(30, 80, 301, 231))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.RefcalendarWidget.setFont(font)
        self.RefcalendarWidget.setObjectName("RefcalendarWidget")
        self.CurecalendarWidget_2 = QtWidgets.QCalendarWidget(self.centralwidget)
        self.CurecalendarWidget_2.setGeometry(QtCore.QRect(420, 80, 301, 231))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.CurecalendarWidget_2.setFont(font)
        self.CurecalendarWidget_2.setObjectName("CurecalendarWidget_2")
        self.Ptlabel = QtWidgets.QLabel(self.centralwidget)
        self.Ptlabel.setGeometry(QtCore.QRect(20, 360, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.Ptlabel.setFont(font)
        self.Ptlabel.setObjectName("Ptlabel")
        self.WeighttextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.WeighttextEdit.setGeometry(QtCore.QRect(200, 360, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.WeighttextEdit.setFont(font)
        self.WeighttextEdit.setObjectName("WeighttextEdit")
        self.Calculationbuttom = QtWidgets.QPushButton(self.centralwidget)
        self.Calculationbuttom.setGeometry(QtCore.QRect(470, 450, 221, 91))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.Calculationbuttom.setFont(font)
        self.Calculationbuttom.setObjectName("Calculationbuttom")
        self.Ref = QtWidgets.QLabel(self.centralwidget)
        self.Ref.setGeometry(QtCore.QRect(20, 320, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.Ref.setFont(font)
        self.Ref.setObjectName("Ref")
        self.RefDateShow = QtWidgets.QLabel(self.centralwidget)
        self.RefDateShow.setGeometry(QtCore.QRect(170, 320, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.RefDateShow.setFont(font)
        self.RefDateShow.setText("")
        self.RefDateShow.setObjectName("RefDateShow")
        self.Ref_2 = QtWidgets.QLabel(self.centralwidget)
        self.Ref_2.setGeometry(QtCore.QRect(450, 320, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.Ref_2.setFont(font)
        self.Ref_2.setObjectName("Ref_2")
        self.CureDateShow = QtWidgets.QLabel(self.centralwidget)
        self.CureDateShow.setGeometry(QtCore.QRect(590, 320, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.CureDateShow.setFont(font)
        self.CureDateShow.setText("")
        self.CureDateShow.setObjectName("CureDateShow")
        self.DiffdayShow = QtWidgets.QLabel(self.centralwidget)
        self.DiffdayShow.setGeometry(QtCore.QRect(250, 410, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.DiffdayShow.setFont(font)
        self.DiffdayShow.setText("")
        self.DiffdayShow.setObjectName("DiffdayShow")
        self.Ref_3 = QtWidgets.QLabel(self.centralwidget)
        self.Ref_3.setGeometry(QtCore.QRect(20, 410, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.Ref_3.setFont(font)
        self.Ref_3.setObjectName("Ref_3")
        self.Ref_4 = QtWidgets.QLabel(self.centralwidget)
        self.Ref_4.setGeometry(QtCore.QRect(20, 470, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.Ref_4.setFont(font)
        self.Ref_4.setObjectName("Ref_4")
        self.DecayfactorShow = QtWidgets.QLabel(self.centralwidget)
        self.DecayfactorShow.setGeometry(QtCore.QRect(190, 470, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.DecayfactorShow.setFont(font)
        self.DecayfactorShow.setText("")
        self.DecayfactorShow.setObjectName("DecayfactorShow")
        self.DoseShow = QtWidgets.QLabel(self.centralwidget)
        self.DoseShow.setGeometry(QtCore.QRect(190, 520, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.DoseShow.setFont(font)
        self.DoseShow.setText("")
        self.DoseShow.setObjectName("DoseShow")
        self.Ref_5 = QtWidgets.QLabel(self.centralwidget)
        self.Ref_5.setGeometry(QtCore.QRect(20, 520, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.Ref_5.setFont(font)
        self.Ref_5.setObjectName("Ref_5")
        self.Ref_6 = QtWidgets.QLabel(self.centralwidget)
        self.Ref_6.setGeometry(QtCore.QRect(20, 570, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.Ref_6.setFont(font)
        self.Ref_6.setObjectName("Ref_6")
        self.VolumeShow = QtWidgets.QLabel(self.centralwidget)
        self.VolumeShow.setGeometry(QtCore.QRect(190, 570, 71, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.VolumeShow.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setUnderline(True)
        self.VolumeShow.setFont(font)
        self.VolumeShow.setText("")
        self.VolumeShow.setWordWrap(False)
        self.VolumeShow.setObjectName("VolumeShow")
        self.Clearbuttom = QtWidgets.QPushButton(self.centralwidget)
        self.Clearbuttom.setGeometry(QtCore.QRect(470, 360, 221, 91))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.Clearbuttom.setFont(font)
        self.Clearbuttom.setObjectName("Clearbuttom")
        self.Ref_7 = QtWidgets.QLabel(self.centralwidget)
        self.Ref_7.setGeometry(QtCore.QRect(250, 570, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.Ref_7.setFont(font)
        self.Ref_7.setObjectName("Ref_7")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(450, 570, 281, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(610, 540, 131, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(380, 600, 351, 16))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ra-223 Does Calculator for NM, YMUH"))
        self.RefLabel.setText(_translate("MainWindow", "Ref.Date"))
        self.CureLabel.setText(_translate("MainWindow", "Cure.Date"))
        self.Ptlabel.setText(_translate("MainWindow", "Patient Weight (kg)"))
        self.WeighttextEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.Calculationbuttom.setText(_translate("MainWindow", "Calculation of Dose"))
        self.Ref.setText(_translate("MainWindow", "Ref.Date is :"))
        self.Ref_2.setText(_translate("MainWindow", "Cure.Date is :"))
        self.Ref_3.setText(_translate("MainWindow", "Days from Ref.Date is : "))
        self.Ref_4.setText(_translate("MainWindow", "Decay factor is : "))
        self.Ref_5.setText(_translate("MainWindow", "Total Dose is : "))
        self.Ref_6.setText(_translate("MainWindow", "Total Volume is :"))
        self.Clearbuttom.setText(_translate("MainWindow", "Rset"))
        self.Ref_7.setText(_translate("MainWindow", "ml"))
        self.label.setText(_translate("MainWindow", "Department of Nuclear Medicine"))
        self.label_2.setText(_translate("MainWindow", "Kai-Jie, Jhan "))
        self.label_3.setText(_translate("MainWindow", "National YANG-MING University Hospital"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

