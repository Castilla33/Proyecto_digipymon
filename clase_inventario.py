class clase_inventario:
    def __init__(self):
        self.objetos = {}

    def añadir_objeto(self, nombre, cantidad):
        for i in self.objetos:
            nombre == self.objetos[i]
            self.objetos[i] = self.objetos[i] + 1
        else:
            self.objetos[nombre] = 1

    def usar_objeto(self, objeto):
        self.objetos[objeto] = self.objetos[objeto] - 1
        if self.objetos [objeto] == 0:
            self.objetos.pop(objeto)