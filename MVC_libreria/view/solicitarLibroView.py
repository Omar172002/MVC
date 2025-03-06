from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_MainWindow_SolicitarLibro(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 350)
        MainWindow.setStyleSheet("background-color: #000; color: white;")  # Fondo negro y texto blanco

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.layout = QtWidgets.QVBoxLayout(self.centralwidget)

        # Título
        self.label_titulo = QtWidgets.QLabel("Solicitar un Libro", self.centralwidget)
        self.label_titulo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_titulo.setStyleSheet("font-size: 18px; font-weight: bold; color: white;")  # Texto blanco

        # Formulario
        self.form_layout = QtWidgets.QFormLayout()
        
        self.label_usuario = QtWidgets.QLabel("Usuario:", self.centralwidget)
        self.input_usuario = QtWidgets.QLineEdit(self.centralwidget)
        self.input_usuario.setStyleSheet("padding: 5px; border-radius: 5px; border: 1px solid white; color: white; background-color: #333;")

        self.label_libro = QtWidgets.QLabel("Título del Libro:", self.centralwidget)
        self.input_libro = QtWidgets.QLineEdit(self.centralwidget)
        self.input_libro.setStyleSheet("padding: 5px; border-radius: 5px; border: 1px solid white; color: white; background-color: #333;")

        self.form_layout.addRow(self.label_usuario, self.input_usuario)
        self.form_layout.addRow(self.label_libro, self.input_libro)

        # Botones
        self.button_layout = QtWidgets.QHBoxLayout()
        
        self.BT_solicitarLibro = QtWidgets.QPushButton("Solicitar Libro", self.centralwidget)
        self.BT_solicitarLibro.setStyleSheet("background-color: #4CAF50; color: white; font-weight: bold; padding: 8px; border-radius: 5px;")

        self.BT_regresar = QtWidgets.QPushButton("Regresar", self.centralwidget)
        self.BT_regresar.setStyleSheet("background-color: #D32F2F; color: white; font-weight: bold; padding: 8px; border-radius: 5px;")

        self.button_layout.addWidget(self.BT_solicitarLibro)
        self.button_layout.addWidget(self.BT_regresar)

        # Agregar widgets al layout principal
        self.layout.addWidget(self.label_titulo)
        self.layout.addLayout(self.form_layout)
        self.layout.addLayout(self.button_layout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Solicitar Libro"))
