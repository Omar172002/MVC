from model.objects.usuario import Usuario
from dbConnection.FirebaseConnection import FirebaseConnection

class UsuarioDAO:
    def __init__(self):
        self.firebase_connection = FirebaseConnection()
        if self.firebase_connection.db is not None:
            self.usuarios_ref = self.firebase_connection.db.collection('usuarios')
        else:
            self.usuarios_ref = None

    def add_usuario(self, usuario):
        if self.usuarios_ref is None:
            return

        try:
            if not isinstance(usuario, Usuario):
                raise ValueError("❌ El objeto no es una instancia de Usuario")
            self.usuarios_ref.add(usuario.create_dictionary())  
            print("✅ Usuario agregado con éxito")
        except Exception as e:
            print(f"❌ Error al agregar el usuario: {e}")

    def get_usuarios(self):
        if self.usuarios_ref is None:
            print("❌ No se puede conectar a Firebase")
            return []

        try:
            return [doc.to_dict() for doc in self.usuarios_ref.stream()]
        except Exception as e:
            print(f"❌ Error al obtener los usuarios: {e}")
            return []

    def get_usuario_por_nombre(self, nombre):
        if self.usuarios_ref is None:
            print("❌ No se puede conectar a Firebase")
            return None

        try:
            query = self.usuarios_ref.where("nombre", "==", nombre).limit(1).stream()
            for doc in query:
                return doc.to_dict()  # Corregido: usar `to_dict()` en lugar de `create_dictionary()`
            return None
        except Exception as e:
            print(f"❌ Error al obtener el usuario por nombre: {e}")
            return None
