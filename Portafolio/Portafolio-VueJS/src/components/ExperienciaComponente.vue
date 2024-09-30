<script setup>
import { ref } from 'vue';
const titulo = 'Desarrollador Full Stack';
const fecha = 'Desde Enero 2022 / Julio 2024';
const experiencias = ref([
  { id: 1, src: '/src/assets/github_icon.svg', parrafo: 'Lideré un equipo de 5 desarrolladores en la creación de una plataforma de comercio electrónico que incremento las ventas en un 35% durante el primer año' },
  { id: 2, src: 'src/assets/github_icon.svg', parrafo: 'Diseñé y desarrollé aplicaciones web utilizando Node.js, React y MongoDB, logrando reducir el tiempo de carga de las paginas en un 50%' },
  { id: 3, src: 'src/assets/github_icon.svg', parrafo: 'Implementé soluciones de autenticación y autorización, mejorando la seguridad del sitio web y reduciendo los intenteos de acceso no autorizado en un 20%' },
  { id: 4, src: 'src/assets/github_icon.svg', parrafo: 'Colaboré con diseñadores de UX/UI para crear interfaces de usuario atractivas y fáciles de usar, aumentando la satisfaccion del cliente en un 15%' },
  { id: 5, src: 'src/assets/github_icon.svg', parrafo: 'Automatizé procesos de despliegue continuo utilizando Jenkins y Docker, reduciendo los tiempos de despliegue en un 40%' },
]);
</script>

<template>
    <section id="experiencia">
    <div class="card">
      <h3 class="titulo">{{titulo}}</h3>
      <p class="fecha">{{fecha}}</p>
      <ul class="listado">
        <li class="item" v-for="experiencia in experiencias" :key="experiencia.id">
            <img class="imagen-svg" :src="experiencia.src" width="45rem" :alt="experiencia.parrafo">
            <p>{{ experiencia.parrafo }}</p>
        </li>
        <!--<li class="item"><img class="imagen-svg" src="@/assets/cv_icon.svg" width="45rem" alt="">
            Lideré un equipo de 5 desarrolladores en la creación de una plataforma de comercio electrónico que incrementó las ventas en un 35% durante el primer año.
        </li>
        <li class="item"><img class="imagen-svg" src="@/assets/cv_icon.svg" width="45rem" alt="">
            Diseñé y desarrollé aplicaciones web utilizando Node.js, React y MongoDB, logrando reducir el tiempo de carga de las páginas en un 50%.
        </li>
        <li class="item"><img class="imagen-svg" src="@/assets/cv_icon.svg" width="45rem" alt="">
            Implementé soluciones de autenticación y autorización, mejorando la seguridad del sitio web y reduciendo los intentos de acceso no autorizados en un 25%.
        </li>
        <li class="item"><img class="imagen-svg" src="@/assets/cv_icon.svg" width="45rem" alt="">
            Colaboré con diseñadores de UX/UI para crear interfaces de usuario atractivas y fáciles de usar, aumentando la satisfacción del cliente en un 30%.</li>

        <li class="item"><img class="imagen-svg" src="@/assets/cv_icon.svg" width="45rem" alt="">
            Automaticé procesos de despliegue continuo utilizando Jenkins y Docker, reduciendo los tiempos de despliegue en un 40%.
        </li>-->
      </ul>
    </div>
    </section>
  </template>
  
  <style scoped>
.card{
      display: flex;
      flex-direction: column;
      padding: 2rem;
      background-color: rgb(28, 41, 52);
      border-radius: 15px;
}

.titulo{
   font-size: 1.5rem;
   color: coral;
}

.fecha{
   font-size: 1rem;
   color: burlywood;
   margin-bottom: 1rem;
}

.listado{
   display: flex;
   flex-direction: column;
}

.item{
   align-items: center;
   display: flex;
   padding: 1rem;
} 
  </style>