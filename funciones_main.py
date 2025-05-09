from clase_inventario import clase_inventario
from clase_jugador import clase_jugador 
from clase_lista_nombres import lista_nombre
from enemigo import Enemigo
from digipymon import Digipymon
jugador = clase_jugador("Juga")

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
    lista_de_nombres = lista_nombre()
    enemigo1 = Enemigo(lista_de_nombres.lista_nombres_entrenadores)
    # Añade al enemigo tantos digipymons como tu tengas
    print("-----------¿Deseas luchar?-----------")
    print("1 para luchar")
    print("2 para huir")

    combate = int(input("¿Que quieres hacer? "))

    if combate == 1:
        # Combate
        print("a")
    elif combate == 2:
        print("Has huido. Has perdido una digicoin")
        jugador.digicoins = jugador.digicoins - 1

        if jugador.digicoins <= 0:
            jugador.digicoins = 0


def usar_item():
    inventario = clase_inventario()
    print("-----------Inventario-----------")
    print("¿Qué item deseas usar?")
    print("--------------------------------")
    print(inventario.objetos)
    print("--------------------------------")
    objeto_elegido = input("Elige el objeto: ")
    if objeto_elegido == "Digipyballs":
        print("No puedes usar ahora mismo las digipyballs")
    elif objeto_elegido != "Pocion" or "Anabolizantes":
        print("No existe ese objeto")
    elif objeto_elegido == "Pocion":
        # Las pociones aumentan la vida de un digipymon
        inventario.usar_objeto(objeto_elegido)
        print("Has usado: " + objeto_elegido + "!")
    elif objeto_elegido == "Anabolizantes"
        # Los anabolizantes el ataque
        inventario.usar_objeto(objeto_elegido)
        print("Has usado: " + objeto_elegido + "!")