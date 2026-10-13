from celda import Celda
from matriz import Matriz

def pedir_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Debe ingresar un número entero válido")

def main():
    matriz = Matriz()

    print("Carga de celdas (escriba FIN como valor para terminar)")
    while True:
        valor = input("Ingrese el valor de la celda: ")
        if valor.upper() == "FIN":
            break

        fila = pedir_entero("Ingrese la fila: ")
        columna = pedir_entero("Ingrese la columna: ")

        if matriz.existe_celda(fila, columna):
            print("Esa fila y columna ya fueron cargadas. Intente con otra posicion.")
            continue

        celda = Celda(fila, columna, valor)
        matriz.agregar_celda(celda)

    matriz.mostrar_celdas()

    fila = pedir_entero("Ingrese la fila a consultar: ")
    columna = pedir_entero("Ingrese la columna a consultar: ")
    print("Resultado:", matriz.obtener_valor(fila, columna))

if __name__ == "__main__":
    main()