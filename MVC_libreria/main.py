from PyQt6 import QtWidgets
from controllers.loginController import LoginController  # Importamos el controlador de login
from controllers.agregarLibroController import AgregarLibroController  # Importamos el controlador de agregar libro


# pyuic6 -o  loginView.py loginView.ui        
# pyuic6 -o  agregarLibroView.py agregarLibroView.ui    
# pyuic6 -o  crearUsuarioView.py crearUsuarioView.ui   
# pyuic6 -o  solicitarLibroView.py solicitarLibroView.ui   


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login_window = LoginController()
    login_window.show()
   
    sys.exit(app.exec())
