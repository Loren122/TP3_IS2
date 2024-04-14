"""
Libreria para la utilización de clases abstractas.
"""
from abc import ABC, abstractmethod

class FactorialCalculator:
    """
    Clase Singleton para calcular factoriales.

    Esta clase garantiza que solo se cree una instancia y mantiene un diccionario
    para almacenar los factoriales previamente calculados.
    """
    _instance = None
    def __new__(cls):
        """
        Verifica si ya se generó una instancia
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.factorials = {}
        return cls._instance

    def calcular_factorial(self, n):
        """
        Calcula el factorial de un número entero dado.
        """
        if n < 0:
            raise ValueError("El factorial no está definido para números negativos")
        if n in self.factorials:
            return self.factorials[n]
        if n in (0,1):
            self.factorials[n] = 1
            return 1
        else:
            self.factorials[n] = n * self.calcular_factorial(n - 1)
            return self.factorials[n]

# Ejemplo de uso
if __name__ == "__main__":
    try:
        numero = "5" # Aquí va el numero al que le calculamos el factorial
        factorial_calculator = FactorialCalculator()
        resultado = factorial_calculator.calcular_factorial(int(numero))
        print(f"El factorial de {numero} es {resultado}")
    except ValueError:
        print("Por favor, ingresa un número entero válido.")


class CalculadoraFactory:
    """
    Fábrica para crear diferentes tipos de calculadoras de impuestos.
    
    Tipos de calculadoras disponibles:
        - "iva"
        - "iibb"
        - "contrib municipales"
    """
    def crear_calculadora(self, tipo):
        """
        Crea una instancia de la calculadora de impuestos según el tipo especificado.
        """
        if tipo == "iva":
            return CalculadoraIVA()
        elif tipo == "iibb":
            return CalculadoraIngresosBrutos()
        elif tipo == "contrib municipales":
            return CalculadoraContribMunicipales()
        else:
            raise ValueError("Tipo de calculadora no válido.")
        
class CalculadoraIVA:
    """
    Calculadora de impuesto IVA (21%).
    """
    def calcular_impuesto(self, importe_base):
        """
        Calcula el impuesto IVA a partir del importe base.
        """
        # Al importe_base se le agrega el 21%
        return importe_base * 1.21

class CalculadoraIngresosBrutos:
    """
    Calculadora de impuesto Ingresos Brutos (5%).
    """
    def calcular_impuesto(self, importe_base):
        """
        Calcula el impuesto Ingresos Brutos a partir del importe base.
        """
        # Al importe_base se le agrega el 5%
        return importe_base * 1.05

class CalculadoraContribMunicipales:
    """
    Calculadora de impuesto Contribuciones Municipales (1,2%).
    """
    def calcular_impuesto(self, importe_base):
        """
        Calcula el impuesto Contribuciones Municipales a partir del importe base.
        """
        # Al importe_base se le agrega el 1,2%
        return importe_base * 1.012

# Utiliza el patrón Factory para la entrega
class Hamburguesa:
    """
    Clase que define el tipo de hamburguesa e indica como entregarla al cliente
    """
    def __init__(self, tipo_hamburguesa):
        self.tipo_hamburguesa = tipo_hamburguesa
        
    def entregar_hamburguesa(self, entrega_factory):
        """
        Imprime la descripción de la entrega de la hamburguesa.
        """
        entrega = entrega_factory.entregar()
        print(f"Hamburguesa {self.tipo_hamburguesa}: {entrega}")

class EntregaFactory(ABC):
    """
    Clase abstracta para la fábrica de tipos de entrega.
    """
    @abstractmethod
    def entregar(self):
        """
        Método abstracto para obtener la descripción del tipo de entrega.
        """
        pass

class Entrega_mostrador(EntregaFactory):
    def entregar(self):
        """
        Implementación concreta para la entrega en mostrador.
        """
        return "Para retirarla por el mostrador"

class Entrega_cliente(EntregaFactory):
    def entregar(self):
        """
        Implementación concreta para la entrega al cliente.
        """
        return "Siendo retirada por el cliente"

class Entrega_delivery(EntregaFactory):
    def entregar(self):
        """
        Implementación concreta para la entrega por delivery.
        """
        return "Será entregada por delivery"


# Ejemplo de uso
if __name__ == "__main__":
    # Crear una hamburguesa
    hamburguesa = Hamburguesa("con lechuga")

    # Entrega en mostrador
    entrega_mostrador = Entrega_mostrador()
    hamburguesa.entregar_hamburguesa(entrega_mostrador)

    # Entrega al cliente
    entrega_cliente = Entrega_cliente()
    hamburguesa.entregar_hamburguesa(entrega_cliente)

    # Entrega por delivery
    entrega_delivery = Entrega_delivery()
    hamburguesa.entregar_hamburguesa(entrega_delivery)



class Factura:
    """
    Clase para representar una factura.
    """
    def __init__(self, importe: float):
        self.importe = importe
        

class FacturaFactory(ABC):
    """
    Clase abstracta para la fábrica de facturas.

    Define el método abstracto para crear una factura.
    """
    @abstractmethod
    def crear_factura(self) -> Factura:
        pass

class FacturaFactoryIVAResponsable(FacturaFactory):
    """
    Fábrica para crear facturas con IVA Responsable (21%).
    """
    def crear_factura(self, importe: float) -> Factura:
        """
        Crea una factura con IVA Responsable.
        """
        # Cálculo del IVA (21%)
        iva = importe * 0.21
        importe_total = importe + iva
        return Factura(importe_total)

class FacturaFactoryIVANoInscripto(FacturaFactory):
    """
    Fábrica para crear facturas con IVA No Inscripto (sin agregar impuestos).
    """
    def crear_factura(self, importe: float) -> Factura:
        """
        Crea una factura sin agregar impuestos.
        """
        # Lógica para crear una factura con IVA No Inscripto
        return Factura(importe)

class FacturaFactoryIVAExento(FacturaFactory):
    """
    Fábrica para crear facturas con IVA Exento (sin agregar impuestos).
    """
    def crear_factura(self, importe: float) -> Factura:
        """
        Crea una factura con IVA Exento (sin impuestos).
        """
        # Lógica para crear una factura con IVA Exento
        return Factura(importe)

# Ejemplo de uso
def main():
    fabrica = FacturaFactoryIVAResponsable()  # Cambiar según la condición impositiva
    factura = fabrica.crear_factura(1000)
    print(f"Importe total: ${factura.importe:.2f}")

if __name__ == "__main__":
    main()
