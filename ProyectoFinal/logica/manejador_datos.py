import csv
from logica.lugar import Lugar

def cargar_lugares_desde_csv(ruta_archivo, arbol, tipo_entidad):
    try:
        with open(ruta_archivo, newline='', encoding='utf-8') as archivo_csv:
            lector = csv.DictReader(archivo_csv)
            for fila in lector:
                if fila['tipo'] != tipo_entidad:
                    continue
                lugar = Lugar(
                    id=fila['id'],
                    nombre=fila['nombre'],
                    tipo=fila['tipo'],
                    latitud=fila['latitud'],
                    longitud=fila['longitud'],
                    precio=fila['precio'],
                    calificacion=fila['calificacion'],
                    tiempo_estadia=fila.get('tiempo_estadia')
                )
                arbol.insertar(lugar)
    except FileNotFoundError:
        print(f"Archivo {ruta_archivo} no encontrado.")
    except Exception as e:
        print(f"Error al cargar datos: {e}")
