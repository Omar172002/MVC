from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMessageBox
from view.crearUsuarioView import Ui_MainWindow_agregarUsuarios
from model.objects.usuario import Usuario
from model.DAO.usuarioDAO import UsuarioDAO


class AgregarUsuarioController(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow_agregarUsuarios()
        self.ui.setupUi(self)
        self.initializeGUI()

    def initializeGUI(self):
        self.ui.BT_CrearUsuario.clicked.connect(self.agregarUsuario)
        self.ui.BT_regresar.clicked.connect(self.regresar)

    def regresar(self):
        self.close()
        from controllers.loginController import LoginController
        self.login_window = LoginController()
        self.login_window.show()

    def agregarUsuario(self):
        nombre = self.ui.input_nombre.text().strip()
        rol = self.ui.input_rol.text().strip()
        
        if not nombre or not rol:
            QMessageBox.warning(self, "Advertencia", "Todos los campos son obligatorios.", QMessageBox.StandardButton.Ok)
            return

        usuario = Usuario(nombre=nombre, rol=rol)
        usuario_dao = UsuarioDAO()
        usuario_dao.add_usuario(usuario)
        
        QMessageBox.information(self, "Éxito", "Usuario agregado correctamente.", QMessageBox.StandardButton.Ok)
        self.clearFields()

    def clearFields(self):
        self.ui.input_nombre.clear()
        self.ui.input_rol.clear()
