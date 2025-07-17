# main.py

from estudiante import (
    EstudianteInformatica,
    EstudianteMedicina,
    EstudianteVeterinaria
)

def main():
    ei = EstudianteInformatica(100, "Ana López", 2, "Python")
    ei.calcular_promedio([9.0, 8.5, 9.2])
    ei.mostrar_información()
    print("-" * 30)

    em = EstudianteMedicina(101, "Carlos Ruiz", 5, "Pediatría")
    em.calcular_promedio([8.8, 9.0, 9.5])
    em.mostrar_información()
    em.solicitar_práctica_clínica()
    print("-" * 30)

    ev = EstudianteVeterinaria(102, "Lucía Gómez", 3, "Gato")
    ev.calcular_promedio([9.2, 9.4, 8.9])
    ev.mostrar_información()
    ev.agendar_cita_con_animal()
    print("-" * 30)

if __name__ == "__main__":
    main()
