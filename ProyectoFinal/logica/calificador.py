import csv
from logica.lugar import Lugar

def calificar_lugar(arbol, ruta_csv="data/lugares.csv"):
    print("\n--- Calificar un Lugar ---")
    id = input("Ingresa el ID del lugar a calificar: ")

    nodo = arbol.buscar(id)
    if not nodo:
        print("No se encontró un lugar con ese ID.")
        return

    lugar = nodo
    print(f"Lugar encontrado: {lugar.nombre} - Calificación actual: {lugar.calificacion}")
    try:
        nueva = float(input("Nueva calificación (0 a 5): "))
        if not 0 <= nueva <= 5:
            print("La calificación debe estar entre 0 y 5.")
            return

        # Actualizar calificación (promedio simple)
        lugar.calificacion = round((lugar.calificacion + nueva) / 2, 2)

        # Reescribir el archivo CSV con la nueva calificación
        actualizar_csv_con_nueva_calificacion(lugar, ruta_csv)

        print(f"Calificación actualizada a: {lugar.calificacion}")

    except ValueError:
        print("Entrada inválida. Debes ingresar un número.")

def actualizar_csv_con_nueva_calificacion(lugar_actualizado, ruta_csv):
    filas = []
    with open(ruta_csv, mode='r', encoding='utf-8') as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            if fila and fila[0] == lugar_actualizado.id:
                fila[6] = str(lugar_actualizado.calificacion)
            filas.append(fila)

    with open(ruta_csv, mode='w', newline='', encoding='utf-8') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerows(filas)
