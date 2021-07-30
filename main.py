from PyQt5 import QtWidgets , QtGui,QtCore,uic
import sys

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("appui.ui",self)
        self.show()
        self.Sort_b.clicked.connect(self.Sort)
        self.AscOrder.setChecked(True)
        self.UnsortedNums.setFocus()
        self.Delete_b.clicked.connect(self.Delete)
        self.actionAbout.triggered.connect(self.about)
        self.actionExit.triggered.connect(self.exit)
     
    #implementing my own sort method.i didnt want to use the builtin .sort() method.
    def Sort(self):
        self.statusbar.showMessage("")
        try:
            import re
            uN = self.UnsortedNums.toPlainText().rstrip().lstrip()
            uN = re.split(',|\s',uN)
            uN = [int(x) for x in uN]
            if self.AscOrder.isChecked() == True:
                for i in range(len(uN)):
                    for j in range(i+1,len(uN)):
                        if uN[j] < uN[i]:
                            num1 = uN[i]
                            num2 = uN[j]
                            uN[i] = num2
                            uN[j] = num1
            else:
                for i in range(len(uN)):
                    for j in range(i+1,len(uN)):
                        if uN[j] > uN[i]:
                            num1 = uN[i]
                            num2 = uN[j]
                            uN[i] = num2
                            uN[j] = num1

            uN = [str(x) for x in uN]             
            self.sortedNums.setText(" , ".join(uN))
        except:
            self.statusbar.showMessage("An error has occurred !")    

    def Delete(self):
        self.UnsortedNums.clear()
        self.sortedNums.clear()
        self.statusbar.showMessage("")

    def about(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("About")
        msg.setText("SortNumbers:\nVersion:1.0\nDeveloper:Oussama Ben Sassi\nGithub:https://github.com/Oussama1403")
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.exec_()                                                  

    def exit(self):
        QtWidgets.QApplication.quit() 


app = QtWidgets.QApplication(sys.argv)
win = MyWindow()
sys.exit(app.exec_()) 
