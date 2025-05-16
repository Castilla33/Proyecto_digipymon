#Definimos la clase Jugador
class Jugador:
    #Método constructor que se ejecuta al crear un nuevo jugador
    def __init__(self, nombre):
        self.nombre = nombre
        self.lista_digipymon = []
        self.cantidad_digipymon = 0
        self.digicoins = 10

    #Método para añadir un digipymon al jugador
    def añadir_digipymon(self, digipymon):
        self.lista_digipymon.append(digipymon)
        self.cantidad_digipymon += 1

    #Método para consultar los digipymon del jugador
    def consultar_digipymon(self):
        for digipymon in self.lista_digipymon:
            return digipymon
        
    #Método para consultar las digicoins del jugador
    def consultar_digicoins(self):
        return self.digicoins