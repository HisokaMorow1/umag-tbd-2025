from typing import List, Optional

class Libro:
    def __init__(self, titulo: str, autor: str, isbn: str, disponible: bool = True):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible

    def __str__(self) -> str:
        estado = "Disponible" if self.disponible else "No disponible"
        return f"Titulo: {self.titulo}, Autor: {self.autor}, ISBN: {self.isbn}, Estado: {estado}"

    def mostrar_info(self) -> None:
        print(self)

    def prestar(self) -> None:
        if self.disponible:
            self.disponible = False
        else:
            print("El libro no está disponible para préstamo.")

    def devolver(self) -> None:
        self.disponible = True


class Usuario:
    def __init__(self, nombre: str, id_usuario: str):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.prestamos: List[Libro] = []

    def __str__(self) -> str:
        prestamos_titulos = [libro.titulo for libro in self.prestamos]
        return f"Nombre: {self.nombre}, ID: {self.id_usuario}, Préstamos: {prestamos_titulos}"

    def tomar_libro(self, libro: Libro) -> None:
        if libro.disponible:
            libro.prestar()
            self.prestamos.append(libro)
        else:
            print(f"El libro '{libro.titulo}' no está disponible.")

    def devolver_libro(self, libro: Libro) -> None:
        if libro in self.prestamos:
            libro.devolver()
            self.prestamos.remove(libro)
        else:
            print(f"El libro '{libro.titulo}' no está en la lista de préstamos.")


class Biblioteca:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.libros: List[Libro] = []
        self.usuarios: List[Usuario] = []

    def __str__(self) -> str:
        libros_titulos = [libro.titulo for libro in self.libros]
        usuarios_nombres = [usuario.nombre for usuario in self.usuarios]
        return f"Biblioteca: {self.nombre}, Libros: {libros_titulos}, Usuarios: {usuarios_nombres}"

    def agregar_libro(self, libro: Libro) -> None:
        self.libros.append(libro)

    def registrar_usuario(self, usuario: Usuario) -> None:
        self.usuarios.append(usuario)

    def mostrar_libros_disponibles(self) -> None:
        print("Libros disponibles:")
        for libro in self.libros:
            if libro.disponible:
                libro.mostrar_info()

    def buscar_libro_por_titulo(self, titulo: str) -> Optional[Libro]:
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                return libro
        print(f"No se encontró un libro con el título '{titulo}'.")
        return None