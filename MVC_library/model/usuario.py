class Usuario:
    def __init__(self, id, nombre, apellido_paterno, apellido_materno):
        self.id = id
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
    
    def consultar_libros(self):
        print(f"{self.nombre} está consultando libros.")
    
    def solicitar_prestamo(self):
        print(f"{self.nombre} está solicitando un préstamo de libro.")