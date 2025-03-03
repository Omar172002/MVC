class Libro:
    def __init__(self, id, titulo, autor, genero):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.estado = "Disponible"
    
    def cambiar_estado(self):
        self.estado = "Prestado" if self.estado == "Disponible" else "Disponible"
        print(f"El estado del libro {self.titulo} ahora es: {self.estado}")