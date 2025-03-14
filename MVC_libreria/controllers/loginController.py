from PyQt6 import QtWidgets
from view.loginView import Ui_MainWindow as LoginView  # Vista de login
from view.solicitarLibroView import Ui_MainWindow_SolicitarLibro as solicitar_libro_window # Vista de solicitar libro
from controllers.solicitarLibroController import SolicitarLibroController
from controllers.agregarLibroController import AgregarLibroController
from dbConnection.FirebaseConnection import FirebaseConnection  # Conexión a Firebase
from model.DAO.usuarioDAO import UsuarioDAO  # DAO de Usuario
from model.DAO.profesorDAO import ProfesorDAO  # DAO de Profesor


class LoginController(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = LoginView()
        self.ui.setupUi(self)
        self.ui.BT_login.clicked.connect(self.check_login)
        self.usuario_dao = UsuarioDAO()  # Instancia de UsuarioDAO para acceder a Firebase
        self.profesor_dao = ProfesorDAO()  # Instancia de ProfesorDAO para profesores

    def check_login(self):
        username = self.ui.login_input.toPlainText().strip().lower()
        rol = self.ui.rol_input.toPlainText().strip().lower()

        if rol == "administrador":
            usuario = self.usuario_dao.get_usuario_por_nombre_en_rol(username, "administradores")
            if usuario:
                self.open_agregar_libro_view()
            else:
                QtWidgets.QMessageBox.warning(self, "Error", "Administrador no encontrado")

        elif rol == "estudiante":
            usuario = self.usuario_dao.get_usuario_por_nombre_en_rol(username, "alumnos")
            if usuario:
                self.open_solicitar_libro_view(username, rol)  # Vista para estudiantes
            else:
                QtWidgets.QMessageBox.warning(self, "Error", "Estudiante no encontrado")

        elif rol == "profesor":
            usuario = self.usuario_dao.get_usuario_por_nombre_en_rol(username, "profesores")
            if usuario:
                self.open_solicitar_libro_view(username, rol)  # Vista para profesores
            else:
                QtWidgets.QMessageBox.warning(self, "Error", "Profesor no encontrado")

        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Rol no válido o usuario no encontrado")

    def open_agregar_libro_view(self):
        self.agregar_libro_window = AgregarLibroController()
        self.agregar_libro_window.show()
       
        self.close()

    def open_solicitar_libro_view(self, username, rol):
        self.solicitar_libro_window = SolicitarLibroController(username, rol)  # Pasar username y rol
        self.solicitar_libro_window.show()
        self.close()
