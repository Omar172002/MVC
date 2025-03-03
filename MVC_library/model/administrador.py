from model.usuario import Usuario

class Administrador(Usuario):
    def agregar_libro(self):
        print("Administrador: Agregando un nuevo libro al catálogo.")
    
    def eliminar_libro(self):
        print("Administrador: Eliminando un libro del catálogo.")