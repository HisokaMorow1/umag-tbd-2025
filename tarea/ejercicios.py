#ejercicio 1

def calculadora(x=5,y=10,resultado=0):
    if resultado == '+':
        return x+y
    elif resultado == '-':
        return x-y
    elif resultado == '*':
        return x*y
    elif resultado == '/':
        if resultado != 0:
            return x/y
        else:
            return "error"
print(calculadora())


#ejercicio 2
def contar(cadena):
    palabra = cadena.split()
    conteo = {}
    for palabra in palabra:
        if palabra in conteo:
            conteo[palabra] += 1
        else:
            conteo[palabra] = 1
    return conteo
 
#ejercicio 3

# def polindromo(frase):
#     frase = frase.lower()
#     inicio = 0
#     final = 0

#     for i in frase:
#         final = 1
#     final -= 1

#     while inicio < final:
#         if frase[inicio] < 'a' or frase[inicio] > 'z' and frase[inicio] < 0 or frase[inicio] > 0:
#             inicio += 1
#         elif:
#         frase[final] < 'a' or frase[final] > 'z' and frase[final] < 0 or frase[final] > 0:
#         final -= 1
#         elif:
#         frase[inicio] != frase[final]
#         return False
#         else:
#         inicio += 1
#         final -= 1
#     return True