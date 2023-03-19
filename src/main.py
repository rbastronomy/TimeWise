print("Hola Mundo")

class Animal:
    def __init__(self, especie, peso):
        self.especie = especie
        self.peso = peso

    def Sonido(self):
        print("A")
class Gato(Animal):
    def __init__(self, especie, peso):
        super().__init__(especie, peso)
    def Sonido(self):
        print("Meow")


Animalia = Animal("Gato", 4) 
Animalia.Sonido()
Gatito = Gato("Gato", 4)
Gatito.Sonido()