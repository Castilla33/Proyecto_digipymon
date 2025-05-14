import random
import time
from lista_nombres import Lista
from digipymon import Digipymon
from inventario import Inventario
from jugador import Jugador 
from enemigo import Enemigo

jugador = Jugador("Juga")

def generar_digipymon_aleatorio():
    lista = Lista()
    nombre = lista.obtener_nombre_digipymon()
    vida = random.randint(10,20)
    ataque = random.randint(1,10)
    nivel = random.randint(1,3)
    tipo = random.choice(["fuego", "agua", "planta"])
    digi = Digipymon(nombre,vida,ataque,tipo,nivel)

    return digi

def menu():
    print("-----------Menu-----------")
    print("1. Buscar digipymon")
    print("2. Luchar contra un entrenador")
    print("3. Ir a la tienda")
    print("4. Usar objetos")
    print("5. Consultar inventario")
    print("6. Consultar digipymons")
    print("7. Salir")

def buscar_digipymon(jug, inv):
        pymon = generar_digipymon_aleatorio()
        print(f"Has encontrado un Digipymon aleatorio!!!!! " + str(pymon))
        probabilidad = 100 - (pymon.nivel * 10)
        print(f"La probailidad de que captures a un mostruo es: {probabilidad}%")
        bucle = True
        while bucle:
            print("Cuidado estas en sitio peligroso ")
            print("1. Captura Digipymon")
            print("Rapido huye!!!!")

            nombre = int(input("Elije la opcion que quieras "))
            
            if nombre == 1:
                if "Digiballs" in inv.objetos["Digiballs"]:
                    
                    inv.objetos.usar_objetos("Digyballs")

                    elegir = random.randint(1, 100)

                    if elegir <= probabilidad:
                        jug.añadir_digipymon(pymon)
                    else:
                        print("No has podido capturar al monstruo")
                        print("Ha escapado corre!!: " + str(pymon))
                    bucle = False
                else:
                    print("No te quedan digyballs")
            elif nombre == 2:
                if jug.digicoins > 0:
                    jug.digicoins -= 1
                    print(f"Tiene un total de:  {jug.consultar_digicoins()} digicoins")

                    bucle = False
                elif jug.digicoins <= 0:
                    print("Debes un total de:  {jug.digicoins} digicoins")

                else:
                    print("No es una opcion valida")

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
    elif objeto_elegido == "Pocion":
        inventario.usar_objeto(objeto_elegido)

        for digipymon in jugador.consultar_digipymon():
            print(digipymon)

        aplicarDigipymon = input("Elige el digipymon en el que aplicarlo: ")
        for digipymon in jugador.lista_digipymon:
            if digipymon.nombre == aplicarDigipymon:
                digipymon.vida += 10
                print("Has usado: " + objeto_elegido + "!")
            else:
                print("Ese digipymon no existe")
    elif objeto_elegido == "Anabolizantes":
        inventario.usar_objeto(objeto_elegido)

        for digipymon in jugador.consultar_digipymon():
            print(digipymon)
            
        aplicarDigipymon = input("Elige el digipymon en el que aplicarlo: ")
        for digipymon in jugador.lista_digipymon:
            if digipymon.nombre == aplicarDigipymon:
                digipymon.ataque += 4
                print("Has usado: " + objeto_elegido + "!")
            else:
                print("Ese digipymon no existe")
        
    else:
        print("No existe ese objeto")


def main():
    inv = Inventario()
    print("Basado en un juego de cazar monstruos, donde hubo una guerra entre ellos")
    #time.sleep(2)
    print("No se sabe como se originó la guerra entre ellos pero...")
    #time.sleep(2)
    print("La guerra era entre dos bandas, por lo que se dice")
    #time.sleep(2)
    print("Gano una de ellas")
    #time.sleep(2)
    nombre = input("Introduce el nombre del entrenador: ")
    jug = Jugador(nombre)
    #time.sleep(1)
    print("Al final solo quedo un bando")
    #time.sleep(2)
    print("La ciudad se quedo completamente en silencio...")
    python = generar_digipymon_aleatorio()
    #time.sleep(2)
    print("Has obtenido un Digipymon ")
    print("es un: " + str(python))
    jug.añadir_digipymon(python)
    print("Has obtenido 3 digipyballs y una pocion")
    inv.añadir_objeto("Digyballs", 3)
    inv.añadir_objeto("Pocion", 1)

    salir = True
    while salir:
        menu()

        opcion = input("Elige que quieres hacer: ")

        if opcion == 1:
            buscar_digipymon(jug, inv)

        elif opcion == 2:
            print("No puedes luchar")

        elif opcion == 3:
            print("Todavia no se ha usado en la tienda")

        elif opcion == 4:
            print(inv.objetos)
            objeto = input("¿Que objeto quieres usar?: ")
            inv.usar_objeto(objeto)
        
        elif opcion == 5:
            print("Tu inventario es:")

        elif opcion == 6:
            print("Tus Digipymon son: ")

            jug.consultar_digipymon()
        
        elif opcion == 7:
            print("Hasta la proxima!!")
            salir = False
main()