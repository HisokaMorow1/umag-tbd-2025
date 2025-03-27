from dataclasses import dataclass
from math import sqrt
numeric = int | float

class Coordenada:
    def __init__(self, x: numeric , y: numeric ):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"Coordenada(x={self.x},y={self.y})"
    
    def __eq__(self, other: "Coordenada") -> bool: #type: ignore
        return self.x == other.x and self.y == other.y
    
    def __add__(self, other: "Coordenada") -> "Coordenada":
        return Coordenada(x=self.x + other.x,y=self.y + other.y)

    def distancia(self, otra_coordenada):
        x_diff = (self.x - otra_coordenada.x)**2
        y_diff = (self.y - otra_coordenada.y)**2

        return (x_diff + y_diff)**0.5

c1 = Coordenada(3,5)
c2 = Coordenada(3,5)

print(c1 + c2)
print(c1 == c2)

print(c1.distancia(c2))

def sumar_numeros(numeros: list[int | float]) -> int | float:
    return sum(numeros)

def contar_ocurrencias(palabras: list[str], palabra: str) -> dict[str,int]:
    resultado: dict[str,int] = {}
    for palabra in palabra:
        resultado[palabra] = resultado.get(palabra,0) + 1
    return resultado

def buscar_elemento(lista: list[int], elemento: int) -> int | None:
    if elemento in lista:
        return lista.index(elemento)
    return None 

@dataclass(eq=True, order=True,frozen=True)
class Punto:
    x: numeric 
    y: numeric 
    def distancia(self, other: "Punto") -> float:
        x_diff = (self.x - other.x)**2
        y_diff = (self.y - other.y)**2

        return (x_diff + y_diff)**0.5
    
p1 = Punto(3,1)
p2 = Punto(3,2)
print(p1)
print(p1 == p2)
print(p1.distancia(p2))
print(sorted([p2,p1]))
