import csv

# Nodo del Árbol
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None
        self.altura = 1

# ABB: Árbol Binario de Búsqueda
class ABB:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        self.raiz = self._insertar(self.raiz, valor)

    def _insertar(self, nodo, valor):
        if nodo is None:
            return Nodo(valor)
        if valor < nodo.valor:
            nodo.izquierda = self._insertar(nodo.izquierda, valor)
        elif valor > nodo.valor:
            nodo.derecha = self._insertar(nodo.derecha, valor)
        return nodo

    def buscar(self, valor):
        return self._buscar(self.raiz, valor)

    def _buscar(self, nodo, valor):
        if nodo is None or nodo.valor == valor:
            return nodo
        if valor < nodo.valor:
            return self._buscar(nodo.izquierda, valor)
        else:
            return self._buscar(nodo.derecha, valor)

    def eliminar(self, valor):
        self.raiz = self._eliminar(self.raiz, valor)

    def _eliminar(self, nodo, valor):
        if nodo is None:
            return nodo
        if valor < nodo.valor:
            nodo.izquierda = self._eliminar(nodo.izquierda, valor)
        elif valor > nodo.valor:
            nodo.derecha = self._eliminar(nodo.derecha, valor)
        else:
            if nodo.izquierda is None:
                return nodo.derecha
            elif nodo.derecha is None:
                return nodo.izquierda
            temp = self._minimo(nodo.derecha)
            nodo.valor = temp.valor
            nodo.derecha = self._eliminar(nodo.derecha, temp.valor)
        return nodo

    def _minimo(self, nodo):
        while nodo.izquierda:
            nodo = nodo.izquierda
        return nodo

# AVL: Extiende ABB con balanceo
class AVL(ABB):
    def _insertar(self, nodo, valor):
        nodo = super()._insertar(nodo, valor)
        return self._balancear(nodo)

    def _eliminar(self, nodo, valor):
        nodo = super()._eliminar(nodo, valor)
        if nodo:
            return self._balancear(nodo)
        return nodo

    def _altura(self, nodo):
        return nodo.altura if nodo else 0

    def _actualizar_altura(self, nodo):
        nodo.altura = 1 + max(self._altura(nodo.izquierda), self._altura(nodo.derecha))

    def _factor_balance(self, nodo):
        return self._altura(nodo.izquierda) - self._altura(nodo.derecha)

    def _balancear(self, nodo):
        self._actualizar_altura(nodo)
        balance = self._factor_balance(nodo)

        # Rotación izquierda-derecha (LR)
        if balance > 1 and self._factor_balance(nodo.izquierda) < 0:
            nodo.izquierda = self._rotar_izquierda(nodo.izquierda)
            return self._rotar_derecha(nodo)

        # Rotación derecha-izquierda (RL)
        if balance < -1 and self._factor_balance(nodo.derecha) > 0:
            nodo.derecha = self._rotar_derecha(nodo.derecha)
            return self._rotar_izquierda(nodo)

        # Rotación derecha (LL)
        if balance > 1:
            return self._rotar_derecha(nodo)

        # Rotación izquierda (RR)
        if balance < -1:
            return self._rotar_izquierda(nodo)

        return nodo

    def _rotar_izquierda(self, z):
        y = z.derecha
        T2 = y.izquierda
        y.izquierda = z
        z.derecha = T2
        self._actualizar_altura(z)
        self._actualizar_altura(y)
        return y

    def _rotar_derecha(self, z):
        y = z.izquierda
        T3 = y.derecha
        y.derecha = z
        z.izquierda = T3
        self._actualizar_altura(z)
        self._actualizar_altura(y)
        return y

# Cargar desde CSV
def cargar_desde_csv(ruta, arbol):
    try:
        with open(ruta, newline='') as archivo:
            reader = csv.reader(archivo)
            for fila in reader:
                for valor in fila:
                    if valor.strip().isdigit():
                        arbol.insertar(int(valor.strip()))
        print(f"Datos cargados desde {ruta}")
    except FileNotFoundError:
        print("Archivo no encontrado.")
    except Exception as e:
        print("Error al cargar CSV:", e)

# Visualizar con Graphviz
def graficar_arbol(arbol):
    dot = Digraph()
    def recorrer(nodo):
        if nodo:
            dot.node(str(nodo.valor))
            if nodo.izquierda:
                dot.edge(str(nodo.valor), str(nodo.izquierda.valor))
                recorrer(nodo.izquierda)
            if nodo.derecha:
                dot.edge(str(nodo.valor), str(nodo.derecha.valor))
                recorrer(nodo.derecha)
    recorrer(arbol.raiz)
    dot.render('arbol_avl', format='png', cleanup=True)
    print("Árbol generado como 'arbol_avl.png'")

# Menú CLI
def menu():
    arbol = AVL()
    while True:
        print("\n--- Menú Árbol AVL ---")
        print("1. Insertar número")
        print("2. Buscar número")
        print("3. Eliminar número")
        print("4. Cargar desde CSV")
        print("5. Visualizar árbol")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                valor = int(input("Número a insertar: "))
                arbol.insertar(valor)
            except ValueError:
                print("Entrada inválida.")
        elif opcion == "2":
            try:
                valor = int(input("Número a buscar: "))
                nodo = arbol.buscar(valor)
                print("Encontrado" if nodo else "No encontrado")
            except ValueError:
                print("Entrada inválida.")
        elif opcion == "3":
            try:
                valor = int(input("Número a eliminar: "))
                arbol.eliminar(valor)
            except ValueError:
                print("Entrada inválida.")
        elif opcion == "4":
            ruta = input("Ruta del archivo CSV: ")
            cargar_desde_csv(ruta, arbol)
        elif opcion == "5":
            graficar_arbol(arbol)
        elif opcion == "6":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()