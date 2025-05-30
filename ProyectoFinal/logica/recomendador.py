import math

# Cálculo de distancia entre coordenadas
def calcular_distancia(lat1, lon1, lat2, lon2):
    # Fórmula Haversine para distancias entre coordenadas geográficas
    R = 6371  # Radio de la tierra en km
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)

    a = math.sin(dlat / 2)**2 + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon / 2)**2

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distancia = R * c
    return distancia  # en kilómetros

def recomendar_lugares(origen_lat, origen_lon, lugares, presupuesto_diario):
    # Filtramos solo los lugares turísticos válidos
    candidatos = [
        lugar for lugar in lugares
        if lugar.tipo == "Turístico" and lugar.precio <= presupuesto_diario and lugar.tiempo_estadia is not None
    ]

    # Calculamos datos adicionales: distancia, tiempo total estimado, y puntaje
    recomendaciones = []
    for lugar in candidatos:
        distancia = calcular_distancia(origen_lat, origen_lon, lugar.latitud, lugar.longitud)
        tiempo_traslado = distancia / 50  # Suponemos promedio 50km/h
        tiempo_total = tiempo_traslado + lugar.tiempo_estadia

        if tiempo_total <= 8:
            # Puntaje ponderado
            puntaje = lugar.calificacion / (lugar.precio + 1)
            recomendaciones.append((lugar, puntaje))

    # Ordenamos por puntaje y tomamos los mejores 5
    recomendaciones.sort(key=lambda x: x[1], reverse=True)
    mejores_lugares = [r[0] for r in recomendaciones[:5]]

    return mejores_lugares
