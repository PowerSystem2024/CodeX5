<script setup>
const proyectos = [
  {
    imgSrc: "/src/assets/Codex5-1.jpg",
    titulo: "E-commerce",
    descripcion: "Creé una plataforma de comercio electrónico que incrementó las ventas en un 355% durante el primer año.",
    youtubeLink: "https://youtube.com",
    githubLink: "https://github.com"
  },
  {
    imgSrc: "/src/assets/Codex5-2.jpg",
    titulo: "App de Gestión",
    descripcion: "Desarrollé una aplicación de gestión de tareas para mejorar la productividad en un 40%.",
    youtubeLink: "https://youtube.com",
    githubLink: "https://github.com"
  },
  {
    imgSrc: "/src/assets/Codex5-3.jpg",
    titulo: "App Delivery",
    descripcion: "App prototipo estilo pedidosYa , Rappi, Glovo.",
    youtubeLink: "https://youtube.com",
    githubLink: "https://github.com"
  },
];
</script>

<template>
  <div class="galeria">
    <div class="proyecto" v-for="(proyecto, index) in proyectos" :key="index">
      <img :src="proyecto.imgSrc" :alt="proyecto.titulo">
      <div class="proyecto-info">
        <h3>{{ proyecto.titulo }}</h3>
        <p>{{ proyecto.descripcion }}</p>
        <div class="proyecto-links">
          <a :href="proyecto.youtubeLink" class="btn-ver-mas" target="_blank" rel="noopener noreferrer">Ver Proyecto</a>
          <a :href="proyecto.githubLink" class="github-link" target="_blank" rel="noopener noreferrer">Ver Código GitHub</a>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
 .galeria{
    width: 100%;
    height: 100%;
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
    padding: 20px;
    justify-content: center;
    background: linear-gradient(-45deg, #021526, #03346E, #6eacda, #e2e2b6);
    background-size: 400% 400%;
    animation: gradient 15s ease infinite;
 }

@keyframes gradient{
    0%{
        background-position: 0% 50%;
    }
    50%{
        background-position: 100% 50%;
    }
    100%{
        background-position: 0% 50%;
    }
}

.proyecto{
    display: flex;
    flex-direction: column;
    border: 2px solid #ddd;
    overflow: hidden;
    background-color: #f9f9f9;
    max-width: 222px;
    flex: 1 1 300px;
}

.proyecto img{
    width: 100%;
    height: auto;
    display: block;
}

.proyecto-info{
    padding: 15px;
    text-align: center;
}

.proyecto-info h3{
    margin: 10px 0;
    font-size: 1.3rem;
    color: #333;
}

.proyecto-info p{
    margin: 10px 0;
    font-size: 1em;
    color: #666;
}

.proyecto-links{
    display: flex;
    flex-direction: column;
    gap: 10px;
    margin-top: 10px;
}
</style>
