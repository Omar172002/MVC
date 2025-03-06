# model/objects/prestamo.py
class Prestamo:
    def __init__(self, usuario_nombre, libro_titulo, fecha_prestamo, fecha_devolucion=None):
        self.usuario_nombre = usuario_nombre  # Solo el nombre del usuario
        self.libro_titulo = libro_titulo  # Solo el título del libro
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion  # Puede ser None si aún no se devuelve

    def devolver_libro(self, fecha_devolucion):
        self.fecha_devolucion = fecha_devolucion

    def create_dictionary(self):
        # Crear un diccionario del préstamo con solo texto
        return {
            "usuario": {
                "nombre": self.usuario_nombre  
            },
            "libro": {
                "titulo": self.libro_titulo  #
            },
            "fecha_prestamo": self.fecha_prestamo,
            "fecha_devolucion": self.fecha_devolucion
        }
