import random
from clase_lista_nombres import ListaNombres
from digipymon import Digipymon

def generar_digipymon_aleatorio():
    lista = ListaNombres()
    nombre = lista.obtener_nombre_digipymon()
    vida = random.randint(10,20)
    ataque = random.randint(1,10)
    nivel = random.randint(1,3)
    tipo = random.choice(["fuego", "agua", "planta"])
    digi = Digipymon(nombre,vida,ataque,tipo,nivel)

    return digi

def buscar_digipymon(jugador,inventario):
    while True:
        pymon = generar_digipymon_aleatorio()
        print(f"Has encontrado un Digipymon aleatorio!!!!! {pymon}")
        probabilidad = 100 - (pymon.nivel * 10)
        print(f"La probailidad de que captures a una persona: {probabilidad}%")


def


    


    