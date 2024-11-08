<script setup>
const title = "Ana Castro Nieto"
const descripcion = "Tecnica Universitaria en Programación - UTN"
const residencia = "San Rafael, Mendoza Argentina"
const presentacion = "Hola, Bienvenido a mi portafolio de proyectos, soy desarrolladora web con experiencia en el desarrollo de aplicaciones web y moviles."
const redesSociales = [
    {id:1, name:"Linkedin", src:'/src/assets/linkedin_icon.svg',url:'https://ar.linkedin.com/'},
    {id:1, name:"Instagram", src:'/src/assets/instagram_icon.svg',url:'https://instagram.com/'},
    {id:1, name:"Github", src:'/src/assets/github_icon.svg',url:'https://github.com/'},
    {id:1, name:"CurriculumVitae", src:'/src/assets/cv_icon.svg',url:''},
];
const telefono = "+54 2604651804"
</script>

<template>
<section class="datos-personales">
    <div class="card">
        <h1>{{ title }}</h1>
        <h2>{{ descripcion }}</h2>
        <p>{{ presentacion }}</p>
        <ul class="container-lista">
            <li v-for="red in redesSociales":key="red.id">
                <a href="red.url"><img class="icon-redsocial" :src="red.src" width="35rem" :alt="red.name"></a>
            </li>
        </ul>
        <h3>Mi telefono personal: {{ telefono }}</h3>
        <h4>{{ residencia }}</h4>
    </div>
</section>
</template>

<style scoped>
h1 {
    font-size: 2.5rem;
}

p {
    font-size: 1.2rem;
    font-weight: 600;
    margin-bottom: 1rem;
}

.card {
    background-color: #e1bee7; /* Fondo violeta pastel */
    border-radius: 10px;
    padding: 10px;
    margin: 10px;
    text-align: center;
    color: #4a148c; /* Texto violeta oscuro */
}

.container-lista {
    display: flex;
    justify-content: center;
    list-style: none;
    padding: 0;
    margin: 0;
    text-align: center;
}

.icon-redsocial {
    align-items: center;
    background-color: #f3e5f5; /* Fondo violeta claro */
    border-radius: 50%;
    padding: 2px;
    margin: 5px;
    box-shadow: 0 0 5px rgba(171, 71, 188, 0.7); /* Sombra violeta pastel */
}

.icon-redsocial:hover {
    background-color: #ce93d8; /* Cambio a un violeta más fuerte */
    box-shadow: 0 0 5px rgba(156, 39, 176, 0.8);
}

h3 {
    font-size: 1.2rem;
    font-weight: 600;
}
</style>
