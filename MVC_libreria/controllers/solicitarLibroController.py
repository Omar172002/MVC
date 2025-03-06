from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMessageBox
from view.solicitarLibroView import Ui_MainWindow_SolicitarLibro
from model.objects.prestamo import Prestamo
from model.DAO.prestamoDAO import PrestamoDAO
from datetime import datetime, timedelta
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMessageBox
from model.DAO.agregarLibroDAO import LibroDAO
from model.objects.libro import Libro

class SolicitarLibroController(QtWidgets.QMainWindow):
    def __init__(self, username, rol):
        super().__init__()
        self.ui = Ui_MainWindow_SolicitarLibro()
        self.ui.setupUi(self)
        self.libro_dao = LibroDAO()
        self.username = username  # Guardamos el username
        self.rol = rol            # Guardamos el rol
        self.initializeGUI()

    def initializeGUI(self):
        self.ui.BT_solicitarLibro.clicked.connect(self.solicitarLibro)
        self.ui.BT_regresar.clicked.connect(self.regresar)

    def regresar(self):
        self.close()
        from controllers.loginController import LoginController
        self.login_window = LoginController()
        self.login_window.show()

    def solicitarLibro(self):
        titulo = self.ui.input_libro.text()
        usuario = self.ui.input_usuario.text()

        if not titulo or not usuario:
            QMessageBox.warning(self, "Error", "Por favor, ingrese todos los datos.", QMessageBox.StandardButton.Ok)
            return

        libros_disponibles = self.libro_dao.obtener_libros_disponibles()
        libro_existente = next((libro for libro in libros_disponibles if libro.get_titulo() == titulo), None)

        if not libro_existente:
            QMessageBox.warning(self, "Error", "El libro no está disponible o no existe.", QMessageBox.StandardButton.Ok)
            return

        libro_existente.set_estado("Solicitado")
        self.libro_dao.actualizar_estado_libro(libro_existente)

        QMessageBox.information(self, "Éxito", f"Libro '{titulo}' solicitado correctamente.", QMessageBox.StandardButton.Ok)
        self.ui.input_libro.clear()
        self.ui.input_usuario.clear()
