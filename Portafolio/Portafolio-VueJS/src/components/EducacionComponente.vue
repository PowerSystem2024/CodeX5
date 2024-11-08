<script setup> 
import { ref } from 'vue';

const fechaColor = ref([
  { color: "#d1c4e9" },
  { color: "#ba68c8" },
  { color: "#7e57c2" },
  { color: "#9575cd" },
  { color: "#ce93d8" }
]);

const educacion = ref([
  { fecha: '2024', title: 'Tecnicatura Universitaria en Programación', descripcion: 'Incumbencias Profesionales: Operación y programación de computadoras, desarrollo de programas en distintos lenguajes, análisis y control de sistemas informáticos.' },
  { fecha: '2023', title: 'Desarrollador Full Stack', descripcion: 'Trabajé en XYZ Tech, donde diseñé y desarrollé aplicaciones web completas utilizando tecnologías como Node.js, React y MongoDB.' },
  { fecha: '2022', title: 'Internship en Desarrollo Web', descripcion: 'Realicé una pasantía en ABC Solutions, contribuyendo en la creación de interfaces de usuario y optimización de sitios web.' },
  { fecha: '2021', title: 'Proyecto Personal - Aplicación de Gestión de Tareas', descripcion: 'Desarrollé una aplicación para la gestión de tareas diarias usando HTML, CSS y JavaScript.' },
  { fecha: '2020', title: 'Curso de Introducción a la Programación', descripcion: 'Completé un curso en línea sobre fundamentos de programación, donde aprendí conceptos básicos.' }
]);
</script>

<template>
  <section id="educacion">
  <h1>Educacion - Cursos</h1>
  <ul>
    <li v-for="(item, index) in educacion" :key="index" :style="{ '--accent-color': fechaColor[index].color }">
      <div class="date">{{ item.fecha }}</div>
      <div class="title">{{ item.title }}</div>
      <div class="descr">{{ item.descripcion }}</div>
    </li>
  </ul>
  <div class="credits"><a target="_blank" href="https://www.freepik.com/free-vector/infographic-template-with-yearly-info_1252895.htm"></a></div>
</section>
</template>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;700&display=swap");

*,
*::before,
*::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  --color: rgba(63, 81, 181);
  --bgColor: #ede7f6;
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

ul::before {
  content: "";
  grid-column: 1;
  grid-row: 1 / span 20;
  background: #b39ddb;
  border-radius: calc(var(--line-w) / 2);
}

ul li:not(:last-child) {
  margin-bottom: var(--row-gap);
}

ul li {
  grid-column: 2;
  --inlineP: 1.5rem;
  margin-inline: var(--inlineP);
  grid-row: span 2;
  display: grid;
  grid-template-rows: min-content min-content min-content;
}

ul li .date {
  --dateH: 3rem;
  height: var(--dateH);
  margin-inline: calc(var(--inlineP) * -1);
  text-align: center;
  background-color: var(--accent-color);
  color: white;
  font-size: 1.25rem;
  font-weight: 700;
  display: grid;
  place-content: center;
  position: relative;
  border-radius: calc(var(--dateH) / 2) 0 0 calc(var(--dateH) / 2);
}

ul li .date::before {
  content: "";
  width: var(--inlineP);
  aspect-ratio: 1;
  background: var(--accent-color);
  background-image: linear-gradient(rgba(0, 0, 0, 0.2) 100%, transparent);
  position: absolute;
  top: 100%;
  clip-path: polygon(0 0, 100% 0, 0 100%);
  right: 0;
}

ul li .date::after {
  content: "";
  position: absolute;
  width: 2rem;
  aspect-ratio: 1;
  background: var(--bgColor);
  border: 0.3rem solid var(--accent-color);
  border-radius: 50%;
  top: 50%;
  transform: translate(50%, -50%);
  right: calc(100% + var(--col-gap) + var(--line-w) / 2);
}

ul li .title,
ul li .descr {
  background: var(--bgColor);
  position: relative;
  padding-inline: 1.5rem;
}

ul li .title {
  overflow: hidden;
  padding-block-start: 1.5rem;
  padding-block-end: 1rem;
  font-weight: 500;
}

ul li .descr {
  padding-block-end: 1.5rem;
  font-weight: 300;
}

ul li .title::before,
ul li .descr::before {
  content: "";
  position: absolute;
  width: 90%;
  height: 0.5rem;
  background: rgba(0, 0, 0, 0.5);
  left: 50%;
  border-radius: 50%;
  filter: blur(4px);
  transform: translate(-50%, 50%);
}

ul li .title::before {
  bottom: calc(100% + 0.125rem);
}

ul li .descr::before {
  z-index: -1;
  bottom: 0.25rem;
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

  ul li:nth-child(2) {
    grid-row: 2/4;
  }

  ul li:nth-child(odd) .date::before {
    clip-path: polygon(0 0, 100% 0, 100% 100%);
    left: 0;
  }

  ul li:nth-child(odd) .date::after {
    transform: translate(-50%, -50%);
    left: calc(100% + var(--col-gap) + var(--line-w) / 2);
  }
  ul li:nth-child(odd) .date {
    border-radius: 0 calc(var(--dateH) / 2) calc(var(--dateH) / 2) 0;
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


