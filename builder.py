from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

class Builder(ABC):
    """
    The Builder interface specifies methods for creating the different parts of
    the Product objects.
    """

    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def produce_part_a(self) -> None:
        pass

    @abstractmethod
    def produce_part_b(self) -> None:
        pass

    @abstractmethod
    def produce_part_c(self) -> None:
        pass
    
    @abstractmethod
    def produce_part_d(self) -> None:
        pass
    
    @abstractmethod
    def produce_part_e(self) -> None:
        pass
    
    @abstractmethod
    def produce_part_f(self) -> None:
        pass


class AvionBuilder(Builder):
    """
    Implementación concreta del Builder para ensamblar un avión.
    """

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Avion()

    @property
    def product(self) -> Avion:
        avion = self._product
        self.reset()
        return avion

    def produce_part_a(self) -> None:
        self._product.add("Body del Avión")

    def produce_part_b(self) -> None:
        self._product.add("Turbina Izquierda")
        
    def produce_part_c(self) -> None:
        self._product.add("Turbina Derecha")

    def produce_part_d(self) -> None:
        self._product.add("Ala Izquierda")
        
    def produce_part_e(self) -> None:
        self._product.add("Ala Derecha")
        
    def produce_part_f(self) -> None:
        self._product.add("Tren de Aterrizaje")


class Avion():
    """
    Representa el producto final: un avión.
    """

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Partes del avión: {', '.join(self.parts)}", end="")


class Director:
    """
    The Director is only responsible for executing the building steps in a
    particular sequence. It is helpful when producing products according to a
    specific order or configuration. Strictly speaking, the Director class is
    optional, since the client can control builders directly.
    """

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        """
        The Director works with any builder instance that the client code passes
        to it. This way, the client code may alter the final type of the newly
        assembled product.
        """
        self._builder = builder

    """
    The Director can construct several product variations using the same
    building steps.
    """

    def build_minimal_viable_product(self) -> None:
        self.builder.produce_part_a()

    def build_full_featured_product(self) -> None:
        self.builder.produce_part_a()
        self.builder.produce_part_b()
        self.builder.produce_part_c()
        self.builder.produce_part_d()
        self.builder.produce_part_e()
        self.builder.produce_part_f()

    def build_parcial(self) -> None:
        self.builder.produce_part_b()

if __name__ == "__main__":
    """
    The client code creates a builder object, passes it to the director and then
    initiates the construction process. The end result is retrieved from the
    builder object.
    """

    director = Director()
    builder = AvionBuilder()
    director.builder = builder

    print("Standard basic product: ")
    director.build_minimal_viable_product()
    builder.product.list_parts()

    print("\n")

    print("Standard full featured product: ")
    director.build_full_featured_product()
    builder.product.list_parts()

    print("\n")

    print("Producto especial para la clase UADER SWEII")
    director.build_parcial()
    builder.product.list_parts()

    print("\n")

    # Remember, the Builder pattern can be used without a Director class.
    print("Custom product: ")
    builder.produce_part_a()
    builder.produce_part_b()
    builder.produce_part_c()
    builder.produce_part_d()
    builder.produce_part_e()
    builder.produce_part_f()
    builder.product.list_parts()

    print("\n")
