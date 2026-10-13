from alumno import Alumno
from nota import Nota

def pedir_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Debe ingresar un numero entero valido.")

def pedir_decimal(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Debe ingresar un numero valido.")

def main():
    alumnos = []

    salirAlumno = False
    while not salirAlumno:
        nombreCompleto = input("Ingrese nombre del alumno: ")

        while nombreCompleto.isdigit() or nombreCompleto == "":
            print("Ingrese un nombre válido")
            nombreCompleto = input("")

        legajo = pedir_entero("Ingrese legajo: ")

        alumno = Alumno(nombreCompleto, legajo)

        salirNotas = False
        while not salirNotas:
            catedra = input("Ingrese el nombre de la catedra: ")
            notaExamen = pedir_decimal("Nota: ")
            alumno.agregar_nota(Nota(catedra, notaExamen))

            if len(alumno.notas) >= 1:
                respuesta = input("Desea salir de la carga de datos? (si/no): ")
                if respuesta.upper() == "SI":
                    salirNotas = True

        alumnos.append(alumno)

        respuesta = input("Desea salir de la carga de datos? (si/no): ")
        if respuesta.upper() == "SI":
            salirAlumno = True

    for alumno in alumnos:
        print(f"Alumno: {alumno.nombreCompleto} | Legajo: {alumno.legajo}")
        for nota in alumno.notas:
            print("", nota)
        print(f"El promedio del alumno es: {alumno.calcular_promedio():.2f}")

if __name__ == "__main__":
    main()