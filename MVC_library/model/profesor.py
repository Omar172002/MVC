from model.usuario import Usuario

class Profesor(Usuario):
    def solicitar_prestamo(self):
        print(f"{self.nombre} ha solicitado un préstamo de libros.")
    
    def solicitar_laptop(self):
        print(f"{self.nombre} ha solicitado una laptop.")
