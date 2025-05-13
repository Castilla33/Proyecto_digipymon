import random
import time
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
    print("Bienvenido a la mejor tienda {jugador.nombre}")
    print("Tienes {jugador.monedas}monedas")
    time.sleep(3)
    salir = False
    jugador1 = jugador()
    inventario1 = inventario()
    while salir == False:
        print("Bienvenido a la tienda: ")
        print("1. Digipyball --> 5 digicoins")
        print("2. Pocion --> 3 digicoins")
        print("3. Anabolizante --> 4 digicoins")
        print("4. salir")
        opcion = input ("Elije una de las opciones: ")
        
        if opcion == 1:
            if jugador1.digicoins >= 5:
                jugador1.digicoins - 5
                inventario1.añadir_objetos.append("Digiball",1)
                print("Has comprado una Digiball!!!!")
            else:
                print("No tienes suficientes monedas")
            
        if opcion == 2:
            if jugador1.digicoins >= 3:
                jugador1.digicoins - 3
                inventario1.añadir_objetos.append("Pocion",1)
                print("Has comprado una pocion!!!")
            else:
                print("No tienes suficiente dinero")

        if opcion == 3:
            if jugador1.digicoins >= 4:
                jugador1.digicoins - 4
                inventario1.añadir_objetos.append("Anabolizante")
            else:
                print("No tienes suficiente dinero")
            
            if opcion == 4:
                print("Has huido del juego")
                time.sleep(3)
                salir = True


    
    

    
    
        


    


    


    


    