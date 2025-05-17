import random
from clase_inventario import Inventario
from clase_jugador import Jugador 
from clase_lista_nombres import Lista
from enemigo import Enemigo
from digipymon import Digipymon
jugador = Jugador("Juga")

def menu():
    print("-----------Menu-----------")
    print("1. Buscar digipymon")
    print("2. Luchar contra un entrenador")
    print("3. Ir a la tienda")
    print("4. Usar objetos")
    print("5. Consultar inventario")
    print("6. Consultar digipymons")
    print("7. Salir")

def combate():
    lista_de_nombres = Lista()
    enemigo1 = Enemigo(random.choice(lista_de_nombres.lista_nombres_entrenadores))

    print("-----------¿Deseas luchar?-----------")
    print("1 para luchar")
    print("2 para huir")

    combate = int(input("¿Que quieres hacer? "))

    if combate == 1:
        contadorJug = 0
        contadorEn = 0
        for i in range(int(jugador.cantidad_digipymon)):
            tipos = ["Agua", "Fuego", "Planta"]
            enemigo1.añadir_digipymon(digiEn = Digipymon((random.choice(lista_de_nombres.lista_nombres_digipymon), random.randint(10, 20), random.randint(0, 9), random.randint(0, 3), random.choice(tipos))))
        
        for x in range(int(jugador.cantidad_digipymon)):
            digi_jugador = jugador.lista_digipymon[x]
            digi_enemigo = enemigo1.lista_digipymon[x]

            if digi_jugador.salud == 0:
                print("Tu digipymon: " + digi_jugador.nombre + " no tiene salud. ¡Pierdes el combate!")
                contadorEn += 1
            elif digi_jugador.ataque > digi_enemigo.ataque:
                print("El digipymon del jugador: " + digi_jugador.nombre + ", supera al digipymon enemigo: " + digi_enemigo.nombre)
                diferencia = digi_jugador.ataque - digi_enemigo.ataque
                digi_jugador.salud -= diferencia
                contadorJug += 1
                if digi_jugador.salud == 0:
                    print("Tu digipymon ha caído en combate!")
            elif digi_jugador.ataque < digi_enemigo.ataque:
                print("El digipymon del jugador: " + digi_jugador.nombre + ", supera al digipymon enemigo: " + digi_enemigo.nombre)
                diferencia = digi_jugador.ataque - digi_enemigo.ataque
                digi_jugador.salud -= diferencia
                contadorEn += 1
                if digi_jugador.salud == 0:
                    print("Tu digipymon ha caído en combate!")
            elif digi_jugador.ataque == digi_enemigo.ataque:
                print("Vuestros digipymon tienen el mismo ataque ¡Es una empate!")
            
        if contadorJug > contadorEn:
            jugador.digicoins += contadorJug
        elif contadorJug < contadorEn:
            jugador.digicoins -= contadorEn 
        
        if jugador.digicoins <= 0:
            jugador.digicoins = 0

    elif combate == 2:
        print("Has huido. Has perdido una digicoin")
        jugador.digicoins -= 1

        if jugador.digicoins <= 0:
            jugador.digicoins = 0

def usar_item():
    inventario = Inventario()
    print("-----------Inventario-----------")
    print("¿Qué item deseas usar?")
    print("--------------------------------")
    print(inventario.objetos)
    print("--------------------------------")
    objeto_elegido = input("Elige el objeto: ")
    if objeto_elegido == "Digipyballs":
        print("No puedes usar ahora mismo las digipyballs")
    #elif objeto_elegido != "Pocion" or "Anabolizantes":
    #print("No existe ese objeto")
    elif objeto_elegido == "Pocion":
        # Las pociones aumentan la vida de un digipymon
        inventario.usar_objeto(objeto_elegido)
        print("Has usado: " + objeto_elegido + "!")
        # ¿Es necesario un límite de vida?
    elif objeto_elegido == "Anabolizantes":
        # Los anabolizantes el ataque
        inventario.usar_objeto(objeto_elegido)
        print("Has usado: " + objeto_elegido + "!")
    else:
        print("No existe ese objeto")