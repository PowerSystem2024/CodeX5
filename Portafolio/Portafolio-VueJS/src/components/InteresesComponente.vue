<script setup>

import FondoLava from './FondoLava.vue';
import {ref} from 'vue';
//Este es un arreglo con ref para que se pueda reactivar el cambio de los intereses
const intereses = ref([
    'Deportes: Disfruto del trabajo en equipo en fútbol, la relajación de la natación y el ejercicio al aire libre que ofrece el running.',
    'Tecnología: Me apasiona crear soluciones innovadoras, explorar nuevas tecnologías y aprovechar la impresión 3D para proyectos creativos y prácticos.',
    'Viajes: Me encanta explorar culturas, paisajes, y disfrutar de la aventura de viajar como mochilero, descubriendo lugares auténticos y conectando con personas locales.'
]);
</script>

<template>
    <div class="intereses-contenedor">
        <FondoLava/>
        <ul class="contenedor-lista">
            <li class="item" v-for="interes in intereses" :key="interes"> 
                {{ interes }}
            </li>
        </ul>
    </div>
    <!--
    <div class="intereses-contenedor">
        <FondoLava/>
        <ul class="contenedor-lista">
            <li class="item">
                Deportes: Futbol, Natación, Running
            </li>
            <li class="item">
                Tecnología: Desarrollo de software, Impresión 3D, IA
            </li>
            <li class="item">
                Viajes: Europa, Sudamérica, Mochilero
            </li>
        </ul>
    </div>
    -->
</template>

<style scoped>
.intereses-contenedor{
    display: flex;
    position: relative;
    margin: 0 auto;
    max-width: 85%;
    padding: 1rem;
}

.contenedor-lista{
    position: absolute;
    align-content: center;
    list-style-type: none;
    padding: 1rem;
    margin-bottom: .5rem;
    color:rgb(28, 41, 52);
    font-size: 1.4rem;
    text-shadow: 3px 3px 6px rgba(0,0,0,1);
}

.item{
    margin-bottom: 1rem;
}


</style>