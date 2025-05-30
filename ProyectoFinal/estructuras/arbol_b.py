from estructuras.nodo_arbol_b import NodoArbolB

class ArbolB:
    def __init__(self, grado):
        self.raiz = NodoArbolB(grado, True)
        self.grado = grado

    def insertar(self, llave):
        raiz = self.raiz
        if len(raiz.llaves) == (2 * self.grado) - 1:
            nueva_raiz = NodoArbolB(self.grado, False)
            nueva_raiz.hijos.append(self.raiz)
            self._dividir_hijo(nueva_raiz, 0)
            self._insertar_no_lleno(nueva_raiz, llave)
            self.raiz = nueva_raiz
        else:
            self._insertar_no_lleno(raiz, llave)

    def _insertar_no_lleno(self, nodo, llave):
        i = len(nodo.llaves) - 1
        if nodo.hoja:
            nodo.llaves.append(None)
            while i >= 0 and llave.id < nodo.llaves[i].id:
                nodo.llaves[i + 1] = nodo.llaves[i]
                i -= 1
            nodo.llaves[i + 1] = llave
        else:
            while i >= 0 and llave.id < nodo.llaves[i].id:
                i -= 1
            i += 1
            if len(nodo.hijos[i].llaves) == (2 * self.grado) - 1:
                self._dividir_hijo(nodo, i)
                if llave.id > nodo.llaves[i].id:
                    i += 1
            self._insertar_no_lleno(nodo.hijos[i], llave)

    def _dividir_hijo(self, padre, i):
        grado = self.grado
        y = padre.hijos[i]
        z = NodoArbolB(grado, y.hoja)
        padre.hijos.insert(i + 1, z)
        padre.llaves.insert(i, y.llaves[grado - 1])
        z.llaves = y.llaves[grado:(2 * grado - 1)]
        y.llaves = y.llaves[0:grado - 1]
        if not y.hoja:
            z.hijos = y.hijos[grado:(2 * grado)]
            y.hijos = y.hijos[0:grado]

    def recorrer_en_orden(self):
        resultado = []
        if self.raiz is not None:
            self._recorrer_en_orden(self.raiz, resultado)
        return resultado

    def _recorrer_en_orden(self, nodo, resultado):
        for i in range(len(nodo.llaves)):
            if not nodo.hoja:
                self._recorrer_en_orden(nodo.hijos[i], resultado)
            resultado.append(nodo.llaves[i])
        if not nodo.hoja:
            self._recorrer_en_orden(nodo.hijos[len(nodo.llaves)], resultado)
