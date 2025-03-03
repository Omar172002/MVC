from PyQt6 import QtWidgets
from view.loginView import Ui_MainWindow as LoginView
from controllers.agregarLibroController import AgregarLibroController
from dbConnection.FirebaseConnection import FirebaseConnection  # Conexión a Firebase
from model.DAO.usuarioDAO import UsuarioDAO  # Importa el DAO de Usuario

class LoginController(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = LoginView()
        self.ui.setupUi(self)
        self.ui.BT_login.clicked.connect(self.check_login)
        self.usuario_dao = UsuarioDAO()  # Instancia de usuarioDAO para acceder a Firebase

    def check_login(self):
        username = self.ui.login_input.toPlainText().strip().lower()
        rol = self.ui.rol_input.toPlainText().strip().lower()

        # Si el usuario y el rol son "admin", permite el acceso sin verificar Firebase
        if username == "admin" and rol == "admin":
            self.open_agregar_libro_view()
            return
        
        # Si no es "admin", verificar en Firebase
        usuario = self.usuario_dao.get_usuario_por_nombre(username)

        if usuario:
            rol_usuario = usuario.get("rol", "").lower()  # Obtiene el rol del usuario

            if rol_usuario == "admin":
                self.open_agregar_libro_view()
            else:
                QtWidgets.QMessageBox.warning(self, "Error", "Usuario no autorizado")
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Usuario no encontrado")

    def open_agregar_libro_view(self):
        # Abre la ventana de agregar libro
        self.agregar_libro_window = AgregarLibroController()
        self.agregar_libro_window.show()
        self.close()
