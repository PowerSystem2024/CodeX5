<script setup>
import NavBar from './components/NavBar.vue';
import DatosPersonales from './components/DatosPersonales.vue';
import Educacion from './components/EducacionComponente.vue';
import ExperienciaComponente from './components/ExperienciaComponente.vue';
import ProyectosComponentes from './components/ProyectosComponentes.vue';
import HabilidadesComponente from './components/HabilidadesComponente.vue';
import InteresesComponente  from './components/InteresesComponente.vue';
</script>

<template>
   <header id="top">
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
      <section id="habilidades">
         <h2>Habilidades</h2>
         <HabilidadesComponente />
      </section>
      <section id="intereses"><h2>Intereses</h2></section>
      <InteresesComponente/>
   </main>
   <footer>
      <a href="#top">Inicio</a>
      <p> &reg; 2024 Santiago Calzolari - Portafolio Web</p>
   </footer>
</template>

<style scoped>

   footer {
      display: flex;
      flex-direction: column;
      align-items: center;
      padding: 2rem;
      font-size: 1.3rem;
   }

   footer a{
      color:rgb(25, 86, 136);
      text-decoration: double;
      font-size: 1.4rem;
   }

   footer a:hover{
      color:rgb(28, 41, 52);
      scale: 105%;
   }
</style>
