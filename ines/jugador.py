class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.lista_digipymon = []
        self.cantidad_digipymon = 0
        self.digicoins = 10

    def añadir_digipymon(self, digipymon):
        self.lista_digipymon.append(digipymon)
        self.cantidad_digipymon += 1

    def consultar_digipymon(self):
        for digipymon in self.lista_digipymon:
            return self.lista_digipymon
        
    def consultar_digicoins(self):
        return self.digicoins