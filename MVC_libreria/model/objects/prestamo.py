class Prestamo:
    def __init__(self, usuario, libro, fecha_inicial, fecha_final):
        self.__usuario = usuario
        self.__libro = libro
        self.__fecha_inicial = fecha_inicial
        self.__fecha_final = fecha_final

    # Getters
    def get_usuario(self):
        return self.__usuario

    def get_libro(self):
        return self.__libro

    def get_fecha_inicial(self):
        return self.__fecha_inicial

    def get_fecha_final(self):
        return self.__fecha_final

    # Setters
    def set_usuario(self, usuario):
        self.__usuario = usuario

    def set_libro(self, libro):
        self.__libro = libro

    def set_fecha_inicial(self, fecha_inicial):
        self.__fecha_inicial = fecha_inicial

    def set_fecha_final(self, fecha_final):
        self.__fecha_final = fecha_final

    # Representación en diccionario para Firebase
    def create_dictionary(self):
        return {
            "usuario": self.__usuario,
            "libro": self.__libro,
            "fecha_inicial": self.__fecha_inicial,
            "fecha_final": self.__fecha_final
        }
