# estudiante.py

class Estudiante:
    def __init__(self, id: int, nombre: str, semestre: int):
        self.id = id
        self.nombre = nombre
        self.semestre = semestre
        self.promedio = 0.0

    def calcular_promedio(self, califs: list[float]) -> None:
        self.promedio = sum(califs)/len(califs) if califs else 0.0

    def mostrar_información(self) -> None:
        print(f"ID: {self.id}")
        print(f"Nombre: {self.nombre}")
        print(f"Semestre: {self.semestre}")
        print(f"Promedio: {self.promedio:.2f}")


class EstudianteInformatica(Estudiante):
    def __init__(self, id, nombre, semestre, lenguaje_favorito):
        super().__init__(id, nombre, semestre)
        self.carrera = "Informática"
        self.lenguaje_favorito = lenguaje_favorito

    def mostrar_información(self):
        super().mostrar_información()
        print(f"Carrera: {self.carrera}")
        print(f"Lenguaje favorito: {self.lenguaje_favorito}")


class EstudianteMedicina(Estudiante):
    def __init__(self, id, nombre, semestre, especialidad_interes):
        super().__init__(id, nombre, semestre)
        self.carrera = "Medicina"
        self.especialidad_interes = especialidad_interes

    def solicitar_práctica_clínica(self):
        print(f"{self.nombre} solicita práctica en {self.especialidad_interes}.")

    def mostrar_información(self):
        super().mostrar_información()
        print(f"Carrera: {self.carrera}")
        print(f"Especialidad de interés: {self.especialidad_interes}")


class EstudianteVeterinaria(Estudiante):
    def __init__(self, id, nombre, semestre, tipo_animal_preferido):
        super().__init__(id, nombre, semestre)
        self.carrera = "Veterinaria"
        self.tipo_animal_preferido = tipo_animal_preferido

    def agendar_cita_con_animal(self):
        print(f"{self.nombre} agenda cita para un {self.tipo_animal_preferido}.")

    def mostrar_información(self):
        super().mostrar_información()
        print(f"Carrera: {self.carrera}")
        print(f"Animal preferido: {self.tipo_animal_preferido}")
