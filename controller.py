from PyQt5 import QtWidgets, QtGui, QtCore
from UI import Ui_MainWindow
import pandas as pd
import datetime
from PyQt5.QtWidgets import (QApplication, QMessageBox,QDialog,QPushButton)


class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() # in python3, super(Class, self).xxx = super().xxx
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()
        self.setWindowIcon(QtGui.QIcon('icon.jpg'))

    def setup_control(self):
        # TODO        
        self.ui.RefcalendarWidget.selectedDate()
        self.ui.CurecalendarWidget_2.selectedDate()
        self.ui.WeighttextEdit.setPlaceholderText("Patient Weight")
        self.ui.RefDateShow.setText(str(datetime.date.today()))      #        print(f"You clicked {self.clicked_counter} times.")
        self.ui.CureDateShow.setText(str(datetime.date.today()))
        self.ui.CurecalendarWidget_2.selectionChanged.connect(self.CureCalendar_select)
        self.ui.RefcalendarWidget.selectionChanged.connect(self.RefCalendar_select)
        self.ui.Calculationbuttom.clicked.connect(self.calc) 
        self.ui.Clearbuttom.clicked.connect(self.rest_buttom)
        dialog=QMessageBox()
        

    def calc(self):
        Diffday=(self.ui.CurecalendarWidget_2.selectedDate().toPyDate() - self.ui.RefcalendarWidget.selectedDate().toPyDate()).days
        

        if Diffday < -14 or Diffday > 14 :  # 判斷天數差是否超過 參考日期
            #self.ui.Calculationbuttom.clicked.connect(self.showDialog)
            dialog=QMessageBox()
            dialog.setText("Day from Ref.Date < -14 or >14  haven't data can be used")
            dialog.setWindowTitle('Error')
            dialog.setIcon(dialog.Critical)
            dialog.exec_()
            return
        else:
            pass

        self.ui.DiffdayShow.setText(str(Diffday))

        if self.ui.WeighttextEdit.toPlainText() =='':
            dialog=QMessageBox()
            dialog.setText("Please input patient weight")
            dialog.setWindowTitle('Error')
            dialog.setIcon(dialog.Critical)
            dialog.exec_()
            return
        else:
            pass
      

        data=pd.DataFrame({                     #建立dateframe 字典
            "Day":[i for i in range(-14,15)],
            "Decayfactor":[2.296, 2.161, 2.034, 1.914, 1.802, 1.696, 1.596, 1.502, 1.414, 1.33, 1.252, 1.178, 1.109, 1.044, 0.982, 0.925, 0.87, 0.819, 0.771, 0.725, 0.683, 0.643, 0.605, 0.569, 0.536, 0.504, 0.475, 0.447, 0.42]
        },index=[i for i in range(-14,15)]) #定義index參數
        
        Treamentfactor=data.at[Diffday, "Decayfactor"]  #擷取Decay factor

        
        self.ui.DecayfactorShow.setText(str(Treamentfactor))
        
        
        self.ui.DoseShow.setText(str(float(self.ui.WeighttextEdit.toPlainText())*55))

        Volume=round(float(self.ui.WeighttextEdit.toPlainText())*55/(Treamentfactor*1100),2) #需抽取多少體積
        self.ui.VolumeShow.setText(str(Volume))

    def RefCalendar_select(self):
        self.ui.RefDateShow.setText(str(self.ui.RefcalendarWidget.selectedDate().toPyDate()))
    
    def CureCalendar_select(self):
        self.ui.CureDateShow.setText(str(self.ui.CurecalendarWidget_2.selectedDate().toPyDate()))
    
    def rest_buttom(self):
        self.ui.RefDateShow.setText("")
        self.ui.CureDateShow.setText("")
        self.ui.RefDateShow.setText(str(self.ui.RefcalendarWidget.selectedDate().toPyDate()))
        self.ui.CureDateShow.setText(str(self.ui.CurecalendarWidget_2.selectedDate().toPyDate()))
        self.ui.DecayfactorShow.setText("")
        self.ui.DiffdayShow.setText("")
        self.ui.DoseShow.setText("")
        self.ui.VolumeShow.setText("")
        self.ui.WeighttextEdit.setText("")
    
