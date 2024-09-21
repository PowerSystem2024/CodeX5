let x = 10; //Variable de tipo primitiva
console.log(x.length);
console.log("Tipos primitivos");
//Objeto
let persona = {
    nombre: "Carlos",
    apellido: "Gil",
    email: "cgil@gmail.com",
    edad: 28,
    idioma: "es",
    get lang(){
        return this.idioma.toUpperCase(); // Convierte las minusculas a mayusculas
    },
    set lang(lang){
        this.idioma = lang.toUpperCase();
    },
    nombreCompleto: function(){ //Metodo o funcion en JavaScript
        return this.nombre+' '+this.apellido;
    },
    get nombreEdad(){ // Este es el metodo get
        return "El nombre es: "+this.nombre+", Edad: "+ this.edad
    }
}

console.log(persona.nombre);
console.log(persona.apellido);
console.log(persona.email,);
console.log(persona.edad);
console.log(persona)
console.log(persona.nombreCompleto());
console.log("Ejecutando con un objeto");
let persona2 = new Object(); //Debe crear un nuevo objeto en memoria
persona2.nombre = "Juan";
persona2.direccion = "Salada 14";
persona2.telefono = "542604651804";
console.log(persona2.telefono);
console.log("Creamos un nuevo objeto");
console.log(persona["apellido"]); //Accedemos como si fuera un arreglo
console.log("Usamos el ciclo for in");

//for in y accedemos al objeto como si fuera un arreglo
for(propiedad in persona){
    console.log(propiedad);
    console.log(persona[propiedad]);
}
persona.apellida = "Betancud"//Cambiamos dinamicamente un valor del objeto
delete persona.apellida; // Eliminamos el  error
console.log(persona);

//Distintas formas de imprimir un objeto
//Numero 1: Las mas sensillas: concatenar cada valor de cada propiedad
console.log("Distintas formas de imprimir un objeto: 1");
console.log(persona.nombre+","+persona.apellido);

//Numero 2: Atraves del ciclo for in
console.log("Distintas formas de imprimir un objeto: 2");
for(nombrePropiedad in persona){
    console.log(persona[nombrePropiedad]);
}

//Numero 3: La funcion objet values()
console.log("Distintas formas de imprimir un objeto: 3");
let personaArray = Object.values(persona);
console.log(personaArray);

//Numero 4: Utilizaremos el metodo JSON.stringify
console.log("Distintas formas de imprimir un objeto: 4");
let personaString = JSON.stringify(persona);
console.log(personaString);

console.log("Comenzamos a utilizar el metodo get");
console.log(persona.nombreEdad);

console.log("Comenzamos con el método get y set para idiomas");
persona.lang = "en";
console.log(persona.lang);

function Persona3(nombre,apellido,email){ // Constructor
    this.nombre = nombre;
    this.apellido = apellido;
    this.email = email;
    this.nombreCompleto = function(){
        return this.nombre+" "+this.apellido;
    }
}
let padre = new Persona3("Leo","Lopez","lopezl@gmail.com");
padre.nombre = "Luis"; // Modificamos el nombre
padre.telefono = "29426558767"; // Una propiedad exclusiva del objeto padre
console.log(padre);
console.log(padre.nombreCompleto()) // Utilizamos la funcion
let madre = new Persona3("Laura", "Contrera", "contreral@gmail.com")
console.log(madre);
console.log(madre.telefono); //La propiedad no esta definida
console.log(madre.nombreCompleto())


// Diferentes formas de crear objetos
// Caso numero 1
let miObjeto = new Object(); // Esta es una opcion formal
// Caso numero 2
let miObjeto2 = {} // Esta opcion es breve y recomendada

// Caso String 1
let miCadena1 = new String("Hola"); // Sintaxis Formal
// Caso String 2
let miCadena2 = "Hola"; // Esta es la sintaxis simplificada y recomendada

// Caso con numeros 1
let miNumero = new Number(1); // Es formal no recomendable
// Caso con numeros 2 
let miNumero2 = 1; // Sintaxis Recomendada

// Caso boolean 1
let miBoolean1 = new Boolean(false); // Formal
// Caso boolean 2
let miBoolean2 = false; // Sintaxis recomendada

// Caso Arreglos 1
let miArreglo1 = new Array(); // Formal
// Caso Arreglos 2
let miArreglo2 = [] // Sintaxis recomendada

// Caso function 1
let miFunction1 = new function(){} // Todo despues de new es considero objeto
// Caso function 2
let miFunction2 = function(){}; // Notacion simplificada y recomendada

// Uso de prototype
Persona3.prototype.telefono = "2942438734";
console.log(padre);
console.log(madre.telefono)
madre.telefono = "32464534125"
console.log(madre.telefono)

//Uso de call
let Persona4 = {
    nombre: "Juan",
    apellido: "Perez",
    nombreCompleto2: function(titulo,telefono){
        return titulo+": "+this.nombre+" "+this.apellido+ " "+telefono; 
        //return this.nombre+ " "+this.apellido;
    }
}

let Persona5 = {
    nombre: " Carlos",
    apellido:"Lara"
}

console.log(Persona4.nombreCompleto2("Lic","345657546"))
console.log(Persona4.nombreCompleto2.call(Persona5,"Ing","564575456"));

// Metodo Apply
let arreglo = ["Ing.","4536544356"];
console.log(Persona4.nombreCompleto2.apply(Persona5,arreglo));
