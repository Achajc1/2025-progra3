class nodo:
    def __init__(self, nombre):
        self.nombre=nombre
        self.siguiente=None

class lista:
    def __init__(self):
        self.inicio=None
    def agregar (self,nombre):
        nuevo=nodo(nombre)
        nuevo.siguiente=self.inicio
        self.inicio=nuevo
        estudiantes=lista()
        estudiantes.agregar("james")
        estudiantes.agregar("Erwin")
        estudiantes.agregar("Sara")
    def listar(self):
        temp=self.inicio
        while temp!=None:
            print(temp.nombre +"-->")
            temp=temp.siguiente
    #def borrarTodo(self):
     #   inicio=None