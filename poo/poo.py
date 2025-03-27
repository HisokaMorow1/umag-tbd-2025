class Animal:
    def __init__(self, especie, edad, color="negro"):
        self.color = color
        self.especie = especie
        self.edad = edad

    def __repr__(self):
        return f"Animal(especie={self.especie},edad={self.edad},color={self.color})"

    def hacer_sonido(self):
        print(f"El animal de especie {self.especie} hace un sonido")


class AnimalEntrenado(Animal):
    def __init__(self, nivel_de_entrenamiento, especie, edad, color="negro"):
        super().__init__(especie, edad, color)
        self.nivel_de_entrenamiento = nivel_de_entrenamiento

    def hacer_truco(self):
        if self.nivel_de_entrenamiento == 1:
            print("Dar la pata")
        if self.nivel_de_entrenamiento == 2:
            print("Hacerse el muerto")
        if self.nivel_de_entrenamiento == 3:
            print("Dar ")


# class MascotaEntrenada(Mascota,AnimalEntrenado):


class Mascota(Animal):
    def __init__(self, nombre, especie, edad, color="negro"):
        super().__init__(especie, edad, color)
        self.nombre = nombre

    def __repr__(self):
        return f"Animal(nombre={self.nombre},especie={self.especie},edad={self.edad},color={self.color})"

    def presentar(self):
        print("Hola esta es mi mascota {self.nombre}")


perro = Animal(especie="perro", edad="5")
bobby = Mascota(nombre="Bobby", especie="perro", edad="1", color="blanco")
print(bobby)
print(perro)
perro.hacer_sonido()

