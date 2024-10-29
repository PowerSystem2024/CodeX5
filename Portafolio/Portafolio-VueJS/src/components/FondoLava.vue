<template>
  <div class="fondo-animado">
    <div class="wave"></div>
    <div class="wave"></div>
    <div class="wave"></div>
  </div>
</template>

<script>
export default {
  name: 'FondoLava'
}
</script>

<style scoped>
/* Fondo animado con olas monocromáticas */
.fondo-animado {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: -1;
  overflow: hidden;
  border-radius: 10px; /* Borde redondeado */
}

/* Estilo de las olas */
.wave {
  background: linear-gradient(45deg, rgba(0, 66, 112, 0.6), rgba(42, 0, 84, 0.6)); /* Colores azul y morado */
  border-radius: 1000% 1000% 0 0;
  position: absolute;
  width: 200%; /* Olas más grandes */
  height: 30em; /* Altura de las olas */
  animation: wave 10s -3s linear infinite; /* Movimiento de las olas */
  transform: translate3d(0, 0, 0);
  opacity: 0.8; /* Opacidad */
  bottom: 0;
}

/* Segunda ola con un movimiento distinto */
.wave:nth-of-type(2) {
  bottom: -1em;
  animation: wave 10s linear reverse infinite; /* Movimiento inverso */
}

/* Tercera ola */
.wave:nth-of-type(3) {
  bottom: -4em;
  animation: wave 20s -1s reverse infinite; /* Movimiento inverso */
  opacity: 0.6; /* Opacidad diferente */
}

/* Animación del movimiento de las olas */
@keyframes wave {
  0% {
    transform: translateX(0);
  }
  50% {
    transform: translateX(-50%);
  }
  100% {
    transform: translateX(0);
  }
}
</style>
