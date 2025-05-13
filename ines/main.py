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


def digishop(jugador,inventario):
    print("Bienvenido a la tienda: ")
    print("1. Digipyball --> 5 digicoins")
    print("2. Pocion --> 3 digicoins")
    print("3. Anabolizante --> 4 digicoins")
    print("4. salir")
    opcion = input ("¿Elije un número de lo que quieras comprar?: ")

    salir = True
    While salir == True:
    buscar_digipymon()
    encontrar = input("Introduce el número: ")
    
    if encontrar == 1:
        


    elif encontrar() == "salir":
    print("Nos vemos")
    salir = False

    else:
        print("Tu dato no es valido")


    


    


    