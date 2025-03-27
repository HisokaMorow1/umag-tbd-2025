class Coordenada:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"Coordenada(x={self.x},y={self.y})"
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __add__(self, other):
        return Coordenada(x=self.x + other.x,y=self.y + other.y)

    def distancia(self, otra_coordenada):
        x_diff = (self.x - otra_coordenada.x)**2
        y_diff = (self.y - otra_coordenada.y)**2

        return (x_diff + y_diff)**0.5

c1 = Coordenada(3,5)
c2 = Coordenada(3,6)

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