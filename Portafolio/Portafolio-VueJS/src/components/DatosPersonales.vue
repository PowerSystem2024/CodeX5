<script setup>
import linkedin from '/src/assets/linkedin_icon.svg';
import instagram from '/src/assets/instagram_icon.svg';
import github from '/src/assets/github_icon.svg';
import cv from '/src/assets/cv_icon.svg';

const title = "CodeX5";
const descripcion = "Grupo de Programación - Tecnicatura Universitaria en Programación, UTN FRSR";
const residencia = "San Rafael, Mendoza, Argentina";
const presentacion = "Hola, bienvenidos a nuestro portafolio de proyectos. Somos CodeX5, un grupo de estudiantes de programación web y móvil.";

const redesSociales = [
  { id: 1, name: "Linkedin", src: linkedin, url: 'https://ar.linkedin.com/' },
  { id: 2, name: "Instagram", src: instagram, url: 'https://instagram.com/' },
  { id: 3, name: "Github", src: github, url: 'https://github.com/orgs/PowerSystem2024/teams/codex5' },
  { id: 4, name: "Curriculum Vitae", src: cv, url: '' },
];
</script>

<template>
  <section class="datos-personales">
    <div class="card">
      <h1>{{ title }}</h1>
      <h2>{{ descripcion }}</h2>
      <p class="presentacion">{{ presentacion }}</p>
      <h4>{{ residencia }}</h4>
      <ul class="container-lista">
        <li v-for="red in redesSociales" :key="red.id">
          <a :href="red.url" target="_blank" rel="noopener noreferrer">
            <img class="icon-redsocial" :src="red.src" width="35" :alt="red.name">
          </a>
        </li>
      </ul>
    </div>
  </section>
</template>

<style scoped>
.datos-personales {
  padding: 2rem 0; /* Espaciado superior e inferior */
}

.card {
  background-color: #A0D2EB; /* Azul Cielo */
  border-radius: 10px;
  padding: 20px; /* Espaciado interno aumentado */
  margin: 20px; /* Espaciado externo aumentado */
  text-align: center;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.5); /* Sombra más intensa */
}

h1 {
  font-size: 2.5rem;
  font-weight: bold;
  color: #005B96; /* Azul Profundo */
  margin-bottom: 0.5rem; /* Espacio debajo del título */
}

h2 {
  font-size: 1.5rem;
  color: #0288D1; /* Azul Real */
  margin-bottom: 1rem; /* Espacio debajo de la descripción */
}

.presentacion {
  font-size: 1.2rem;
  font-weight: 400; /* Peso normal */
  margin-bottom: 1.5rem; /* Espacio debajo de la presentación */
  color: #005B96; /* Azul Profundo */
}

h4 {
  font-size: 1rem;
  color: #00507a; /* Color gris más claro para la residencia */
  margin-bottom: 1.5rem; /* Espacio debajo de la residencia */
}

.container-lista {
  display: flex;
  justify-content: center;
  list-style: none;
  padding: 0;
  margin: 1rem 0; /* Margen superior e inferior */
}

.icon-redsocial {
  background-color: transparent; /* Fondo transparente */
  border-radius: 50%;
  padding: 5px; /* Espaciado interno */
  margin: 0 5px; /* Espacio horizontal entre iconos */
  transition: background-color 0.3s; /* Suave transición */
}

.icon-redsocial:hover {
  background-color: #ffffff; /* Fondo suave al pasar el ratón */
}

/* Media Queries para Responsividad */
@media (max-width: 768px) {
  h1 {
    font-size: 2rem; /* Ajustar el tamaño de fuente del título */
  }

  h2 {
    font-size: 1.3rem; /* Ajustar el tamaño de fuente de la descripción */
  }

  .presentacion {
    font-size: 1rem; /* Ajustar el tamaño de fuente del párrafo */
  }

  .card {
    padding: 15px; /* Reducir el espaciado interno en pantallas pequeñas */
    margin: 10px; /* Reducir el espaciado externo en pantallas pequeñas */
  }

  h4 {
    font-size: 0.9rem; /* Ajustar el tamaño de fuente de la residencia */
  }

  .container-lista {
    flex-wrap: wrap; /* Permitir que los iconos se envuelvan en líneas */
    justify-content: center; /* Centrar los iconos */
  }
}

@media (max-width: 700px) {
  h1 {
    font-size: 1.8rem; /* Ajustar aún más el tamaño de fuente del título */
  }

  h2 {
    font-size: 1.2rem; /* Ajustar aún más el tamaño de fuente de la descripción */
  }

  .presentacion {
    font-size: 0.9rem; /* Ajustar aún más el tamaño de fuente del párrafo */
  }

  h4 {
    font-size: 0.8rem; /* Reducir el tamaño de fuente de la residencia */
  }
}
</style>
