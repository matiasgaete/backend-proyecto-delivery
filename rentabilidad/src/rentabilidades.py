class Rentabilidad():
    def __init__(self, id_local, nombre_local, direccion_local):
        self.id_local = id_local
        self.nombre_local = nombre_local
        self.direccion_local = direccion_local
        self.rentabilidades = []

    def agregar_rentabilidad(self, registro):
        self.rentabilidades.append(registro)

    def calcular_rentabilidad(self):
        return sum(self.rentabilidades)
