<script setup>
const props = defineProps({
    task: Object,
})
const emit = defineEmits(['click'])
const a="A"
</script>

<template>
    <div class="card">
        <div class ="card-title">
            <h3>{{ props.task?.title }}</h3>
        </div>
        <div class = "card-body">
            <p>{{ props.task?.subtitle }}</p>
            <input type ="text" />
            <button @click="emit('click', a)">Click</button>
        </div>  
    </div>
</template>

<style lang="css" scoped>
.card {
  background-color: #f9f9f9; /* Color de fondo claro */
  border: 1px solid #ddd; /* Borde gris claro */
  border-radius: 8px; /* Bordes redondeados */
  padding: 16px; /* Espaciado interno */
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* Sombra ligera */
  max-width: 300px; /* Ancho máximo */
  margin: 16px auto; /* Centrar la tarjeta */
  transition: transform 0.3s ease, box-shadow 0.3s ease; /* Animación suave */
}

.card:hover {
  transform: scale(1.05); /* Aumentar ligeramente el tamaño */ 
  box-shadow: 0 8px 12px rgba(0, 0, 0, 0.2); /* Sombra más pronunciada */
}

.card h3 {
  font-size: 1.5rem; /* Tamaño de fuente del título */
  margin-bottom: 8px; /* Espaciado debajo del título */
  background-color: #000; /* Fondo negro */
  color: #fff; /* Texto blanco */
  padding: 8px; /* Espaciado interno */
  border-radius: 4px; /* Bordes redondeados */
}
.card p {
  font-size: 1rem; /* Tamaño de fuente del subtítulo */
  color: #555; /* Color de texto gris oscuro */
}
</style>