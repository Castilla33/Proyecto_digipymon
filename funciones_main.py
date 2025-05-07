from clase_inventario import clase_inventario
from clase_jugador import clase_jugador 
from clase_lista_nombres import lista_nombre
jugador = clase_jugador()

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
    enemigo1 = clase_enemigo(lista_de_nombres.lista_nombres_entrenadores)
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
    # Las pociones aumentan la vida de un digipymon
    # Los anabolizantes el ataque
    elif objeto_elegido != "Pocion" or "Anabolizantes":
        print("No existe ese objeto")
    else:
        inventario.usar_objeto(objeto_elegido)
        print("Has usado: " + objeto_elegido + "!")

