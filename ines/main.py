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


def main():
    print("Basado en un juego de cazar monstruos, donde hubo una guerra entre ellos")
    time.sleep(2)
    print("No se sabe como se originó la guerra entre ellos pero...")
    time.sleep(2)
    print("La guerra era entre dos bandas, por lo que se dice")
    time.sleep(2)
    print("Gano una de ellas")
    time.sleep(2)
    nombre = input("Introduce el nombre de los monstruos: ")
    Objeto = Jugador1(nombre)
    time.sleep(1)
    print("Al final solo quedo un bando")
    time.sleep(2)
    print("La ciudad se quedo completamente en silencio...")
    python = generar_digipymon_aleatorio()
    time.sleep(2)
    print("Has obtenido un Digipymon ")
    print("es un: " + str(python))
    JugadorObjeto.añadir_digipymon(python)
    print("Has obtenido 3 digipyballs y una pocion")
    inventario_objeto.agregar_objeto("Digyballs", 3)
    inventario_objeto.agregar_objeto("Pocion", 1)
    inventario_objeto.mostrar_inventario()

    salir = True
    while salir:
        opcion = menu()

        if opcion == 1:
            buscar-digipymon(JugadorObjeto, inventariObjeto)

        elif opcion == 2:
            print("No puedes luchar")

        elif opcion == 3:
            print("Todavia no se ha usado en la tienda")

        elif opcion == 4:
            InventarioObjeto.mostrar_inventario()
            objeto = input("¿Que objeto quieres usar?: ")
            InventarioObjeto.usar_objetos(objeto)
        elif opcion == 5:
            print("Tu inventario es:")

        elif opcion == 6:
            prin("Tus Digipymon son: ")

            JugadorObjeto.consultar_digipymon()
        
        elif opcion == 7:
            print("Hasta la proxima!!")
            bucle = False
main()





    
    

    
    
        


    


    


    


    