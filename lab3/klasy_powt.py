from abc import ABC, abstractmethod # klasa abstrakcyjna i metody

class Pojazd:
    def __init__(self, typ):
        self.typ = typ

    def wypiszTyp(self):
        return f"Pojazd typu {self.typ}"
    
# class Pojazd(ABC):
#     @abstractmethod
#     def info(self):
#         pass


class Samochod(Pojazd):
    def __init__(self, typ, marka, model, rok):  # Konstruktor
        super().__init__(typ)  # Poprawne wywołanie konstruktora klasy bazowej
        self.marka = marka
        self.model = model
        self.rok = rok

    def opis(self):
        return f"{super().wypiszTyp()} {self.marka} {self.model} {self.rok}"
    
samochod1 = Samochod("osobowy", "toyota", "corolla", 2005)

print(samochod1.opis())