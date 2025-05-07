class Digipymon:
    def __init__(self,nombre,vida,ataque,tipo,nivel):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.tipo = tipo
        self.nivel = nivel

    def __str__(self):
        return f"nombre: {self.nombre}, \n\
            vida: {self.vida}, \n\
            ataque: {self.ataque}, \n\
            tipo: {self.tipo}, \n\
            nivel: {self.nivel}"          
             