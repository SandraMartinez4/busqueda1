class Nodo:
    def __init__(self, datos):
        self.datos = datos
        self.padre = None
        self.costo = 0

    def get_datos(self):
        return self.datos

    def set_padre(self, padre):
        self.padre = padre

    def get_padre(self):
        return self.padre

    def set_costo(self, costo):
        self.costo = costo

    def get_costo(self):
        return self.costo

    def igual(self, nodo):
        return self.datos == nodo.get_datos()

    def en_lista(self, lista):
        for n in lista:
            if self.igual(n):
                return True
        return False