from model.objects.administador import Administrador
from dbConnection.FirebaseConnection import FirebaseConnection

class AdministradorDAO:
    def __init__(self):
        self.firebase_connection = FirebaseConnection()
        if self.firebase_connection.db is not None:
            self.administradores_ref = self.firebase_connection.db.collection('administradores')
        else:
            self.administradores_ref = None

    def add_administrador(self, administrador):
        if self.administradores_ref is None:
            print("Error: No hay conexión con Firebase")
            return

        try:
            if not isinstance(administrador, Administrador):
                raise ValueError("El objeto no es una instancia de Administrador")
            self.administradores_ref.add(administrador.create_dictionary())  
            print("Administrador agregado con éxito")
        except Exception as e:
            print(f"Error al agregar el administrador: {e}")

    def get_administradores(self):
        if self.administradores_ref is None:
            print("No se puede conectar a Firebase")
            return []

        try:
            return [doc.to_dict() for doc in self.administradores_ref.stream()]
        except Exception as e:
            print(f"Error al obtener los administradores: {e}")
            return []

    def get_administrador_por_matricula(self, matricula):
        if self.administradores_ref is None:
            print("No se puede conectar a Firebase")
            return None

        try:
            query = self.administradores_ref.where("matricula", "==", matricula).limit(1).stream()
            for doc in query:
                return doc.to_dict()  
            return None
        except Exception as e:
            print(f"Error al obtener el administrador por matrícula: {e}")
            return None
