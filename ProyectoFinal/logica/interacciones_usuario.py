import uuid
from logica.lugar import Lugar

def agregar_lugar_manual(arbol):
    try:
        nombre = input("Nombre del lugar: ")
        tipo = input("Tipo (Turístico/Hospedaje): ")
        latitud = float(input("Latitud: "))
        longitud = float(input("Longitud: "))
        precio = float(input("Precio aproximado: "))
        calificacion = float(input("Calificación (1-5): "))
        tiempo_estadia = float(input("Tiempo de estadía en días: "))

        nuevo_lugar = Lugar(
            id=str(uuid.uuid4()),  # ID único para evitar errores de comparación
            nombre=nombre,
            tipo=tipo,
            latitud=latitud,
            longitud=longitud,
            precio=precio,
            calificacion=calificacion,
            tiempo_estadia=tiempo_estadia
        )

        arbol.insertar(nuevo_lugar)
        print(f"✔ Lugar '{nombre}' agregado correctamente.")
    except ValueError:
        print("❌ Error: Entrada inválida. Asegúrate de ingresar valores correctos.")
