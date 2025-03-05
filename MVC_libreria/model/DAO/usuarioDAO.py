from dbConnection.FirebaseConnection import FirebaseConnection
from model.objects.usuario import Usuario

class UsuarioDAO:
    def __init__(self):
        self.firebase_connection = FirebaseConnection()
        if self.firebase_connection.db is not None:
            self.usuarios_ref = self.firebase_connection.db.collection('usuarios')  # Para usuarios en general
        else:
            self.usuarios_ref = None

    def get_usuario_por_nombre(self, nombre):
        if self.usuarios_ref is None:
            print("Error: No hay conexión con Firebase")
            return None
        try:
            query = self.usuarios_ref.where("nombre", "==", nombre).limit(1).stream()
            for doc in query:
                return doc.to_dict()  # Devuelve el primer resultado como diccionario
            return None
        except Exception as e:
            print(f"Error al obtener el usuario: {e}")
            return None

    # Método para obtener el usuario por nombre y rol
    def get_usuario_por_nombre_en_rol(self, nombre, rol):
        if self.firebase_connection.db is None:
            print("Error: No hay conexión con Firebase")
            return None
        
        # Dependiendo del rol, buscaremos en la colección adecuada
        if rol == "administradores":
            usuarios_ref = self.firebase_connection.db.collection('administradores')
        elif rol == "alumnos":
            usuarios_ref = self.firebase_connection.db.collection('alumnos')
        elif rol == "profesores":
            usuarios_ref = self.firebase_connection.db.collection('profesores')  
        else:
            print(f"Rol desconocido: {rol}")
            return None
        
        try:
            query = usuarios_ref.where("nombre", "==", nombre).limit(1).stream()
            for doc in query:
                return doc.to_dict()  # Devuelve el primer resultado como diccionario
            return None
        except Exception as e:
            print(f"Error al obtener el usuario: {e}")
            return None
