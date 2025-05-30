from estructuras.grafo import Grafo
from logica.lugar import Lugar
import math

def construir_grafo_desde_arbol(arbol):
    grafo = Grafo()

    lugares = arbol.recorrer_en_orden()

    # Agregar vértices
    for lugar in lugares:
        grafo.agregar_vertice(lugar)

    # Conectar todos los lugares entre sí con distancia geográfica como peso
    for i in range(len(lugares)):
        for j in range(i + 1, len(lugares)):
            l1 = lugares[i]
            l2 = lugares[j]
            distancia = calcular_distancia((l1.latitud, l1.longitud), (l2.latitud, l2.longitud))
            grafo.agregar_arista(l1, l2, distancia)

    return grafo

def calcular_distancia(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def recomendar_ruta(grafo, origen, presupuesto_maximo, dias_disponibles):
    lugares = []
    total_dias = 0
    total_presupuesto = 0

    # Ordenar vértices por distancia desde el origen
    vertices_ordenados = sorted(
        grafo.vertices,
        key=lambda lugar: calcular_distancia((lugar.latitud, lugar.longitud), origen)
    )

    for lugar in vertices_ordenados:
        if lugar.tiempo_estadia is None or lugar.precio is None:
            continue

        if total_dias + lugar.tiempo_estadia <= dias_disponibles and \
           total_presupuesto + lugar.precio <= presupuesto_maximo:
            lugares.append(lugar)
            total_dias += lugar.tiempo_estadia
            total_presupuesto += lugar.precio

    return lugares
