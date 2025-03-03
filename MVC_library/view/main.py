import sys
import os

# Agregar el directorio raíz al path de Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from model.profesor import Profesor
from model.estudiante import Estudiante
from model.administrador import Administrador
from model.libro import Libro
from controller.usuario_controller import UsuarioController
from controller.libro_controller import LibroController

def main():
    profesor = Profesor(1, "Carlos", "Pérez", "Gómez")
    estudiante = Estudiante(2, "Ana", "López", "Díaz")
    admin = Administrador(3, "Marta", "Hernández", "Ruiz")
    
    libro = Libro(101, "El Quijote", "Miguel de Cervantes", "Novela")
    usuario_controller = UsuarioController()
    libro_controller = LibroController()
    
    usuario_controller.solicitar_prestamo(profesor)
    usuario_controller.solicitar_prestamo(estudiante)
    admin.agregar_libro()
    
    libro_controller.cambiar_estado_libro(libro)
    
if __name__ == "__main__":
    main()