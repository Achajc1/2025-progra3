import csv

class BTreeNode:
    def __init__(self, t, leaf=False):
        self.t = t  # grado mínimo
        self.keys = []  # claves
        self.children = []  # hijos
        self.leaf = leaf  # True si es hoja

    def traverse(self, depth=0):
        print("    " * depth + str(self.keys))
        for child in self.children:
            child.traverse(depth + 1)

    def search(self, key):
        i = 0
        while i < len(self.keys) and key > self.keys[i]:
            i += 1
        if i < len(self.keys) and self.keys[i] == key:
            return self
        if self.leaf:
            return None
        return self.children[i].search(key)

    def insert_non_full(self, key):
        i = len(self.keys) - 1
        if self.leaf:
            self.keys.append(None)
            while i >= 0 and key < self.keys[i]:
                self.keys[i + 1] = self.keys[i]
                i -= 1
            self.keys[i + 1] = key
        else:
            while i >= 0 and key < self.keys[i]:
                i -= 1
            i += 1
            if len(self.children[i].keys) == (2 * self.t) - 1:
                self.split_child(i)
                if key > self.keys[i]:
                    i += 1
            self.children[i].insert_non_full(key)

    def split_child(self, i):
        t = self.t
        y = self.children[i]
        z = BTreeNode(t, y.leaf)
        z.keys = y.keys[t:]
        y.keys = y.keys[:t-1]
        if not y.leaf:
            z.children = y.children[t:]
            y.children = y.children[:t]
        self.children.insert(i + 1, z)
        self.keys.insert(i, y.keys.pop())

class BTree:
    def __init__(self, t):
        self.t = t
        self.root = BTreeNode(t, True)

    def traverse(self):
        if self.root:
            self.root.traverse()

    def search(self, key):
        return self.root.search(key)

    def insert(self, key):
        r = self.root
        if len(r.keys) == (2 * self.t) - 1:
            s = BTreeNode(self.t, False)
            s.children.insert(0, r)
            s.split_child(0)
            i = 0
            if s.keys[0] < key:
                i += 1
            s.children[i].insert_non_full(key)
            self.root = s
        else:
            r.insert_non_full(key)

    def load_from_csv(self, filename):
        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                for value in row:
                    try:
                        self.insert(int(value))
                    except ValueError:
                        print(f"Ignored non-integer value: {value}")

# --- Programa Interactivo ---
def main():
    print("Árbol B en Python")
    t = int(input("Ingrese el grado mínimo (t) del árbol: "))
    btree = BTree(t)

    while True:
        print("\nOpciones:")
        print("1. Insertar clave")
        print("2. Buscar clave")
        print("3. Eliminar clave (No implementado)")
        print("4. Mostrar árbol")
        print("5. Cargar desde CSV")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            key = int(input("Ingrese la clave a insertar: "))
            btree.insert(key)
        elif opcion == "2":
            key = int(input("Ingrese la clave a buscar: "))
            result = btree.search(key)
            if result:
                print(f"Clave {key} encontrada.")
            else:
                print(f"Clave {key} no encontrada.")
        elif opcion == "3":
            print("Eliminar aún no implementado.")
        elif opcion == "4":
            btree.traverse()
        elif opcion == "5":
            filename = input("Ingrese el nombre del archivo CSV: ")
            btree.load_from_csv(filename)
        elif opcion == "6":
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
