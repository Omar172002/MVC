

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
            print(f"Error al obtener los libros: {e}")
            return []
        
    def solicitar_libro(self, libro: Libro):
        """Método para solicitar un libro. Este podría agregar el libro como 'Solicitado' en la base de datos"""
        if self.libros_ref is None:
            print("Error: No hay conexión con Firebase")
            return None
        try:
            # Crear un diccionario del libro con estado 'Solicitado'
            libro_dict = libro.create_dictionary()
            libro_dict["estado"] = "Solicitado"  # Cambiar el estado del libro a 'Solicitado'
            
            # Agregar el libro a la base de datos de Firebase
            self.libros_ref.add(libro_dict)
            print(f"Libro solicitado con éxito: {libro_dict}")
        except Exception as e:
            print(f"Error al solicitar el libro: {e}")

    def obtener_libros_disponibles(self):
        """Método para obtener todos los libros que están disponibles"""
        if self.libros_ref is None:
            print("Error: No hay conexión con Firebase")
            return []
        try:
            # Filtrar los libros por estado "Disponible"
            query = self.libros_ref.where("estado", "==", "Disponible").stream()
            libros = []
            for doc in query:
                libro_data = doc.to_dict()
                libro = Libro(libro_data["titulo"], libro_data["autor"], libro_data["genero"], libro_data["estado"])
                libros.append(libro)
            return libros
        except Exception as e:
            print(f"Error al obtener los libros disponibles: {e}")
            return []

    def actualizar_estado_libro(self, libro: Libro):
        if self.libros_ref is None:
            print("Error: No hay conexión con Firebase")
            return

        try:
            # Buscar el libro en la base de datos por su título
            query = self.libros_ref.where("titulo", "==", libro.get_titulo()).limit(1).stream()
            for doc in query:
                doc_ref = self.libros_ref.document(doc.id)
                # Actualizar el estado del libro
                doc_ref.update({"estado": "Solicitado"})
                print(f"Estado del libro '{libro.get_titulo()}' actualizado a 'Solicitado'.")
        except Exception as e:
            print(f"Error al actualizar el estado del libro: {e}")
