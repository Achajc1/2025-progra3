class Nodo:
    def __init__(self, nombre, apellido, carnet):
        self.nombre = nombre
        self.apellido = apellido
        self.carnet = carnet
        self.siguiente = None
        self.anterior = None

class ListaDobleEnlazada:
    def __init__(self):
        self.inicio = None
        self.fin = None

    def insertar_al_principio(self, nombre, apellido, carnet):
        nuevo = Nodo(nombre, apellido, carnet)
        if not self.inicio:
            self.inicio = nuevo
            self.fin = nuevo
        else:
            nuevo.siguiente = self.inicio
            self.inicio.anterior = nuevo
            self.inicio = nuevo

    def insertar_al_final(self, nombre, apellido, carnet):
        nuevo = Nodo(nombre, apellido, carnet)
        if not self.fin:
            self.inicio = nuevo
            self.fin = nuevo
        else:
            self.fin.siguiente = nuevo
            nuevo.anterior = self.fin
            self.fin = nuevo

    def eliminar_por_valor(self, carnet):
        actual = self.inicio
        while actual:
            if actual.carnet == carnet:
                if actual.anterior:
                    actual.anterior.siguiente = actual.siguiente
                else:
                    self.inicio = actual.siguiente
                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior
                else:
                    self.fin = actual.anterior
                return
            actual = actual.siguiente

    def mostrar_lista(self):
        actual = self.inicio
        elementos = []
        while actual:
            elementos.append(f"{actual.nombre} {actual.apellido} ({actual.carnet})")
            actual = actual.siguiente
        print("None <-> " + " <-> ".join(elementos) + " <-> None")


def menu():
    lista = ListaDobleEnlazada()
    while True:
        print("\nMenu:")
        print("1. Insertar al principio")
        print("2. Insertar al final")
        print("3. Eliminar por valor")
        print("4. Mostrar lista")
        print("5. Salir")
        opcion = input("Seleccione una opcion: ")

        if opcion == '1':
            n = input("Nombre: ")
            a = input("Apellido: ")
            c = input("Carnet: ")
            lista.insertar_al_principio(n, a, c)
        elif opcion == '2':
            n = input("Nombre: ")
            a = input("Apellido: ")
            c = input("Carnet: ")
            lista.insertar_al_final(n, a, c)
        elif opcion == '3':
            c = input("Carnet a eliminar: ")
            lista.eliminar_por_valor(c)
        elif opcion == '4':
            lista.mostrar_lista()
        elif opcion == '5':
            break
        else:
            print("Opcion no valida")

if __name__ == "__main__":
    menu()