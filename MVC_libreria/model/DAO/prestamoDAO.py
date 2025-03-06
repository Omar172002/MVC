from model.objects.prestamo import Prestamo
from dbConnection.FirebaseConnection import FirebaseConnection

class PrestamoDAO:
    def __init__(self):
        self.firebase_connection = FirebaseConnection()
        if self.firebase_connection.db is not None:
            self.prestamos_ref = self.firebase_connection.db.collection('prestamos')
        else:
            self.prestamos_ref = None

    def add_prestamo(self, prestamo):
        if self.prestamos_ref is None:
            print("Error: No hay conexión con Firebase")
            return

        try:
            if not isinstance(prestamo, Prestamo):
                raise ValueError("El objeto no es una instancia de Prestamo")
            self.prestamos_ref.add(prestamo.create_dictionary())  
            print("Préstamo agregado con éxito")
        except Exception as e:
            print(f"Error al agregar el préstamo: {e}")

    def get_prestamos(self):
        if self.prestamos_ref is None:
            print("No se puede conectar a Firebase")
            return []

        try:
            return [doc.to_dict() for doc in self.prestamos_ref.stream()]
        except Exception as e:
            print(f"Error al obtener los préstamos: {e}")
            return []

    def get_prestamo_por_usuario(self, usuario):
        """Obtiene los préstamos asociados a un usuario"""
        if self.prestamos_ref is None:
            print("No se puede conectar a Firebase")
            return None

        try:
            query = self.prestamos_ref.where("usuario", "==", usuario).stream()
            prestamos = [doc.to_dict() for doc in query]
            return prestamos if prestamos else None
        except Exception as e:
            print(f"Error al obtener los préstamos del usuario {usuario}: {e}")
            return None

    def get_prestamos_activos(self):
        """Obtiene todos los préstamos activos (que aún no han vencido)"""
        if self.prestamos_ref is None:
            print("No se puede conectar a Firebase")
            return []

        try:
            query = self.prestamos_ref.where("fecha_final", ">=", "2025-03-05").stream()
            return [doc.to_dict() for doc in query]
        except Exception as e:
            print(f"Error al obtener los préstamos activos: {e}")
            return []
