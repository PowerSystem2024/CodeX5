<script setup>
import flecha from '/src/assets/addgente.svg';
import { ref } from 'vue';
const titulo = 'Experiencia en CodeX5';
const fecha = 'Desde Abril 2024 / Diciembre 2024';
const experiencias = ref([
  { id: 1, src: flecha, parrafo: 'Colaboramos como equipo en el desarrollo de aplicaciones innovadoras, utilizando metodologías ágiles que mejoraron la eficiencia en nuestros proyectos.' },
  { id: 2, src: flecha, parrafo: 'Diseñamos interfaces intuitivas y amigables para el usuario, asegurando la satisfacción de quienes utilizan nuestras aplicaciones.' },
  { id: 3, src: flecha, parrafo: 'Implementamos soluciones efectivas para la gestión de datos, optimizando el rendimiento de nuestras aplicaciones y asegurando su escalabilidad.' },
  { id: 4, src: flecha, parrafo: 'Fomentamos un ambiente de trabajo colaborativo y comunicativo entre los miembros del grupo, fortaleciendo así nuestra capacidad de trabajo en equipo.' },
  { id: 5, src: flecha, parrafo: 'Contribuimos en la capacitación de nuevos integrantes, compartiendo conocimientos y mejores prácticas para el desarrollo de proyectos.' },
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
      </ul>
    </div>
  </section>
</template>

<style scoped>
.card {
  display: flex;
  flex-direction: column;
  padding: 2rem;
  background-color: #A0D2EB; /* Azul Cielo */
  border-radius: 15px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.5); /* Sombra más intensa */
}

.titulo {
  font-size: 1.5rem;
  color: #005B96; /* Azul Profundo */
  text-align: center; /* Centrar título */
}

.fecha {
  font-size: 1rem;
  color: #0288D1; /* Azul Real */
  margin-bottom: 1rem;
  text-align: center; /* Centrar fecha */
}

.listado {
  display: flex;
  flex-direction: column;
}

.item {
  align-items: flex-start; /* Alinear a la izquierda */
  display: flex;
  padding: 1rem;
  padding-left: 0; /* Eliminar padding izquierdo */
  border-bottom: 1px solid rgba(255, 255, 255, 0.2); /* Línea sutil entre ítems */
}

.item:last-child {
  border-bottom: none; /* Quitar la línea del último ítem */
}

.imagen-svg {
  margin-right: 1rem; /* Espacio entre la imagen y el texto */
  filter: brightness(0) invert(1); /* Invertir colores de la imagen */
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
