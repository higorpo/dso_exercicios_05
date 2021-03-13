from animal import Animal
from mamifero import Mamifero


class Gato(Mamifero):
    def __init__(self):
        super().__init__(2, 2)

    def miar(self) -> str:
        return self.produzir_som() + " SOM: MIAU"
