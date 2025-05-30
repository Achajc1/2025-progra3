import os
import platform
from graphviz import Digraph

def exportar_grafo(grafo, ruta_destino="exportaciones/grafo", nombre="grafo_rutas"):
    os.makedirs(ruta_destino, exist_ok=True)

    dot = Digraph(format='png')
    dot.attr(rankdir='LR')

    for nodo in grafo.vertices:
        dot.node(str(nodo.id), label=f"{nodo.nombre}\n{nodo.tipo}")

    for origen in grafo.vertices:
        for destino, distancia in grafo.adyacencias[origen]:
            dot.edge(str(origen.id), str(destino.id), label=f"{distancia:.1f} km")

    ruta_completa = os.path.join(ruta_destino, nombre)
    dot.render(ruta_completa, cleanup=True)

    print(f"✅ Grafo exportado correctamente en: {ruta_completa}.png")
    _abrir_imagen(ruta_completa + ".png")

def _abrir_imagen(ruta):
    sistema = platform.system()
    if sistema == "Windows":
        os.startfile(ruta)
    elif sistema == "Darwin":
        os.system(f"open '{ruta}'")
    else:
        os.system(f"xdg-open '{ruta}'")
