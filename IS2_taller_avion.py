import os
#*--------------------------------------------------------------------
#* La clase Director orquesta la construcción del objeto indicando 
#* el orden en que deben llamarse sus componentes, los mismos son
#* genéricos y dependerán del builder específico utilizado sus
#* valores concretos
#*--------------------------------------------------------------------
class Director:
   __builder = None
   
   def setBuilder(self, builder):
      self.__builder = builder
	   
   def getAvion(self):
      avion = Avion()
      
      # Primero el body
      body = self.__builder.getBody()
      avion.setBody(body)
      
      # Luego (2) turbinas
      i = 0
      while i < 2:
        turbina = self.__builder.getTurbina()
        avion.attachTurbina(turbina)
        i += 1
        
      # Luego (2) alas
      i = 0
      while i < 2:
        ala = self.__builder.getAla()
        avion.attachAla(ala)
        i += 1
        
      # Finalmente el tren de aterrizaje
      tren_aterrizaje = self.__builder.getTren()
      avion.setTren(tren_aterrizaje)

      # Retorna el vehiculo completo
      return avion

#*----------------------------------------------------------------
#* Esta es la definición de un objeto vehiculo inicializando 
#* todos sus atributos
#*----------------------------------------------------------------
class Avion:
   def __init__(self):
      self.__body = None
      self.__turbinas = list()
      self.__alas = list()
      self.__tren_aterrizaje = None

   def setBody(self, body):
      self.__body = body
      
   def attachTurbina(self, turbina):
      self.__turbinas.append(turbina)

   def attachAla(self, ala):
      self.__alas.append(ala)
      
   def setTren(self, tren_aterrizaje):
      self.__tren_aterrizaje = tren_aterrizaje

   def specification(self):
      print ("body: %s" % (self.__body.material))
      print ("turbinas: %d\'" % (self.__turbinas[0].potencia))
      print ("alas: %d\'" % (self.__alas[0].size))
      print (f"Tren de aterrizaje: {self.__tren_aterrizaje.resistencia}")
      

#*-----------------------------------------------------------------
#* Builder
#* Clase genérica que solo define la interfaz de los métodos que el
#* Builder específico tiene que implementar
#*-----------------------------------------------------------------
class Builder:
	
      def getBody(self): pass
      def getTurbina(self): pass
      def getAla(self): pass
      def getTren(self): pass
#*-----------------------------------------------------------------
#* Esta es la hoja de ruta para construir un Avión
#* Establece instancias para tomar body, turbinas, alas y el tren de aterrizaje
#* estableciendo las partes específicas que deben tener esas partes
#*-------------------------------------------------------
class AvionBuilder(Builder):
   def getBody(self):
      body = Body()
      body.material = "Aluminio"
      return body
   
   def getTurbina(self):
      turbina = Turbina()
      turbina.potencia = 900 # Caballos de fuerza
      return turbina
   
   def getAla(self):
      ala = Ala()
      ala.size = 65 # Metros
      return ala
   
   def getTren(self):
      tren_aterrizaje = Tren()
      tren_aterrizaje.resistencia = 0.9 # Coeficiente de amortiguación
      return tren_aterrizaje
   

#*----------------------------------------------------------------
#* Define partes genéricas para un vehiculo (sin inicializar)
#*----------------------------------------------------------------
class Body:
   material = None
   
class Turbina:
   potencia = None

class Ala:
   size = None

class Tren:
   resistencia = None

#*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=
#* Esta es la estructura main()
#*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=
def main():

#*----------------------------------------------------------------
#* Instancia la clase que será el resultado y la que guiará el 
#* proceso de construcción
#*----------------------------------------------------------------
   avionBuilder = AvionBuilder() # initializing the class
   director = Director()

#*----------------------------------------------------------------
#* Pasa al director la hoja de ruta para construir un Avión
#*----------------------------------------------------------------   
   director.setBuilder(avionBuilder)

#*----------------------------------------------------------------
#* Ordena al director agregar los componentes de un Avión según
#* la hoja de ruta
#*----------------------------------------------------------------
   avion = director.getAvion()

#*---------------------------------------------------------------
#* Finalizada la construcción verifica que sea completa
#*---------------------------------------------------------------
   avion.specification()
   print ("\n\n")

#*----------------------------------------------------------------------
#* Se detecta el entry point y se lo deriva a una sección main() propia
#*----------------------------------------------------------------------
if __name__ == "__main__":
   os.system("clear")
   print("Ejemplo de un patrón de tipo builder aplicado a la construcción de un avion\n")

   main()
