<script setup>
import { ref } from 'vue' ;

const habilidades = ref([
    {
        id: 1, nombre: 'Lenguajes de Programacion', habilidades: [
            { id: 1, nombre: 'JavaScript', nivel: 'Avanzado', icono: '/src/assets/js.svg' },
            { id: 2, nombre: 'Python', nivel: 'Intermedio', icono: '/src/assets/python.svg' },
            { id: 3, nombre: 'HTML/CSS', nivel: 'Avanzado', icono: '/src/assets/html-css.svg' },
            { id: 4, nombre: 'Java', nivel: 'Intermedio', icono: '/src/assets/java.svg' },
            { id: 5, nombre: 'SQL', nivel: 'Intermedio', icono: '/src/assets/sql.svg' }
        ]
    },
    {
        id: 2, nombre: 'Frameworks y Librerías', habilidades: [
            { id: 1, nombre: 'React.js', nivel: 'Avanzado', icono: '/src/assets/react.svg' },
            { id: 2, nombre: 'Vue.js', nivel: 'Intermedio', icono: '/src/assets/vue.svg' },
            { id: 3, nombre: 'Node.js', nivel: 'Avanzado', icono: '/src/assets/node.sv' },
            { id: 4, nombre: 'Django', nvel: 'Intermedio', icono: '/src/assets/django.svg' },
            { id: 5, nombre: 'Bootstrap', nivel: 'Avanzado', icono: '/src/assets/bootstrap.svg' }
        ]
    },
    {
        id: 3, nombre: 'Herramientas y Software', habilidades: [
            { id: 1, nombre: 'Git', nivel: 'Avanzado', icono: '/src/assets/git.svg'},
            { id: 2, nombre: 'Docker', nivel: 'Intermedio', icono: '/src/assets/docker.svg'},
            { id: 3, nombre: 'Cypress', nivel: 'Intermedio', icono: '/src/assets/cypress.svg'},
            { id: 4, nombre: 'Figma', nivel: 'Intermedio', icono: '/src/assets/figma.svg'}, 
            { id: 5, nombre: 'Visual Studio Code', nivel: 'Avanzado', icono: '/src/assets/vsc.svg'}
        ]
    },
    {
        id: 4, nombre: 'Base de Datos', habilidades: [
            { id: 1, nombre: 'MongoDB', nivel: 'Avanzado', icono: '/src/assets/mongodb.svg'},
            { id: 2, nombre: 'MySQL', nivel: 'Intermedio', icono: '/src/assets/mysql.svg'},
            { id: 3, nombre: 'PostgreSQL', nivel: 'Intermedio', icono: '/src/assets/postgresql.svg'}
        ]
    },
    {
        id: 5, nombre: 'Idiomas', habilidades: [
            { id: 1, nombre: 'Español', nivel: 'Nativo', icono: '/src/assets/arg.svg'},
            { id: 2, nombre: 'Ingles', nivel: 'Avanzado (C1)', icono: '/src/assets/eeuu.svg'}
        ]
    }
]);

</script>

<template>

    <div class="skills-contenedor">
        <div v-for="habilidad in habilidades" :key="habilidad.id" class="skills-categoria">
            <h3>{{ habilidad.nombre }}</h3>
            <ul class="skills">
                <li v-for="habilidad in habilidad.habilidades" :key="habilidad.id" class="skill">
                    <img :src="habilidad.icono" :alt="habilidad.nombre">
                    <span>{{ habilidad.nombre }}: {{ habilidad.nivel }}</span>
                </li>
            </ul>
        </div>
    </div>

</template>

<style scoped>

.skills.contenedor {
    padding: 2rem;
    /*Fondo con gradiente*/
    background: linear-gradient(-45deg, #021526, #03346E, #6EACDA, #E2E2B6);
}

.skills-categoria {
    margin-bottom: 20px;
}

.skills-categoria h3 {
    display: flex;
    justify-content: left;
    margin-bottom: 10px;
    font-size: 1.5rem;
    color: aliceblue;
    font-size: 1.5rem;
    font-weight: bold;
}

.skills {
    display: flex;
    justify-content: space-evenly;
    flex-wrap: wrap;
    gap: 20px;
}

.skill {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 10px;
    background-color: rgba(241, 245, 243, 0.856);
    padding: 0.3rem;
    border-radius: 8px;
    box-shadow: 0px 4px 12px rgb(2, 151, 151, 0.936);
    flex: 1 1 200px;
    max-width: 250px;
}

.skill:hover {
    background-color: rgb(2, 151, 151, 0.936);
}

.skill img {
    width: 35px;
    height: 35px;
}

.skill span {
    font-size: 1em;
    color: #333;
}

.skill:hover{
    font-size: 1.3em;
    transition: 2em ease;
}

@media (max-width: 768px) {
    .skills-categoria h3 {
        justify-content: center;
    }

    .skill {
        justify-content: center;
    }
}

</style>