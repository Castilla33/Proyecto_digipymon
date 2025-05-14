import random
import time
from clase_inventario import Inventario
from clase_jugador import Jugador 
from clase_lista_nombres import Lista
from enemigo import Enemigo
from Digipymon import Digipymon

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
            print("2. Rapido huye!!!!")

            nombre = int(input("Elije la opcion que quieras "))
            
            if nombre == 1:
                if "Digipyball" in inv.objetos:
                    
                    inv.usar_objeto("Digipyball")

                    elegir = random.randint(1, 100)

                    if elegir <= probabilidad:
                        print("Has capturado al digipymon")
                        jug.añadir_digipymon(pymon)
                    else:
                        print("No has podido capturar al monstruo")
                        print("Ha escapado corre!!: " + str(pymon))
                    bucle = False
                else:
                    print("No te quedan Digipyball")
            elif nombre == 2:
                if jug.digicoins > 0:
                    jug.digicoins -= 1
                    print("Has perdido 1 digicoin")
                    print(f"Tiene un total de:  {jug.consultar_digicoins()} digicoins")

                    bucle = False
                elif jug.digicoins <= 0:
                    print("Debes un total de:  {jug.digicoins} digicoins")

                else:
                    print("No es una opcion valida")

def combate(jugador):
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
            nombre = random.choice(lista_de_nombres.lista_nombres_digipymon)
            vida = random.randint(10, 20)
            ataque = random.randint(0, 9)
            tipo = ["Agua", "Fuego", "Planta"]
            tipoAl = random.choice(tipo)
            nivel = random.randint(0, 3)
            digiEn = Digipymon(nombre, vida, ataque, tipoAl, nivel)
            enemigo1.añadir_digipymon(digiEn)
        
        for x in range(int(jugador.cantidad_digipymon)):
            digi_jugador = jugador.lista_digipymon[x]
            digi_enemigo = enemigo1.lista_digipymon[x]

            if digi_jugador.vida == 0:
                print("Tu digipymon: " + digi_jugador.nombre + " no tiene salud. ¡Pierdes el combate!")
                contadorEn += 1
            elif digi_jugador.ataque > digi_enemigo.ataque:
                print("El digipymon del jugador: " + digi_jugador.nombre + ", supera al digipymon enemigo: " + digi_enemigo.nombre)
                diferencia = digi_jugador.ataque - digi_enemigo.ataque
                digi_jugador.vida -= diferencia
                contadorJug += 1
                if digi_jugador.vida == 0:
                    print("Tu digipymon ha caído en combate!")
            elif digi_jugador.ataque < digi_enemigo.ataque:
                print("El digipymon del jugador: " + digi_jugador.nombre + ", supera al digipymon enemigo: " + digi_enemigo.nombre)
                diferencia = digi_jugador.ataque - digi_enemigo.ataque
                digi_jugador.vida -= diferencia
                contadorEn += 1
                if digi_jugador.vida == 0:
                    print("Tu digipymon ha caído en combate!")
            elif digi_jugador.ataque == digi_enemigo.ataque:
                print("Vuestros digipymon tienen el mismo ataque ¡Es una empate!")
            
        if contadorJug > contadorEn:
            print("Has ganado el combate")
            jugador.digicoins += contadorJug
        elif contadorJug < contadorEn:
            print("Has perdido el combate")
            jugador.digicoins -= contadorEn
        elif contadorJug == contadorEn:
            print("Habéis empatado.") 
        
        if jugador.digicoins <= 0:
            jugador.digicoins = 0

    elif combate == 2:
        print("Has huido. Has perdido una digicoin")
        jugador.digicoins -= 1

        if jugador.digicoins <= 0:
            jugador.digicoins = 0



def digishop(jug, inv):

    print(f"Bienvenido a la mejor tienda {jug.nombre}")
    print(f"Tienes {jug.digicoins} monedas")
    time.sleep(2)

    salir = True

    while salir:
        print("Bienvenido a la tienda: ")
        print("1. Digipyball --> 5 digicoins")
        print("2. Pocion --> 3 digicoins")
        print("3. Anabolizante --> 4 digicoins")
        print("4. salir")

        opcion = int(input("Elije una de las opciones: "))
        
        if opcion == 1:
            if jug.digicoins >= 5:
                jug.digicoins - 5
                inv.añadir_objeto("Digipyball", 1)
                print("Has comprado una Digipyball!!!!")
            else:
                print("No tienes suficientes monedas")
            
        elif opcion == 2:
            if jug.digicoins >= 3:
                jug.digicoins - 3
                inv.añadir_objeto("Pocion", 1)
                print("Has comprado una pocion!!!")
            else:
                print("No tienes suficiente dinero")

        elif opcion == 3:
            if jug.digicoins >= 4:
                jug.digicoins - 4
                inv.añadir_objeto("Anabolizante", 1)
            else:
                print("No tienes suficiente dinero")
            
        elif opcion == 4:
                print("Has salido de la tienda")
                time.sleep(3)
                salir = False

def usar_item(jug, inv):

    print("-----------Inventario-----------")
    print("¿Qué item deseas usar?")
    print("--------------------------------")
    print("1 para usar digipyball")
    print("2 para usar pocion")
    print("3 para usar anabolizante")
    print("--------------------------------")

    objeto_elegido = int(input("Elige el objeto: "))

    if objeto_elegido == 1:
        print("No puedes usar ahora mismo las digipyballs")

    elif objeto_elegido == 2:
        if "Pocion" in inv.objetos:

            inv.usar_objeto("Pocion")

            print(jug.consultar_digipymon())

            aplicarDigipymon = input("Elige el digipymon en el que aplicarlo: ")
            for digipymon in jug.lista_digipymon:
                if digipymon.nombre == aplicarDigipymon:
                    digipymon.vida += 10
                    print("Has usado: Pocion. En: " + str(digipymon) + "!")
                else:
                    print("Ese digipymon no existe")
        else:
            print("No te quedan pociones")

    elif objeto_elegido == 3:
        if "Anabolizante" in inv.objetos:
            inv.usar_objeto("Anabolizante")

            print(jug.consultar_digipymon())
            
            aplicarDigipymon = input("Elige el digipymon en el que aplicarlo: ")
            for digipymon in jug.lista_digipymon:
                if digipymon.nombre == aplicarDigipymon:
                    digipymon.ataque += 4
                    print("Has usado: Pocion. En: " + digipymon + "!")
                else:
                    print("Ese digipymon no existe")
        else:
            print("No tienes anabolizantes")
        
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
    inv.objetos["Digipyball"] = 3
    inv.objetos["Pocion"] = 1

    salir = True

    while salir:
        menu()

        opcion = int(input("Elige que quieres hacer: "))

        if opcion == 1:
            buscar_digipymon(jug, inv)

        elif opcion == 2:
            combate(jug)

        elif opcion == 3:
            digishop(jug, inv)

        elif opcion == 4:
            usar_item(jug, inv)
        
        elif opcion == 5:
            print(inv.objetos)

        elif opcion == 6:
            print("Tus Digipymon son: ")

            print(jug.consultar_digipymon())
        
        elif opcion == 7:
            print("Hasta la proxima!!")
            salir = False

main()