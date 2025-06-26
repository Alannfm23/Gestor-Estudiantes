from estudiante import Estudiante

def main():
    est1 = Estudiante(1, "Ana Pérez")
    califs = [8.5, 9.0, 7.8]
    est1.calcular_promedio(califs)
    est1.mostrar_informacion()

if __name__ == "__main__":
    main()
