<script setup>
import { ref } from 'vue';
import python from '/src/components/icons/python.svg';
import java from '/src/components/icons/java.svg';
import js from '/src/components/icons/js.svg';
import html from '/src/components/icons/html.svg';
import css from '/src/components/icons/css.svg';
import react from '/src/components/icons/react.svg';
import vue from '/src/components/icons/vue.svg';
import nodejs from '/src/components/icons/nodejs.svg';
import django from '/src/components/icons/django.svg';
import git from '/src/components/icons/git.svg';
import docker from '/src/components/icons/docker.svg';
import figma from '/src/components/icons/figma.svg';

const habilidades = ref([
  {
    id: 1,
    nombre: 'Lenguajes de Programación',
    habilidades: [
      { id: 1, nombre: 'Python', nivel: 'Avanzado', icono: python },
      { id: 2, nombre: 'Java', nivel: 'Avanzado', icono: java },
      { id: 3, nombre: 'JavaScript', nivel: 'Avanzado', icono: js },
      { id: 4, nombre: 'HTML', nivel: 'Avanzado', icono: html },
      { id: 5, nombre: 'CSS', nivel: 'Avanzado', icono: css }
    ]
  },
  {
    id: 2,
    nombre: 'Frameworks y Librerías',
    habilidades: [
      { id: 1, nombre: 'React JS', nivel: 'Avanzado', icono: react },
      { id: 2, nombre: 'Vue JS', nivel: 'Avanzado', icono: vue },
      { id: 3, nombre: 'Node JS', nivel: 'Avanzado', icono: nodejs },
      { id: 4, nombre: 'Django', nivel: 'Avanzado', icono: django }
    ]
  },
  {
    id: 3,
    nombre: 'Herramientas y Software',
    habilidades: [
      { id: 1, nombre: 'Git', nivel: 'Avanzado', icono: git },
      { id: 2, nombre: 'Docker', nivel: 'Avanzado', icono: docker },
      { id: 3, nombre: 'Figma', nivel: 'Avanzado', icono: figma }
    ]
  }
]);
</script>

<template>
  <div class="skills-contenedor">
    <div v-for="categoria in habilidades" :key="categoria.id" class="skills-categoria">
      <h3>{{ categoria.nombre }}</h3>
      <ul class="skills">
        <li v-for="skill in categoria.habilidades" :key="skill.id" class="skill">
          <img :src="skill.icono" :alt="skill.nombre" />
          <span>{{ skill.nombre }}: <strong>{{ skill.nivel }}</strong></span>
        </li>
      </ul>
    </div>
  </div>
</template>

<style scoped>
.skills-contenedor {
  padding: 2rem;
  background-color: #A0D2EB; /* Fondo azul cielo */
  border-radius: 10px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.5); /* Sombra más intensa */
}

.skills-categoria {
  margin-bottom: 20px;
}

.skills-categoria h3 {
  margin-bottom: 10px;
  font-size: 1.5em;
  color: #005B96; /* Azul profundo para los títulos */
  font-weight: 300; /* Fuente fina */
  border-bottom: 1px solid rgba(0, 91, 150, 0.5); /* Línea azul clara debajo del título */
  padding-bottom: 5px;
}

.skills {
  display: flex;
  justify-content: flex-start; /* Alinear a la izquierda */
  flex-wrap: wrap; /* Permitir que los elementos se ajusten en varias líneas */
  gap: 20px; /* Espaciado entre habilidades */
}

.skill {
  display: flex;
  align-items: center;
  gap: 10px;
  background: #005B96; /* Fondo oscuro */
  padding: 0.5em;
  border-radius: 5px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.5); /* Sombra más intensa */
  transition: background-color 0.3s ease;
  flex: 0 1 calc(20% - 20px); /* Flexibilidad en el tamaño */
  max-width: 150px; /* Máximo ancho para cada habilidad */
}

.skill:hover {
  background-color: #2a0054; /* Cambia el fondo al pasar el mouse */
}

.skill img {
  width: 30px;
  height: 30px;
}

.skill span {
  font-size: 1em;
  color: #f0f0f0; /* Color de texto más claro */
}

@media (max-width: 768px) {
  .skills-categoria h3 {
    text-align: center; /* Centra el título en dispositivos más pequeños */
  }
  
  .skill {
    flex: 0 1 calc(45% - 10px); /* Ajuste de flexibilidad para pantallas más pequeñas */
  }
}
</style>
