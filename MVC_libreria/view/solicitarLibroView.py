from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        
        # Botones
        self.BT_solicitarLibros = QtWidgets.QPushButton(parent=self.frame)
        self.BT_solicitarLibros.setGeometry(QtCore.QRect(310, 210, 100, 32))
        self.BT_solicitarLibros.setObjectName("BT_solicitarLibros")
        
        self.BT_regrear = QtWidgets.QPushButton(parent=self.frame)
        self.BT_regrear.setGeometry(QtCore.QRect(100, 380, 100, 32))
        self.BT_regrear.setObjectName("BT_regrear")
        
        # Campos de entrada
        self.input_titulo = QtWidgets.QLineEdit(self.frame)
        self.input_titulo.setGeometry(QtCore.QRect(150, 150, 200, 32))
        self.input_titulo.setObjectName("input_titulo")
        
        self.input_usuario = QtWidgets.QLineEdit(self.frame)  # Cambiar de input_autor a input_usuario
        self.input_usuario.setGeometry(QtCore.QRect(150, 200, 200, 32))  # Posición ajustada
        self.input_usuario.setObjectName("input_usuario")

        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Solicitar Libro"))
        self.BT_solicitarLibros.setText(_translate("MainWindow", "Solicitar libro"))
        self.BT_regrear.setText(_translate("MainWindow", "Regresar"))
