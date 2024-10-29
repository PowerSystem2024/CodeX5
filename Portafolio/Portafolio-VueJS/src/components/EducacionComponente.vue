<script setup>
import { ref } from 'vue';

const fechaColor = ref([
  { color: "#7A7A7A" },
  { color: "#BFBFBF" },
  { color: "#D1D1D1" },
  { color: "#A0A0A0" },
  { color: "#8C8C8C" }
]);

const integrantes = ref([
  { nombre: 'Santiago Calzolari', descripcion: 'Desarrollador Frontend, con experiencia en Vue.js y React.' },
  { nombre: 'Ana Castro', descripcion: 'Especialista en bases de datos y desarrollo de backend.' },
  { nombre: 'Leonel Palominos', descripcion: 'Experto en diseño de interfaces y experiencia de usuario.' },
  { nombre: 'Karen Cespedes', descripcion: 'Futura ingeniera de software con pasión por la programación y desarrollo de videojuegos.' },
  { nombre: 'Santino Salatino', descripcion: 'Programador entusiasta que se especializa en aplicaciones móviles.' }
]);
</script>

<template>
  <section id="integrantes">
    
    <ul>
      <li v-for="(integrante, index) in integrantes" :key="index" :style="{ '--accent-color': fechaColor[index].color }">
        <div class="nombre">{{ integrante.nombre }}</div>
        <div class="line"></div>
        <div class="descripcion">{{ integrante.descripcion }}</div>
      </li>
    </ul>
  </section>
</template>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Montserrat:wght@300;500;700&display=swap");
@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;700&display=swap");

*,
*::before,
*::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  --color: rgba(30, 30, 30);
  --bgColor: rgba(245, 245, 245);
  min-height: 100vh;
  display: grid;
  align-content: center;
  gap: 2rem;
  padding: 2rem;
  font-family: "Poppins", sans-serif;
  color: var(--color);
  background: var(--bgColor);
}

h1 {
  text-align: center;
}

ul {
  --col-gap: 2rem;
  --row-gap: 2rem;
  --line-w: 0.25rem;
  display: grid;
  grid-template-columns: var(--line-w) 1fr;
  grid-auto-columns: max-content;
  column-gap: var(--col-gap);
  list-style: none;
  width: min(60rem, 90%);
  margin-inline: auto;
}

/* line */
ul::before {
  content: "";
  grid-column: 1;
  grid-row: 1 / span 20;
  background: #4696ff;
  border-radius: calc(var(--line-w) / 2);
}

/* row gaps */
ul li:not(:last-child) {
  margin-bottom: var(--row-gap);
}

/* card */
ul li {
  grid-column: 2;
  --inlineP: 1.5rem;
  margin-inline: var(--inlineP);
  grid-row: span 2;
  display: grid;
  grid-template-rows: min-content min-content min-content;
}

/* nombre */
ul li .nombre {
  color: var(--color);
  font-family: "Montserrat", sans-serif;
  font-size: 1.5rem; 
  font-weight: 700;
  text-align: center;
  padding: 0.5rem;
  position: relative;
}

/* line under nombre */
ul li .line {
  height: 1px; 
  background: white; 
  margin-top: 0.25rem; 
}

/* descripcion */
ul li .descripcion {
  background: transparent; 
  position: relative;
  padding-inline: 1.5rem;
  font-weight: 300; 
  padding-block-end: 1.5rem;
}

@media (min-width: 40rem) {
  ul {
    grid-template-columns: 1fr var(--line-w) 1fr;
  }
  ul::before {
    grid-column: 2;
  }
  ul li:nth-child(odd) {
    grid-column: 1;
  }
  ul li:nth-child(even) {
    grid-column: 3;
  }

  /* start second card */
  ul li:nth-child(2) {
    grid-row: 2/4;
  }
}

.credits {
  margin-top: 1rem;
  text-align: right;
}

.credits a {
  color: var(--color);
}
</style>
