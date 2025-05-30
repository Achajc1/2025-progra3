class NodoA:
    def __init__(self, valor):
        self.valor = valor
        self.der = None
        self.izq = None

class ABB:
    def __init__(self):
        self.raiz = None  # La raíz del árbol comienza vacía

    def agregar(self, valor, nodo=None):
        if nodo is None:
            return NodoA(valor)  # Crea un nuevo nodo si el actual es None

        if valor < nodo.valor:
            nodo.izq = self.agregar(valor, nodo.izq)  # Inserta en la izquierda
        elif valor > nodo.valor:
            nodo.der = self.agregar(valor, nodo.der)  # Inserta en la derecha

        return nodo  # Retorna el nodo actualizado

    def insertar(self, valor):
        self.raiz = self.agregar(valor, self.raiz)  # Inserta en la raíz

# ✅ Ahora podemos crear el árbol y agregar valores correctamente
arbolbb = ABB()
arbolbb.insertar(7)
arbolbb.insertar(11)

# ✅ Verificamos si el valor 11 se insertó correctamente en la derecha de la raíz
print(arbolbb.raiz.der.valor)  # Debería imprimir: 11