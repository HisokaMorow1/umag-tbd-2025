1. Inicializa un repositorio, creando un archivo `.gitignore` que excluya el archivo `TODO.md`. Luego copia el archivo con las instrucciones dentro del repositorio con el nombre `TODO.md`.
2. Crea un primer commit con una página básica en HTML (`index.html`):
   ```html
   <!DOCTYPE html>
   <html>
     <head>
       <title>MyStore - Inicio</title>
     </head>
     <body>
       <h1>Bienvenido a TechStore</h1>
     </body>
   </html>
   ```
3. Crea la rama `feature/products` y añade un commit añadiendo el archivo `products.html`, que presenta una lista de productos:
   ```html
   <!DOCTYPE html>
   <html>
     <head>
       <title>MyStore - Productos</title>
     </head>
     <body>
       <h1>Nuestros productos</h1>
       <ul>
         <li>Laptop</li>
         <li>Teclado mecánico</li>
         <li>Mouse gamer</li>
       </ul>
     </body>
   </html>
   ```
4. Cambia a la rama `main` y luego crea la rama `feature/footer`. Añade un commit añadiendo un pie al archivo `index.html`:
   ```html
   <footer>
     <p>&copy; 2025 My Store</p>
   </footer>
   ```
5. Cambia a la rama `main` y fusiona las ramas `feature/products` y `feature/footer` en ella.
6. En la rama `main`, añade un nuevo commit con un nuevo encabezado a la lista de productos:
   ```html
   <h2>Nuestros productos en oferta</h1>
   ```
7. Cambia a la rama `feature/products` y añade un nuevo commit con un nuevo producto a la lista:
   ```html
   <li>Monitor curvo</li>
   ```
   Luego añade otro commit con un nuevo encabezado al final de la lista:
   ```html
   <h2>Descubre nuestros nuevos productos</h2>
   ```
8. Cambia a la rama `main` y fusiona la rama `feature/products` en ella. Resuelve los conflictos si es necesario.
9. Crea un tag llamado `v1.0` cuando hayas fusionado todas las ramas y hayas verificado que todo funcionó correctamente.
