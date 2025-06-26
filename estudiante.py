class Estudiante:
    def __init__(self, id=0, nombre="", promedio=0.0):
        self.id = id
        self.nombre = nombre
        self.promedio = promedio

    def calcular_promedio(self, calificaciones):
        if not calificaciones:
            return 0.0
        self.promedio = sum(calificaciones) / len(calificaciones)
        return self.promedio

    def mostrar_informacion(self):
        print(f"ID: {self.id}")
        print(f"Nombre: {self.nombre}")
        print(f"Promedio: {self.promedio:.2f}")
