    
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.izquierda, valor)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.derecha, valor)

    def buscar(self, valor):
        return self._buscar_recursivo(self.raiz, valor)

    def _buscar_recursivo(self, nodo, valor):
        if nodo is None or nodo.valor == valor:
            return nodo is not None
        if valor < nodo.valor:
            return self._buscar_recursivo(nodo.izquierda, valor)
        return self._buscar_recursivo(nodo.derecha, valor)

    def eliminar(self, valor):
        self.raiz = self._eliminar_recursivo(self.raiz, valor)

    def _eliminar_recursivo(self, nodo, valor):
        if nodo is None:
            return nodo
        if valor < nodo.valor:
            nodo.izquierda = self._eliminar_recursivo(nodo.izquierda, valor)
        elif valor > nodo.valor:
            nodo.derecha = self._eliminar_recursivo(nodo.derecha, valor)
        else:
            if nodo.izquierda is None:
                return nodo.derecha
            elif nodo.derecha is None:
                return nodo.izquierda
            temp = self._min_valor_nodo(nodo.derecha)
            nodo.valor = temp.valor
            nodo.derecha = self._eliminar_recursivo(nodo.derecha, temp.valor)
        return nodo

    def _min_valor_nodo(self, nodo):
        actual = nodo
        while actual.izquierda is not None:
            actual = actual.izquierda
        return actual

    def cargar_desde_archivo(self, ruta_archivo):
        try:
            with open(ruta_archivo, 'r') as archivo:
                for linea in archivo:
                    try:
                        numero = int(linea.strip())
                        self.insertar(numero)
                    except ValueError:
                        print(f"Ignorando línea no válida: {linea.strip()}")
        except FileNotFoundError:
            print("Archivo no encontrado.")

# Ejemplo de uso
if __name__ == "__main__":
    abb = ArbolBinarioBusqueda()
    abb.insertar(10)
    abb.insertar(5)
    abb.insertar(15)
    abb.insertar(2)
    abb.insertar(7)
    print("Búsqueda de 7:", abb.buscar(7))
    print("Búsqueda de 20:", abb.buscar(20))
    abb.eliminar(5)
    print("Búsqueda de 5 después de eliminar:", abb.buscar(5))
    
    # Cargar desde un archivo
    abb.cargar_desde_archivo("numeros.txt")
