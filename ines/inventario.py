#Definimos la clase Inventario
class Inventario:
    #Método constructor que se ejecuta al crear un nuevo objeto de tipo Inventario
    def __init__(self):
        self.objetos = {} #Diccionario para guardar los objetos y sus cantidades

    #Método para añadir objetos al inventario
    def añadir_objeto(self, nombre, cantidad):
        if nombre in self.objetos:
            self.objetos[nombre] += 1 #Suma la cantidad en el caso en el que exista
        else:
            self.objetos[nombre] = 1 #Crea esa cantidad en el caso de que no exista

    #Método para usar un objeto del inventario
    def usar_objeto(self, objeto):
        self.objetos[objeto] -= 1
        if self.objetos [objeto] == 0:
            self.objetos.__delitem__(objeto)