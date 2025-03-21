import random
import string

#ejercicio 1

x = random.randint(1, 100)
y = random.randint(1, 100)

def calculadora(x, y, operacion):
    if operacion == '+':
        return x + y
    elif operacion == '-':
        return x - y
    elif operacion == '*':
        return x * y
    elif operacion == '/':
        if y != 0:
            return x / y
        else:
            return "error: division por cero"
    else:
        return "operacion no valida"

print(calculadora(x, y, '+'), calculadora(x, y, '-'), calculadora(x, y, '*'), calculadora(x, y, '/'))

#ejercicio 2

def contar_palabras(texto):
    palabras = texto.lower().split()
    conteo = {}
    
    for palabra in palabras:
        palabra = palabra.strip(".,!?()[]{}:;\"'")
        if palabra:
            conteo[palabra] = conteo.get(palabra, 0) + 1
    return conteo

texto = "ana y juan y juan y ana estan juntos"
print(contar_palabras(texto))

#ejercicio 3

def es_palindromo(frase):
    frase = ''.join(char.lower() for char in frase if char.isalnum())

    return frase == frase[::-1]

frase = "Anita lava la tina"
print(es_palindromo(frase))

frase = "Hola mundo"
print(es_palindromo(frase)) 

#ejercicio 4

def generar_contrasena(longitud, incluir_mayusculas=True, incluir_numeros=True, incluir_simbolos=True):
    caracteres = string.ascii_lowercase
    if incluir_mayusculas:
        caracteres += string.ascii_uppercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_simbolos:
        caracteres += string.punctuation
    
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

longitud = 12
print(generar_contrasena(longitud))
print(generar_contrasena(longitud, incluir_mayusculas=False))
print(generar_contrasena(longitud, incluir_numeros=False))
print(generar_contrasena(longitud, incluir_simbolos=False))
print(generar_contrasena(longitud, incluir_mayusculas=False, incluir_numeros=False, incluir_simbolos=False))

#ejercicio 5

def convertir_temperatura(temperatura, unidad):
    if unidad == 'C':
        return (temperatura * 9/5) + 32
    elif unidad == 'F':
        return (temperatura - 32) * 5/9
    else:
        return "Unidad no valida"

temp_celsius = 25
temp_fahrenheit = 77

print(f"{temp_celsius}°C en Fahrenheit es: {convertir_temperatura(temp_celsius, 'C')}°F")
print(f"{temp_fahrenheit}°F en Celsius es: {convertir_temperatura(temp_fahrenheit, 'F')}°C")

#ejercicio 6

# Version iterativa
def fibonacci_iterativo(n):
    secuencia = []
    a, b = 0, 1
    while a <= n:
        secuencia.append(a)
        a, b = b, a + b
    return secuencia

# Version recursiva
def fibonacci_recursivo(n, a=0, b=1, secuencia=None):
    if secuencia is None:
        secuencia = []
    if a > n:
        return secuencia
    secuencia.append(a)
    return fibonacci_recursivo(n, b, a + b, secuencia)

n = 100
print(f"Secuencia de Fibonacci hasta {n} (iterativa): {fibonacci_iterativo(n)}")
print(f"Secuencia de Fibonacci hasta {n} (recursiva): {fibonacci_recursivo(n)}")

#ejercicio 7

def contar_vocales_consonantes(cadena):

    vocales = "aeiouáéíóúü"
    consonantes = "bcdfghjklmnpqrstvwxyz"
    
    num_vocales = 0
    num_consonantes = 0
    
    for char in cadena.lower():
        if char in vocales:
            num_vocales += 1
        elif char in consonantes:
            num_consonantes += 1
    
    return num_vocales, num_consonantes

cadena = "Hola, ¿como estas?"
vocales, consonantes = contar_vocales_consonantes(cadena)
print(f"Vocales: {vocales}, Consonantes: {consonantes}")

#ejercicio 8

def adivinar_numero():
    numero_aleatorio = random.randint(1, 100)
    intentos = 0
    adivinado = False

    print("Adivina el numero entre 1 y 100")

    while not adivinado:
        intento = int(input("Introduce tu intento: "))
        intentos += 1

        if intento < numero_aleatorio:
            print("El numero es mayor")
        elif intento > numero_aleatorio:
            print("El numero es menor")
        else:
            adivinado = True
            print(f"¡Felicidades! Adivinaste el numero en {intentos} intentos.")

adivinar_numero()