import csv
from logica.lugar import Lugar

def agregar_lugar_manual(arbol, ruta_csv="data/lugares.csv"):
    try:
        print("\n--- Agregar Nuevo Lugar ---")
        id = input("ID del lugar (único): ")

        # Verificar si ya existe un lugar con ese ID
        if arbol.buscar(id):
            print(f"Ya existe un lugar con el ID '{id}'. Por favor, utiliza un ID diferente.")
            return

        nombre = input("Nombre: ")
        tipo = input("Tipo (Turístico o Hospedaje): ")
        latitud = float(input("Latitud: "))
        longitud = float(input("Longitud: "))
        precio = float(input("Precio estimado por visita o por noche: "))
        calificacion = float(input("Calificación (0 a 5): "))
        tiempo_estadia = input("Tiempo estimado de estadía (en días, opcional): ")

        lugar = Lugar(id, nombre, tipo, latitud, longitud, precio, calificacion, tiempo_estadia)
        arbol.insertar(lugar)

        # Guardar en CSV
        with open(ruta_csv, mode='a', newline='', encoding='utf-8') as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow([
                lugar.id, lugar.nombre, lugar.tipo, lugar.latitud, lugar.longitud,
                lugar.precio, lugar.calificacion,
                lugar.tiempo_estadia if lugar.tiempo_estadia is not None else '-'
            ])

        print(f"Lugar '{nombre}' agregado correctamente al árbol y al archivo CSV.")
    except Exception as e:
        print(f"Error al agregar el lugar: {e}")
