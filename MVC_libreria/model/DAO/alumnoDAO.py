from model.objects.alumno import Alumno
from dbConnection.FirebaseConnection import FirebaseConnection

class AlumnoDAO:
    def __init__(self):
        self.firebase_connection = FirebaseConnection()
        if self.firebase_connection.db is not None:
            self.alumnos_ref = self.firebase_connection.db.collection('alumnos')
        else:
            self.alumnos_ref = None

    def add_alumno(self, alumno):
        if self.alumnos_ref is None:
            print("Error: No hay conexión con Firebase")
            return

        try:
            if not isinstance(alumno, Alumno):
                raise ValueError("El objeto no es una instancia de Alumno")
            self.alumnos_ref.add(alumno.create_dictionary())  
            print("Alumno agregado con éxito")
        except Exception as e:
            print(f"Error al agregar el alumno: {e}")

    def get_alumnos(self):
        if self.alumnos_ref is None:
            print("No se puede conectar a Firebase")
            return []

        try:
            return [doc.to_dict() for doc in self.alumnos_ref.stream()]
        except Exception as e:
            print(f"Error al obtener los alumnos: {e}")
            return []

    def get_alumno_por_matricula(self, matricula):
        if self.alumnos_ref is None:
            print("No se puede conectar a Firebase")
            return None

        try:
            query = self.alumnos_ref.where("matricula", "==", matricula).limit(1).stream()
            for doc in query:
                return doc.to_dict()  
            return None
        except Exception as e:
            print(f"Error al obtener el alumno por matrícula: {e}")
            return None
