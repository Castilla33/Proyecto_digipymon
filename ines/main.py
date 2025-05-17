import random
import time
from lista_nombres import Lista
from digipymon import Digipymon
from inventario import Inventario
from jugador import Jugador 
from enemigo import Enemigo

#Función para generar un digipymon aleatorio con atributos aleatorios
def generar_digipymon_aleatorio():
    lista = Lista()
    nombre = lista.obtener_nombre_digipymon() #Se obtiene un nombre aleatorio
    vida = random.randint(10,20) #Vida aleatoria entre 10 y 20
    ataque = random.randint(1,10) #Ataque aleatorio entre 1 y 10
    nivel = random.randint(1,3) #Nivel aleatorio entre 1 y 3
    tipo = random.choice(["fuego", "agua", "planta"]) #Tipo aleatorio
    digi = Digipymon(nombre,vida,ataque,tipo,nivel)

    return digi #Se devuelve el digipymon generado


#Función para mosgtrar el menú principal
def menu():
    print("-----------Menu-----------")
    print("1. Buscar digipymon") #Opción para buscar y capturar digipymon
    print("2. Luchar contra un entrenador") #Opción de combatir
    print("3. Ir a la tienda") #Opción para comprar objetos
    print("4. Usar objetos") #Opción para usar del inventario
    print("5. Consultar inventario") #Muestra el contenido del inventario
    print("6. Consultar digipymons") #Muestra los digipymon del jugador
    print("7. Salir") #Salir del juego


#Función para buscar y capturar digipymon
def buscar_digipymon(jug, inv):
        pymon = generar_digipymon_aleatorio() #Se genera un digipymon aleatorio
        print(f"Has encontrado un Digipymon aleatorio!!!!! " + str(pymon)) #Se muestra el digipymon aleatorio
        probabilidad = 100 - (pymon.nivel * 10) #Calcula la probailidad de captura
        print(f"La probailidad de que captures un digipymon es: {probabilidad}%") #Se dice la probabilidad que tienes
        bucle = True #Se inicia un bucle para las opciones de captura o huida

        while bucle:
            print("Cuidado estas en sitio peligroso ")
            print("1. Captura Digipymon")
            print("2. Rapido huye!!!!")

            #Se solicita al jugador que elija una opción
            nombre = int(input("Elije la opcion que quieras "))
            
            if nombre == 1:
                #Si el jugador tiene digipyballs disponibles
                if "Digipyball" in inv.objetos:

                    #Se usa una digiball
                    inv.usar_objeto("Digipyball")

                    elegir = random.randint(1, 100) #Número aleatorio para comprobar la captura

                    if elegir <= probabilidad:
                        print("Has capturado al digipymon")
                        jug.añadir_digipymon(pymon) #Se añade a la lista del jugador
                    else:
                        print("No has podido capturar al monstruo")
                        print("Ha escapado corre!!: " + str(pymon)) #Mensaje si el digipymon espcapa
                    bucle = False #Se sale del bucle
                else:
                    print("No te quedan Digipyball") #Aviso si no tiene digipyballs
            elif nombre == 2:
                if jug.digicoins > 0:
                    jug.digicoins -= 1 #Se le resta una digicoins por huir
                    print("Has perdido 1 digicoin")
                    print(f"Tiene un total de:  {jug.consultar_digicoins()} digicoins") #Se muestra el total actualizado

                    bucle = False #Se sale del bucle
                elif jug.digicoins <= 0:
                    print("Debes un total de:  {jug.digicoins} digicoins") #Mensaje si tiene digicoins en 0 o menos

                else:
                    print("No es una opcion valida") #Mensaje de opción incorrecta

#Función para simular un combate entre jugador y enemigo
def combate(jugador):
    lista_de_nombres = Lista()   
    enemigo1 = Enemigo(random.choice(lista_de_nombres.lista_nombres_entrenadores)) #Se genera un enemigo aleatorio

    #Le pregunta al jugador si quiere luchar o huir
    print("-----------¿Deseas luchar?-----------")
    print("1 para luchar")
    print("2 para huir")

    #Entrada del jugador para decidir que es lo que quiere hacer
    combate = int(input("¿Que quieres hacer? "))

    if combate == 1: #Si elige luchar
        contadorJug = 0 #Contador de combates ganados por el jugador
        contadorEn = 0 #Contador de combates ganados por el enemigo

        #Se crean digipymon aleatoios para el enemigo, igual al número que riene el jugador
        for i in range(int(jugador.cantidad_digipymon)):
            nombre = random.choice(lista_de_nombres.lista_nombres_digipymon)
            vida = random.randint(10, 20)
            ataque = random.randint(0, 9)
            tipo = ["Agua", "Fuego", "Planta"]
            tipoAl = random.choice(tipo)
            nivel = random.randint(0, 3)
            digiEn = Digipymon(nombre, vida, ataque, tipoAl, nivel) #Se crea un digipymon enemigo
            enemigo1.añadir_digipymon(digiEn) #Se añade a la lista del enemigo
        
        #Se enfrentan los digipymon del jugador contra los del enemigo uno a uno 
        for x in range(int(jugador.cantidad_digipymon)):
            digi_jugador = jugador.lista_digipymon[x]
            digi_enemigo = enemigo1.lista_digipymon[x]

            #Si el digipymon del jugador tiene 0 de vida, se considera derrota
            if digi_jugador.vida == 0:
                print("Tu digipymon: " + digi_jugador.nombre + " no tiene salud. ¡Pierdes el combate!")
                contadorEn += 1
            #Si el digipymon del jugador tiene más ataque
            elif digi_jugador.ataque > digi_enemigo.ataque:
                print("El digipymon del jugador: " + digi_jugador.nombre + ", supera al digipymon enemigo: " + digi_enemigo.nombre)
                diferencia = digi_jugador.ataque - digi_enemigo.ataque
                digi_jugador.vida -= diferencia #El jugador pirde vida igual a la diferencia del ataque
                contadorJug += 1
                if digi_jugador.vida == 0:
                    print("Tu digipymon ha caído en combate!")
            #Si el digipymon del enemifo tiene más ataque
            elif digi_jugador.ataque < digi_enemigo.ataque:
                print("El digipymon del jugador: " + digi_jugador.nombre + ", supera al digipymon enemigo: " + digi_enemigo.nombre)
                diferencia = digi_jugador.ataque - digi_enemigo.ataque
                digi_jugador.vida -= diferencia
                contadorEn += 1
                if digi_jugador.vida == 0:
                    print("Tu digipymon ha caído en combate!")
                    #Si tienen el mismo ataque
            elif digi_jugador.ataque == digi_enemigo.ataque:
                print("Vuestros digipymon tienen el mismo ataque ¡Es una empate!")
            
        #Se compararn los resultados y se dan o se quitan digicoins
        if contadorJug > contadorEn:
            print("Has ganado el combate")
            jugador.digicoins += contadorJug #Se suman digicoins por combates ganados
        elif contadorJug < contadorEn:
            print("Has perdido el combate")
            jugador.digicoins -= contadorEn #Se restan digicoins por combates perdidos
        
        #Si las digicoins bajan de 0, se ajustan a 0
        if jugador.digicoins <= 0:
            jugador.digicoins = 0

    #Si el jugador elige huir
    elif combate == 2: 
        print("Has huido. Has perdido una digicoin")
        jugador.digicoins -= 1 #Se le resta una digicoin cada vez que huya

        #Si el jugador se queda sin digicoins, se ajusta a 0
        if jugador.digicoins <= 0:
            jugador.digicoins = 0



#Función para mostrar la tienda y comprar objetos
def digishop(jug, inv):

    #Muestra un mensaje de bienvenida personalizado con el nombre del jugador que tu le quieras poner
    print(f"Bienvenido a la mejor tienda {jug.nombre}")
    print(f"Tienes {jug.digicoins} monedas")
    time.sleep(2) #Pausa de 2 segundos

    salir = True #Controla el bucle para permanecer en la tienda

    while salir:
        #Muestra el menú de la tienda con los objetos disponibles y sus precios
        print("Bienvenido a la tienda: ")
        print("1. Digipyball --> 5 digicoins")
        print("2. Pocion --> 3 digicoins")
        print("3. Anabolizante --> 4 digicoins")
        print("4. salir")

        #Pedimos al jugador que elija una opción
        opcion = int(input("Elije una de las opciones: "))
        
        if opcion == 1:
            #Si el jugador elige una digiball y tiene suficientes monedas
            if jug.digicoins >= 5:
                jug.digicoins - 5 #No esta restando correstamente
                inv.añadir_objeto("Digipyball", 1) #Se añade 1 digiball al inventario
                print("Has comprado una Digipyball!!!!")
            else:
                print("No tienes suficientes digicoins")
            
        elif opcion == 2:
             #Si el jugador elige una pocion y tiene suficientes monedas
            if jug.digicoins >= 3:
                jug.digicoins - 3 #No esta restando correstamente
                inv.añadir_objeto("Pocion", 1) #Se añade 1 poción al inventario
                print("Has comprado una pocion!!!")
            else:
                print("No tienes suficiente digicoins")

        elif opcion == 3:
            #Si el jugador elige una anabolizante y tiene suficientes monedas
            if jug.digicoins >= 4:
                jug.digicoins - 4 #No esta restando correstamente
                inv.añadir_objeto("Anabolizante", 1) #Se añade 1 anabolizante al inventario
            else:
                print("No tienes suficiente digicoins")
            
        elif opcion == 4:
                #Si el jugador elige salir, se termina el bucle
                print("Has salido de la tienda")
                time.sleep(3) 
                salir = False

#Función para usar objetos del inventario
def usar_item(jug, inv):
    #Muestra el menú de opciones para elegir un objeto a usar
    print("-----------Inventario-----------")
    print("¿Qué item deseas usar?")
    print("--------------------------------")
    print("1 para usar digipyball")
    print("2 para usar pocion")
    print("3 para usar anabolizante")
    print("--------------------------------")

    #El jugador elige qué objeto quiere usar
    objeto_elegido = int(input("Elige el objeto: "))

    if objeto_elegido == 1:
        #Los digyballs no se pueden usar manualmente
        print("No puedes usar ahora mismo las digipyballs")

    elif objeto_elegido == 2:
        #Verifica si el jugador tiene una opción
        if "Pocion" in inv.objetos:

            #Se usa una poción del inventario
            inv.usar_objeto("Pocion") 

            #Muestra los digipymon que tienes
            print(jug.consultar_digipymon())

            aplicarDigipymon = input("Elige el digipymon en el que aplicarlo: ")
            #Busca en la lista de digipymon del jugador
            for digipymon in jug.lista_digipymon:
                if digipymon.nombre == aplicarDigipymon:
                    digipymon.vida += 10 #Aumenta la vida del digipymon
                    print("Has usado: Pocion. En: " + str(digipymon) + "!") #Se muestra el mensaje de que tienes una poción
                else:
                    print("Ese digipymon no existe") #Muestra el mensaje si no coincide el nombre 
        else:
            print("No te quedan pociones") #El jugaador no tiene pociones

    elif objeto_elegido == 3:
        #Verifica si el jugador tiene un anabolizante
        if "Anabolizante" in inv.objetos:
            inv.usar_objeto("Anabolizante") #Se usa un anabolizante del inventario

            print(jug.consultar_digipymon()) #Muestra los digymon disponibles
            
            aplicarDigipymon = input("Elige el digipymon en el que aplicarlo: ")
            for digipymon in jug.lista_digipymon:
                #Busca el digipymon por nombre
                if digipymon.nombre == aplicarDigipymon:
                    digipymon.ataque += 4 #Aumenta el ataque del digipymon
                    print("Has usado: Anabolizante. En: " + digipymon + "!")  #Se muestra el mensaje de que tienes un anabolizante
                else:
                    print("Ese digipymon no existe") 
        else:
            print("No tienes anabolizantes") #El jugador no tiene anabolizantes
        
    else:
        #Si se elije una opción que no existe
        print("No existe ese objeto")


#Función principal que inicia el juego
def main():
    inv = Inventario() 
    #Introducción de la historia del juego
    print("Basado en un juego de cazar digipymon, donde hubo una guerra entre ellos")
    time.sleep(2)
    print("No se sabe como se originó la guerra entre ellos pero...")
    time.sleep(2)
    print("La guerra era entre dos bandas, por lo que se dice")
    time.sleep(2)
    print("Gano una de ellas")
    time.sleep(2)
    #Se pide el nombre del jugador y se crea el objeto Jugador
    nombre = input("Introduce el nombre del entrenador: ")
    jug = Jugador(nombre)
    time.sleep(1)
    print("Al final solo quedo un bando")
    time.sleep(2)
    print("La ciudad se quedo completamente en silencio...")
    #Genera un digipymon aleatorio que será el primero del jugador
    python = generar_digipymon_aleatorio()
    time.sleep(2)
    print("Has obtenido un Digipymon ")
    print("es un: " + str(python))
    #Se añade el digipymon al equipo del jugador
    jug.añadir_digipymon(python)
    #Se dan objetos iniciales al jugador
    print("Has obtenido 3 digipyballs y una pocion")
    inv.objetos["Digipyball"] = 3
    inv.objetos["Pocion"] = 1

    #Variable para controlar el bucle del menú
    salir = True 

    while salir:
        #Se muestra el menú principal
        menu() 

        #El jugador elige una opción
        opcion = int(input("Elige que quieres hacer: "))

        if opcion == 1:
            buscar_digipymon(jug, inv) #Opción para buscar y capturar digipymon

        elif opcion == 2:
            combate(jug) #Opción para iniciar el combate

        elif opcion == 3:
            digishop(jug, inv) #Opción para acceder a la tienda

        elif opcion == 4:
            usar_item(jug, inv) #Opción para usar objetos del inventario
        
        elif opcion == 5:
            print(inv.objetos) #Muestra el inventario

        elif opcion == 6:
            print("Tus Digipymon son: ") #Muestra los digipymon del jugador

            print(jug.consultar_digipymon())
        
        elif opcion == 7:
            print("Hasta la proxima!!") #Mensaje de despedida
            salir = False #Sale del bucle y termina el juego

#Llama a la función principal para iniciar el juego
main() 