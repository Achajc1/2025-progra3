import math

class Vertice:
    def __init__(self, lugar):
        self.lugar = lugar  # Objeto de tipo Lugar
        self.adyacentes = {}  # Diccionario: clave=Vertice destino, valor=(distancia_km, tiempo_traslado_horas)

    def agregar_adyacente(self, vertice_destino, distancia_km, tiempo_horas):
        self.adyacentes[vertice_destino] = (distancia_km, tiempo_horas)


class Grafo:
    def __init__(self):
        self.vertices = {}  # Clave: lugar.id, Valor: Vertice

    def agregar_vertice(self, lugar):
        if lugar.id not in self.vertices:
            self.vertices[lugar.id] = Vertice(lugar)

    def agregar_arista(self, id_origen, id_destino):
        if id_origen in self.vertices and id_destino in self.vertices:
            origen = self.vertices[id_origen]
            destino = self.vertices[id_destino]
            distancia = self.calcular_distancia(origen.lugar, destino.lugar)
            tiempo = distancia / 50  # Suponemos promedio de 50 km/h de traslado
            origen.agregar_adyacente(destino, distancia, tiempo)
            destino.agregar_adyacente(origen, distancia, tiempo)  # Grafo no dirigido

    def calcular_distancia(self, lugar1, lugar2):
        # Fórmula de Haversine para calcular distancia entre dos coordenadas geográficas
        R = 6371  # Radio de la Tierra en km
        lat1, lon1 = math.radians(lugar1.latitud), math.radians(lugar1.longitud)
        lat2, lon2 = math.radians(lugar2.latitud), math.radians(lugar2.longitud)
        dlat = lat2 - lat1
        dlon = lon2 - lon1

        a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distancia = R * c
        return distancia

    def obtener_vertice(self, id_lugar):
        return self.vertices.get(id_lugar)

    def obtener_vertices(self):
        return list(self.vertices.values())
