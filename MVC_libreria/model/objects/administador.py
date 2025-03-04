from model.objects.usuario import Usuario

class Administrador(Usuario):
    def __init__(self, nombre, rol, matricula):
        super().__init__(nombre, rol)  # Llama al constructor de la clase padre
        self.__matricula = matricula  # Nuevo atributo exclusivo de Administrador

    # Getter para matrícula
    def get_matricula(self):
        return self.__matricula

    # Setter para matrícula
    def set_matricula(self, matricula):
        self.__matricula = matricula

    # Representación en diccionario para Firebase
    def create_dictionary(self):
        data = super().create_dictionary()  # Obtiene los datos de Usuario
        data["matricula"] = self.__matricula  # Agrega la matrícula
        return data

