# Form implementation generated from reading ui file 'crearUsuarioView.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_agregarUsuarios(object):
    def setupUi(self, MainWindow_agregarUsuarios):
        MainWindow_agregarUsuarios.setObjectName("MainWindow_agregarUsuarios")
        MainWindow_agregarUsuarios.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow_agregarUsuarios)
        self.centralwidget.setObjectName("centralwidget")
        self.input_rol = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.input_rol.setGeometry(QtCore.QRect(390, 270, 113, 21))
        self.input_rol.setObjectName("input_rol")
        self.input_nombre = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.input_nombre.setGeometry(QtCore.QRect(230, 270, 113, 21))
        self.input_nombre.setObjectName("input_nombre")
        self.textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(230, 180, 104, 74))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(390, 180, 104, 74))
        self.textEdit_2.setObjectName("textEdit_2")
        self.BT_CrearUsuario = QtWidgets.QPushButton(parent=self.centralwidget)
        self.BT_CrearUsuario.setGeometry(QtCore.QRect(240, 370, 100, 32))
        self.BT_CrearUsuario.setObjectName("BT_CrearUsuario")
        self.BT_regresar = QtWidgets.QPushButton(parent=self.centralwidget)
        self.BT_regresar.setGeometry(QtCore.QRect(390, 370, 100, 32))
        self.BT_regresar.setObjectName("BT_regresar")
        self.input_matricula = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.input_matricula.setGeometry(QtCore.QRect(550, 270, 113, 21))
        self.input_matricula.setObjectName("input_matricula")
        self.textEdit_3 = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(550, 180, 104, 74))
        self.textEdit_3.setObjectName("textEdit_3")
        MainWindow_agregarUsuarios.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow_agregarUsuarios)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        MainWindow_agregarUsuarios.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow_agregarUsuarios)
        self.statusbar.setObjectName("statusbar")
        MainWindow_agregarUsuarios.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow_agregarUsuarios)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_agregarUsuarios)

    def retranslateUi(self, MainWindow_agregarUsuarios):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_agregarUsuarios.setWindowTitle(_translate("MainWindow_agregarUsuarios", "MainWindow"))
        self.textEdit.setHtml(_translate("MainWindow_agregarUsuarios", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">NOMBRE</p></body></html>"))
        self.textEdit_2.setHtml(_translate("MainWindow_agregarUsuarios", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ROL</p></body></html>"))
        self.BT_CrearUsuario.setText(_translate("MainWindow_agregarUsuarios", "Crear"))
        self.BT_regresar.setText(_translate("MainWindow_agregarUsuarios", "Regresar"))
        self.textEdit_3.setHtml(_translate("MainWindow_agregarUsuarios", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">MATRICULA</p></body></html>"))
