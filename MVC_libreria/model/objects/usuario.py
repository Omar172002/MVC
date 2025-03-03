class Usuario:
    def __init__(self, nombre, rol):
        self.__nombre = nombre
        self.__rol = rol  # Puede ser "estudiante", "profesor", "administrador", etc.

    # Getters
    def get_nombre(self):
        return self.__nombre

    def get_rol(self):
        return self.__rol

    # Setters
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_rol(self, rol):
        self.__rol = rol

    # Representación en diccionario para Firebase
    def create_dictionary(self):
        return {
            "nombre": self.__nombre,
            "rol": self.__rol
        }
