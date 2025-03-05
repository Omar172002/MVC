from PyQt6 import QtWidgets
from view.loginView import Ui_MainWindow as LoginView
from view.solicitarLibroView import Ui_MainWindow as SolicitarLibroView
from view.solicitarLibroView import Ui_MainWindow as SolicitarLibroView
from controllers.agregarLibroController import AgregarLibroController
from dbConnection.FirebaseConnection import FirebaseConnection  # Conexión a Firebase
from model.DAO.usuarioDAO import UsuarioDAO  # Importa el DAO de Usuario
from model.DAO.profesorDAO import ProfesorDAO  # Importa el DAO de Profesor


class LoginController(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = LoginView()
        self.ui.setupUi(self)
        self.ui.BT_login.clicked.connect(self.check_login)
        self.usuario_dao = UsuarioDAO()  # Instancia de usuarioDAO para acceder a Firebase
        self.profesor_dao = ProfesorDAO() 

    def check_login(self):
        username = self.ui.login_input.toPlainText().strip().lower()
        rol = self.ui.rol_input.toPlainText().strip().lower()

        # Si el rol es "administrador", buscar en la colección "administradores"
        if rol == "administrador":
            usuario = self.usuario_dao.get_usuario_por_nombre_en_rol(username, "administradores")
            if usuario:
                self.open_agregar_libro_view()  # Vista para administradores
            else:
                QtWidgets.QMessageBox.warning(self, "Error", "Administrador no encontrado")

        # Si el rol es "estudiante", buscar en la colección "alumnos"
        elif rol == "estudiante":
            usuario = self.usuario_dao.get_usuario_por_nombre_en_rol(username, "alumnos")
            if usuario:
                self.open_alumno_view()  # Vista para alumnos (Asegúrate de implementar esta vista)
            else:
                QtWidgets.QMessageBox.warning(self, "Error", "Estudiante no encontrado")

        # Si el rol es "profesor", buscar en la colección "profesores"
        elif rol == "profesor":
            usuario = self.usuario_dao.get_usuario_por_nombre_en_rol(username, "profesores")
            if usuario:
                self.open_profesor_view()  # Vista para profesores
            else:
                QtWidgets.QMessageBox.warning(self, "Error", "Profesor no encontrado")

        # Si no es un rol válido
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Rol no válido o usuario no encontrado")

    def open_agregar_libro_view(self):
        self.agregar_libro_window = AgregarLibroController()
        self.agregar_libro_window.show()
        self.close()

    def open_alumno_view(self):
        QtWidgets.QMessageBox.information(self, "Bienvenido", "Acceso como alumno")
    

    def open_profesor_view(self):
     
        QtWidgets.QMessageBox.information(self, "Bienvenido", "Acceso como profesor")
     
