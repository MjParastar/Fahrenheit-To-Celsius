from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("F to C Convertor")
        Form.resize(477, 358)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 431, 321))
        self.groupBox.setStyleSheet("background-color : #dfe4ea ;")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(170, 180, 93, 28))
        self.pushButton.setObjectName("pushButton")
        
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(140, 220, 151, 41))
        self.label_2.setStyleSheet("border : 1px solid grey ;\n"
                                   "border-left : 2px solid #2c3e50 ;\n"
                                   "border-right : 2px dashed #16a085 ;\n"
                                   "border-bottom : 2px solid #2c3e50 ;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)

        
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(50, 100, 341, 71))
        self.lineEdit.setStyleSheet("border : 1px solid #f8a5c2 ;\n"
                                    "border-radius : 5px ;\n"
                                    "background-color : #f8a5c2 ;\n"
                                    "text-align : center ;")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)  # تنظیم متن به مرکز
        self.lineEdit.setPlaceholderText("Enter Fahrenheit")
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton.clicked.connect(self.convert_temperature)
    
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Fahrenheit to Celsius Converter"))
        self.pushButton.setText(_translate("Form", "Convert"))
    
    def convert_temperature(self):
        try:
            fahrenheit = float(self.lineEdit.text())  
            celsius = (fahrenheit - 32) * 5/9  
            self.label_2.setText(f"{celsius:.2f} °C") 
        except ValueError:
            self.label_2.setText("Invalid Input") 

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())