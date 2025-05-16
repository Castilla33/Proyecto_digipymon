#Definimos la clase Enemigo
class Enemigo:
    #Método constructor que se ejecuta al crear un nuevo enemigo
    def __init__(self,nombre):
        self.nombre = nombre  #Guarda el nombre del enemigo
        self.lista_digipymon = [] #Lista vacía donde se guardarán los digipymon
        self.cantidad_digipymon = 0 #Contador de digipymon que tiene el enemigo
    
    #Método para añadir un digipymon al enemigo
    def añadir_digipymon(self,digipymon):
        self.lista_digipymon.append(digipymon) #Añade el digipymon a la lista
        self.cantidad_digipymon += 1 #Aumenta en 1 el contador de digipymon

#Crear un objeto enemigo con el nombre "Javi"
enemigo = Enemigo("Javi")
#Imprime el objeto enemigo directamente
print(enemigo)
        