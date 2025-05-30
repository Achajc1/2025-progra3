class Grafo:
    def __init__(self):
        self.vertices = []
        self.adyacencias = {}

    def agregar_vertice(self, lugar):
        if lugar not in self.vertices:
            self.vertices.append(lugar)
            self.adyacencias[lugar] = []

    def agregar_arista(self, origen, destino, peso):
        if origen in self.adyacencias and destino in self.adyacencias:
            self.adyacencias[origen].append((destino, peso))
            self.adyacencias[destino].append((origen, peso))  # si el grafo es no dirigido
