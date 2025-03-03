from model.usuario import Usuario

class Estudiante(Usuario):
    def solicitar_prestamo(self):
        print(f"{self.nombre} ha solicitado un préstamo de libros.")
