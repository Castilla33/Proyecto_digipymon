class clase_inventario:
    def __init__(self):
        self.objetos = {}

    def añadir_objeto(self, nombre, cantidad):
        if nombre in self.objetos:
            self.objetos[nombre] = self.objetos.get(nombre) + 1
        else:
            self.objetos[nombre] = 1

    def usar_objeto(self, objeto):
        self.objetos[objeto] = self.objetos.get(objeto) - 1
        if self.objetos [objeto] == 0:
            self.objetos.__delitem__(objeto)