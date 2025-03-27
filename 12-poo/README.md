# Ejercicio: Sistema de Gestión de Biblioteca
**Objetivo**: Implementar un sistema que permita gestionar libros, usuarios y préstamos en una biblioteca utilizando programación orientada a objetos en Python con anotaciones de tipos.

## Clases requeridas
### Libro

**Atributos:** titulo, autor, isbn, disponible (bool)

**Métodos:**

`mostrar_info()`: imprime la información del libro.

`prestar()`: marca el libro como no disponible.

`devolver()`: marca el libro como disponible.

### Usuario

**Atributos:** nombre, id_usuario, prestamos (lista de libros)

**Métodos:**

`tomar_libro(libro)`: añade el libro a la lista de préstamos (si está disponible).

`devolver_libro(libro)`: lo elimina de la lista de préstamos y lo marca como disponible.

### Biblioteca

**Atributos:** nombre, libros (lista de objetos Libro), usuarios (lista de objetos Usuario)

**Métodos:**

`agregar_libro(libro)`

`registrar_usuario(usuario)`

`mostrar_libros_disponibles()`

`buscar_libro_por_titulo(titulo)`