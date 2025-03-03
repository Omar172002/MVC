from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMessageBox
from view.agregarLibroView import Ui_MainWindow_AgregarLibro  # Cambiar por el archivo correcto de la vista
from dbConnection.FirebaseConnection import FirebaseConnection  # Ajustar la conexión a Firebase
from model.objects.libro import Libro  # Cambiar al objeto adecuado para el libro
from model.DAO.agregarLibroDAO import LibroDAO  # Cambiar el DAO de acuerdo al libro


class AgregarLibroController(QtWidgets.QMainWindow):  # Cambiar a QMainWindow

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow_AgregarLibro()  # Usamos el archivo de la interfaz
        self.ui.setupUi(self)  # Configuramos la interfaz
        self.initializeGUI()
        

 
    def initializeGUI(self):
        # Conectar el botón "Agregar Libro"
        self.ui.BT_agregarLIbro.clicked.connect(self.agregarLibro)
        # Conectar el botón "Regresar"
        self.ui.BT_regresar.clicked.connect(self.regresar)
        self.ui.BT_agregarUsuario.clicked.connect(self.crearUsuario)



    def regresar(self):
        # Cierra la ventana de agregar libro
        self.close()

        # Importar LoginController dentro de la función para evitar la importación circular
        from controllers.loginController import LoginController
        # Muestra la ventana de login
        self.login_window = LoginController()
        self.login_window.show()

    def crearUsuario(self):
        # Cierra la ventana de agregar libro
        self.close()
        # Importar LoginController dentro de la función para evitar la importación circular
        from controllers.crearUsuarioController import AgregarUsuarioController
        # Muestra la ventana de login
        self.login_window = AgregarUsuarioController()
        self.login_window.show()

   

    def agregarLibro(self):
        # Obtener los valores de los campos
        titulo = self.ui.input_titulo.text()
        autor = self.ui.input_Autor.text()
        genero = self.ui.input_Genero.text()

        # Crear un objeto Libro
        libro = Libro(titulo, autor, genero, "Disponible")

        # Crear la instancia del DAO y agregar el libro
        libro_dao = LibroDAO()
        libro_dao.add_libro(libro)

        # Mostrar mensaje de éxito
        QMessageBox.information(self, "Éxito", "Libro agregado correctamente.", QMessageBox.StandardButton.Ok)


        self.clearFields()

    def clearFields(self):
        # Limpiar los campos
        self.ui.input_titulo.clear()
        self.ui.input_Autor.clear()
        self.ui.input_Genero.clear()
