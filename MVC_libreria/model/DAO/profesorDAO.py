from model.objects.profesor import Profesor
from dbConnection.FirebaseConnection import FirebaseConnection

class ProfesorDAO:
    def __init__(self):
        self.firebase_connection = FirebaseConnection()
        if self.firebase_connection.db is not None:
            self.profesores_ref = self.firebase_connection.db.collection('profesores')
        else:
            self.profesores_ref = None

    def add_profesor(self, profesor):
        if self.profesores_ref is None:
            print("Error: No hay conexión con Firebase")
            return

        try:
            if not isinstance(profesor, Profesor):
                raise ValueError("El objeto no es una instancia de Profesor")
            self.profesores_ref.add(profesor.create_dictionary())  
            print("Profesor agregado con éxito")
        except Exception as e:
            print(f"Error al agregar el profesor: {e}")

    def get_profesores(self):
        if self.profesores_ref is None:
            print("No se puede conectar a Firebase")
            return []

        try:
            return [doc.to_dict() for doc in self.profesores_ref.stream()]
        except Exception as e:
            print(f"Error al obtener los profesores: {e}")
            return []

    def get_profesor_por_matricula(self, matricula):
        if self.profesores_ref is None:
            print("No se puede conectar a Firebase")
            return None

        try:
            query = self.profesores_ref.where("matricula", "==", matricula).limit(1).stream()
            for doc in query:
                return doc.to_dict()  
            return None
        except Exception as e:
            print(f"Error al obtener el profesor por matrícula: {e}")
            return None
