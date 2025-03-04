

from model.objects.libro import Libro
from dbConnection.FirebaseConnection import FirebaseConnection

class LibroDAO:
    def __init__(self):
        self.firebase_connection = FirebaseConnection()
        if self.firebase_connection.db is not None:
            self.libros_ref = self.firebase_connection.db.collection('libros')
        else:
            self.libros_ref = None

    def add_libro(self, libro):
        if self.libros_ref is None:
            print("No se puede conectar a Firebase")
            return

        try:
            if not isinstance(libro, Libro):
                raise ValueError("El objeto no es una instancia de Libro")
            self.libros_ref.add(libro.create_dictionary())  
            print("Libro agregado con éxito")
        except Exception as e:
            print(f"Error al agregar el libro: {e}")

    def get_libros(self):
        if self.libros_ref is None:
            print("No se puede conectar a Firebase")
            return []

        try:
            return [doc.create_dictionary() for doc in self.libros_ref.stream()]
        except Exception as e:
            print(f"❌ Error al obtener los libros: {e}")
            return []
