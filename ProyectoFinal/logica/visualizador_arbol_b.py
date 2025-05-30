import os
import platform
from graphviz import Digraph # type: ignore

def exportar_arbol_b(arbol, ruta_destino="exportaciones/arbol", nombre="arbol_b"):
    os.makedirs(ruta_destino, exist_ok=True)
    dot = Digraph(format='png')

    def recorrer(nodo, nombre_nodo="N"):
        if nodo is None:
            return
        etiqueta = "|".join(str(k.id) for k in nodo.llaves)
        actual = nombre_nodo + str(id(nodo))
        dot.node(actual, label=etiqueta, shape='record')
        if not nodo.hoja:
            for i, hijo in enumerate(nodo.hijos):
                hijo_nombre = actual + f"_h{i}"
            recorrer(hijo, hijo_nombre)
            dot.edge(actual, hijo_nombre)


    recorrer(arbol.raiz)
    ruta_completa = os.path.join(ruta_destino, nombre)
    dot.render(ruta_completa, cleanup=True)

    print(f"✅ Árbol B exportado correctamente en: {ruta_completa}.png")
    _abrir_imagen(ruta_completa + ".png")

def _abrir_imagen(ruta):
    sistema = platform.system()
    if sistema == "Windows":
        os.startfile(ruta)
    elif sistema == "Darwin":
        os.system(f"open '{ruta}'")
    else:
        os.system(f"xdg-open '{ruta}'")
