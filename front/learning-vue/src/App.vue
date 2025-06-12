<script setup>
import Card from './components/Card.vue';

const tasks = [
  {title: "Mi tarea", subtitle: "Como utilizar vue"},
  {title: "Otra tarea", subtitle: "Aprender Vue.js"},
  {title: "Tarea adicional", subtitle: "Explorar componentes"}
];

function alertClick(task){
  alert(`click on: ${task}`);
}
</script>

<template>
  <Card v-for="task in tasks" :task="task" @click="alertClick"/>
</template>
<style scoped>
</style>
