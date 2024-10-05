<script setup>
import NavBar from './components/NavBar.vue';
import DatosPersonales from './components/DatosPersonales.vue';
import Educacion from './components/EducacionComponente.vue';
import ExperienciaComponente from './components/ExperienciaComponente.vue';
import ProyectosComponentes from './components/ProyectosComponentes.vue';
</script>

<template>
   <header>
      <!--Barra de Navegacion-->
      <NavBar />
      <DatosPersonales/>
      <Educacion/>
      <ExperienciaComponente/>
      <ProyectosComponentes/>


   </header>
   <main>
      <section id="educacion">Educacion - Cursos</section>
      <section id="experiencia"><h2>Experiencia</h2></section>
      <section id="proyectos"><h2>Proyectos</h2></section>
      <section id="habilidades"><h2>Habilidades</h2></section>
      <section id="intereses"><h2>Intereses</h2></section>
   </main>
</template>

<style scoped>

</style>
