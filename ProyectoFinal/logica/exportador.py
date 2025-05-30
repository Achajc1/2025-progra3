import csv
import os
from datetime import datetime

def exportar_recomendaciones_csv(lista_lugares, ruta_destino="data/recomendaciones"):
    # Crear carpeta si no existe
    os.makedirs(ruta_destino, exist_ok=True)

    # Crear nombre del archivo basado en la fecha/hora
    nombre_archivo = f"recomendaciones_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    ruta_completa = os.path.join(ruta_destino, nombre_archivo)

    # Escribir CSV
    with open(ruta_completa, mode='w', newline='', encoding='utf-8') as archivo_csv:
        writer = csv.writer(archivo_csv)
        writer.writerow(["ID", "Nombre", "Tipo", "Calificación", "Tiempo Estadia", "Costo Aproximado", "Latitud", "Longitud"])

        for lugar in lista_lugares:
            writer.writerow([
                lugar.id,
                lugar.nombre,
                lugar.tipo,
                lugar.calificacion,
                lugar.tiempo_estadia,
                lugar.precio,
                lugar.latitud,
                lugar.longitud
            ])
    
    print(f"\n✅ Recomendaciones exportadas correctamente a: {ruta_completa}")
    return ruta_completa


def exportar_lugares_csv(arbol, ruta_destino="data/lugares_exportados"):
    os.makedirs(ruta_destino, exist_ok=True)
    nombre_archivo = f"lugares_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    ruta_completa = os.path.join(ruta_destino, nombre_archivo)

    lugares = arbol.obtener_todos_los_lugares()

    with open(ruta_completa, mode='w', newline='', encoding='utf-8') as archivo_csv:
        writer = csv.writer(archivo_csv)
        writer.writerow(["ID", "Nombre", "Tipo", "Calificación", "Tiempo Estadia", "Costo Aproximado", "Latitud", "Longitud"])

        for lugar in lugares:
            writer.writerow([
                lugar.id,
                lugar.nombre,
                lugar.tipo,
                lugar.calificacion,
                lugar.tiempo_estadia,
                lugar.precio,
                lugar.latitud,
                lugar.longitud
            ])

    print(f"\n✅ Lugares exportados correctamente a: {ruta_completa}")
    return ruta_completa
