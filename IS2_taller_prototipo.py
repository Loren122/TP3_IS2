#*-------------------------------------------------------------------------
#* prototipo.py
#* Ejemplo para creación de prototipos
#*-------------------------------------------------------------------------
from abc import ABC, abstractmethod
import time
from datetime import datetime
import copy
import os

#*-------------------------------------------------------------------------
#* La clase prototipo utilizada como ejemplo puede estar en una librería
#* externa y ser importada.
#* Define los atributos mandatorios y relevantes, simula actividad por
#* medio de retardos
#*-------------------------------------------------------------------------
# Class Creation
class Prototype(ABC):
    # Constructor:
    def __init__(self):
        # Mocking an expensive call
        time.sleep(2) 
        # Base attributes
        self.height = None
        self.age = None
        self.defense = None
        self.attack = None

#*------------------------------------------------------------------------------
#* El método clone() no está definido en el prototipo y mediante @abstractmethod
#* se fuerza a que cualquier instancia que se haga de ésta clase lo tenga que
#* definir.
#*------------------------------------------------------------------------------
    # Clone Method:
    @abstractmethod
    def clone(self):
        pass 

#*------------------------------------------------------------------------------
#* Clase productiva que puedo querer usar como plantilla
#*------------------------------------------------------------------------------
class Shopkeeper(Prototype):
    def __init__(self, height, age, defense, attack):
        super().__init__()
        # Mock expensive call
        time.sleep(2)
        self.height = height
        self.age = age
        self.defense = defense
        self.attack = attack
        # Subclass-specific Attribute
        self.charisma = 30
        
    def __str__(self):
        return f"Comerciante" # Aqui podrian ir sus estadisticas

    def saludo(self):
        """
        Saluda cuando entra a la tienda.
        """
        print("¡Bienvenido, valiente aventurero! ¿En qué puedo ayudarte hoy?")

    def vender_item(self, item_name, precio):
        """
        Vende un artículo mágico al aventurero y actualiza el inventario.
        """
        print(f"¡Aquí tienes tu {item_name}! Por solo {precio} monedas de oro.")

    def ofrecer_busqueda(self, descrip_busqueda):
        """
        Ofrece una búsqueda o misión al aventurero.
        """
        print(f"Escucha. {descrip_busqueda}. ¿Aceptas?")

    def negociar_precio(self, item_name, inicial_precio):
        """
        Negocia el precio de un artículo con el aventurero.
        """
        print(f"¿Qué dices de {inicial_precio} monedas de oro por el {item_name}?")

    def reabastecer_pociones(self, cant):
        """
        Reabastece pociones mágicas en el inventario.
        """
        print(f"Hemos recibido {cant} pociones de curación. ¡llévatelas!")

    def evaluar_rareza(self, item_name, nivel_rareza):
        """
        Evalúa la rareza de un objeto y proporciona información al aventurero.
        """
        if nivel_rareza == "común":
            print(f"Este {item_name} es bastante común. No tiene mucho valor.")
        elif nivel_rareza == "raro":
            print(f"¡Un {item_name} raro! Puedo ofrecerte un buen precio por él.")
        elif nivel_rareza == "legendario":
            print(f"¡Increíble! Este {item_name} es legendario. ¡Espero que lo uses sabiamente!")
        else:
            print(f"No estoy seguro de qué pensar sobre este {item_name}.")
            
    def info_sobre_monstruos(self, monstruo):
        """
        Proporciona información sobre un monstruo específico.
        """
        if monstruo == "dragones":
            print("Los dragones son criaturas majestuosas y poderosas. Tienen aliento de fuego y escamas irrompibles.")
        elif monstruo == "esqueletos":
            print("Los esqueletos son no muertos que vagan por las tumbas. Son vulnerables a la luz y el fuego.")
        else:
            print(f"No tengo mucha información sobre {monstruo}. ¡Ten cuidado ahí fuera!")

    # Implementa el método de clonado mediante una copia de arbol de métodos
    def clone(self):
        return copy.deepcopy(self)

#*-------------------------------------------------------------------------
#* clase 
#* define un atributo específico
#*-------------------------------------------------------------------------
class Warrior(Prototype):
    def __init__(self, height, age, defense, attack):
        super().__init__()
        # Mock expensive call
        time.sleep(2)
        self.height = height
        self.age = age
        self.defense = defense
        self.attack = attack
        # Concrete class attribute
        self.stamina = 60
        self.arma = "Vacío"
        
    def __str__(self):
        return f"guerrero" # Aqui podrian ir sus estadisticas
        
    def ataque_basico(self, objetivo):
        """
        Realiza un ataque básico contra el objetivo especificado.
        """
        return f"Ataque basico a {objetivo}"
    
    def escudo(self):
        """
        Utiliza un escudo para reducir el daño recibido.
        """
        return f"Utiliza un escudo" 

    def regenerar_stamina(self):
        """
        Incrementa gradualmente la stamina con el tiempo.
        """
        return f"Regenerando stamina..."
    
    def entrenar(self):
        """
        Realiza un entrenamiento físico para fortalecer su cuerpo y aumentar la resistencia.
        """
        self.stamina += 10
        return f"¡Entrenamiento completado! Stamina actual: {self.stamina}"
    
    def equip_arma(self, arma_nueva):
        """
        Cambia el arma actual del guerrero por una nueva.
        """
        self.arma = arma_nueva
        return f"Utilizando: {self.arma}"
    
    def grito_batalla(self):
        """
        Emite un grito de batalla para inspirar a los aliados y asustar a los enemigos.
        """
        return "AHHHHGGGG"
        
    # Overwriting Cloning Method
    def clone(self):
        return copy.deepcopy(self)
    
    

#*--------------------------------------------------------------------------
class Mage(Prototype):
    def __init__(self, height, age, defense, attack):
    # Call superclass constructor, time.sleep() and assign base values
        super().__init__()
        # Mock expensive call
        time.sleep(2)
        self.height = height
        self.age = age
        self.defense = defense
        self.attack = attack
        # Concrete class attribute
        self.mana = 100
        
    def __str__(self):
        return f"mago" # Aqui podrian ir sus estadisticas

    def lanzar_fireball(self, objetivo):
        """
        Lanza una bola de fuego al objetivo especificado.
        """
        return f"Bola de fuego lanzada a {objetivo}"

    def lanzar_hechizo_curac(self, objetivo):
        """
        Lanza un hechizo de curación al objetivo especificado.
        """
        return f"Hechizo de curacíon lanzado a {objetivo}"

    def ataque_especial(self, objetivo):
        """
        Realiza un ataque especial único contra el objetivo.
        """
        return f"Ataque especial lanzado a {objetivo}"

    def regenerar_mana(self):
        """
        Incrementa gradualmente el maná con el tiempo.
        """
        return f"Regenerando maná..."

    def verif_nivel(self):
        """
        Verifica el nivel del mago y devuelve un mensaje apropiado.
        """
        if self.age >= 18 and self.defense >= 50:
            return "Mago de alto nivel"
        else:
            return "Mago en entrenamiento"

    def incrementar_defensa(self, cant):
        """
        Aumenta la defensa del mago en la cantidad especificada.
        """
        self.defense += cant

    def incrementar_ataque(self, cant):
        """
        Aumenta el ataque del mago en la cantidad especificada.
        """
        self.attack += cant

    # Overwriting Cloning Method
    def clone(self):
        return copy.deepcopy(self)

#*--------------------------------------------------------------------------
#* Punto de entrada de ejecución
#*--------------------------------------------------------------------------
print("Ejemplo de taller para patrón prototipo")

#*--------------------------------------------------------------------------
dt = datetime.now()
print('Creando un objeto Shopkeeper NPC: ', dt)
shopkeeper = Shopkeeper(180, 22, 5, 8)

dt = datetime.now()
print('Finaliza la creación del objeto Shopkeeper NPC: ', dt)
print('Atributos: ' + ', '.join("%s: %s" % item for item in vars(shopkeeper).items()))

# Interaccion de shopkeeper
shopkeeper.saludo()
shopkeeper.ofrecer_busqueda("Hay un tesoro oculto en las montañas")

#*--------------------------------------------------------------------------
dt = datetime.now()
print('Creando un objeto Mage NPC: ', dt)
mage = Mage(172, 65, 8, 15)

dt = datetime.now()
print('Finaliza la creación del objeto Mage NPC: ', dt)
print('Atributos: ' + ', '.join("%s: %s" % item for item in vars(mage).items()))

#*--------------------------------------------------------------------------
dt = datetime.now()
print('Creando un objeto Warrior NPC: ', dt)
warrior = Warrior(185, 22, 4, 21)

dt = datetime.now()
print('Finaliza la creación del objeto Warrior NPC: ', dt)
print('Atributos: ' + ', '.join("%s: %s" % item for item in vars(warrior).items()))

# Interacción de los personajes

print(warrior.grito_batalla())
print(warrior.ataque_basico(mage))
print(mage.lanzar_hechizo_curac(mage))
print(mage.lanzar_fireball(warrior))


# dt = datetime.now()
# print('Puedo hacerlo masivamente con 10 NPCs: ', dt)
# shopkeeper_template = Shopkeeper(180, 22, 5, 8)
# warrior_template = Warrior(185, 22, 4, 21)
# mage_template = Mage(172, 65, 8, 15)
# for i in range(3):
#     shopkeeper_clone = shopkeeper_template.clone()
#     warrior_clone = warrior_template.clone()
#     mage_clone = mage_template.clone()
#     dt = datetime.now()
#     print(f'Finaliza la creación de tripletes mediante clone {i} at: ', dt)

# dt = datetime.now()
# print('Finalizó la creación de la población NPC: ', dt)
