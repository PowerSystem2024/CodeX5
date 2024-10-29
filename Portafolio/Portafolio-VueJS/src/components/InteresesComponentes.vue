<script>
import Fondolava from './Fondolava.vue'; // Importa el nuevo componente

export default {
  components: {
    Fondolava // Registra el componente
  },
  data() {
    return {
      intereses: [
        'Colaboración en proyectos de código abierto: En CodeX5, contribuimos a mejorar herramientas y librerías populares en GitHub, potenciando nuestras habilidades como desarrolladores.',
        'Desarrollo de videojuegos: Juntos exploramos el mundo de la programación de videojuegos, aplicando nuestras ideas creativas y habilidades técnicas en proyectos conjuntos.',
        'Metodologías ágiles: Implementamos prácticas ágiles en nuestros proyectos grupales, mejorando la comunicación y la eficiencia en el desarrollo de software.',
        'Mentoría y aprendizaje continuo: En CodeX5, nos apoyamos mutuamente para aprender nuevas tecnologías y mejorar nuestras habilidades, compartiendo conocimientos y recursos.'
      ]
    }
  }
}
</script>

<template>
  <div class="intereses-contenedor">
    <!-- Fondo animado dentro del contenedor -->
    <Fondolava /> <!-- Utiliza el componente importado -->

    <!-- Lista de intereses -->
    <ul class="contenedor-lista">
      <li v-for="(interes, index) in intereses" :key="index" class="item">
        {{ interes }}
      </li>
    </ul>
  </div>
</template>

<style scoped>
/* Contenedor principal de intereses */
.intereses-contenedor {
  position: relative;
  width: 100%; /* Asegura que ocupe el 100% de su contenedor padre */
  max-width: 100%; /* Ajusta el ancho máximo para que sea el 100% */
  margin: 2rem auto; /* Centrado con margen superior e inferior */
  padding: 2rem; /* Ajusta el padding para un diseño más limpio */
  border-radius: 10px; /* Esquinas redondeadas */
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2); /* Sombra sutil */
}

/* Fondo animado */
.fondo-animado {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: -1; /* Asegura que el fondo esté detrás del contenido */
}

/* Lista de intereses */
.contenedor-lista {
  list-style-type: none; /* Sin viñetas */
  padding: 0; /* Sin padding en la lista */
  margin: 0; /* Sin margen en la lista */
  color: rgb(255, 255, 255); /* Color de texto */
  font-size: 1.4rem; /* Tamaño de fuente */
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8); /* Sombra de texto sutil */
}

.item {
  margin-bottom: 1rem; /* Espaciado entre elementos */
  line-height: 1.5; /* Mejora la legibilidad */
}
</style>
