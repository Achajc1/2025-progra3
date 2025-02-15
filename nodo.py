class nodo:
    def __init__(self, nombre):
        self.nombre=nombre
        self.siguiente=None

nd1=nodo("James")
nd2=nodo("Erwin")
nd1.siguiente=nd2
nd3=nodo("Sara")
print(nd1.siguiente)
print(nd2)
nd2.siguiente=nd3
print(nd2.siguiente)
print(nd3)