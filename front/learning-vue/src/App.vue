<script setup>
import { ref } from 'vue'

const message = "Hola"
const titleClass = ref("myclass")
const showTitle = ref(true)
let elements = ref(["Pan", "Yogurt", "Queso"]) 
const name = ref("asdasd")
const newElement = ref("")

const addElement = () =>
{
  elements.value.push(newElement.value)
  newElement.value = ""
}

</script>

<template>
  <input v-model="name"></input>
  <button @click="showTitle = !showTitle">Mostrar Titulo</button>
  <h1 id="message" v-if="showTitle">{{ message }} {{ name }}</h1>
  <h1 v-else :class="titleClass">Otro mensaje</h1>
  <ul>
    <li v-for="elem in elements"> {{ elem }} </li>
  </ul>
  <input v-model="newElement" placeholder="Nuevo elemento"></input>
  <button @click="addElement">Agregar a la lista</button>
</template>

<style scoped>
#message {
  color: purple;
}
.myclass {
  text-decoration: underline dashed green 5pt;
  color: blue;
}
.myclass2 {
  text-decoration: underline dashed green 5pt;
  color: brown;
}
</style>