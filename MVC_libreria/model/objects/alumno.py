from model.objects.usuario import Usuario


class Alumno(Usuario):
    def __init__(self, nombre, rol, matricula):
        super().__init__(nombre, rol)  
        self.__matricula = matricula  

    # Getter para matrícula
    def get_matricula(self):
        return self.__matricula

    # Setter para matrícula
    def set_matricula(self, matricula):
        self.__matricula = matricula

    # Representación en diccionario para Firebase
    def create_dictionary(self):
        data = super().create_dictionary()  
        data["matricula"] = self.__matricula  
        return data
