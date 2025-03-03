from datetime import date

class Prestamo:
    def __init__(self, id, fecha_inicio, fecha_vencimiento):
        self.id = id
        self.fecha_inicio = fecha_inicio
        self.fecha_vencimiento = fecha_vencimiento
        self.estado = "Activo"
    
    def cambiar_estado(self):
        self.estado = "Vencido"
        print("El préstamo ha sido marcado como vencido.")