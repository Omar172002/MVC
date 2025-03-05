from PyQt6 import QtWidgets
from view.crearUsuarioView import Ui_MainWindow_agregarUsuarios
from model.objects.usuario import Usuario
from model.objects.alumno import Alumno
from model.objects.administador import Administrador  # Importa la clase Administrador
from model.objects.profesor import Profesor  
from model.DAO.usuarioDAO import UsuarioDAO
from model.DAO.alumnoDAO import AlumnoDAO
from model.DAO.adminstradorDAO import AdministradorDAO  
from model.DAO.profesorDAO import ProfesorDAO  

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
        from controllers.agregarLibroController import AgregarLibroController
        self.login_window = AgregarLibroController()
        self.login_window.show()

    def agregarUsuario(self):
        nombre = self.ui.input_nombre.text().strip()
        rol = self.ui.input_rol.text().strip().lower() 
        matricula = self.ui.input_matricula.text().strip()

        if not nombre or not rol:
            QtWidgets.QMessageBox.warning(self, "Advertencia", "Todos los campos son obligatorios.", QtWidgets.QMessageBox.StandardButton.Ok)
            return

        if rol == "estudiante":
            if not matricula:
                QtWidgets.QMessageBox.warning(self, "Advertencia", "La matrícula es obligatoria para los estudiantes.", QtWidgets.QMessageBox.StandardButton.Ok)
                return
            usuario = Alumno(nombre=nombre, rol=rol, matricula=matricula)
            usuario_dao = AlumnoDAO()
            usuario_dao.add_alumno(usuario)  

        elif rol == "administrador": 
            usuario = Administrador(nombre=nombre, rol=rol, matricula=matricula) 
            usuario_dao = AdministradorDAO() 
            usuario_dao.add_administrador(usuario)  

        elif rol == "profesor":  
            usuario = Profesor(nombre=nombre, rol=rol, matricula=matricula)  
            usuario_dao = ProfesorDAO()  
            usuario_dao.add_profesor(usuario)  

        else:  
            usuario = Usuario(nombre=nombre, rol=rol)
            usuario_dao = UsuarioDAO()
            usuario_dao.add_usuario(usuario)  

        QtWidgets.QMessageBox.information(self, "Éxito", "Usuario agregado correctamente.", QtWidgets.QMessageBox.StandardButton.Ok)
        self.clearFields()

    def clearFields(self):
        self.ui.input_nombre.clear()
        self.ui.input_rol.clear()
        self.ui.input_matricula.clear()
