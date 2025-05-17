#Importamos la librería random para seleccionar nombres aleatorios
import random

#Definimos la clase Lista
class Lista:
    #Método constructor que se ejecuta al crear un nuevo objeto Lista
    def __init__(self):
        self.lista_nombres_digipymon = ["Gárgola Sombría","Kraken de Hielo","Demonio de Ceniza","Bestia del Abismo","Hidra Espectral","Titán de Roca","Súcubo Nocturno","Vampiro de Sangre Negra","Quimera Alada","Hombre Lobo Alfa","Dragón de Fuego Eterno","Espectro del Dolor","Serpiente del Vacío","Troll de la Niebla","Nigromante Errante", "Araña Colosal", "Minotauro de las Sombras", "Golem de Cristal", "Cíclope Furioso", "Leviatán del Norte"]
        self.lista_nombres_entrenadores = ["Jose", "Alberto", "Carlota", "Inés", "David", "Mario", "Francisco", "César", "Marcos", "Manuel", "Pablo", "Juan", "Adrián", "Oliver", "Alexis", "Candela", "Carolina", "Enoc", "Javier", "Luis"]

    #Método para obtener el nombre aleatorio de digipymon
    def obtener_nombre_digipymon(self):
        nombre_digipymon = random.choice(self.lista_nombres_digipymon)
        return nombre_digipymon

    #Método para obtener un nombre aleatorio de entrenador
    def obtener_nombre_entrenador(self):
        nombre_entrenador = random.choice(self.lista_nombres_entrenadores)
        return nombre_entrenador 