class Producto {
    static contadorProductos = 0;
    constructor(nombre, precio) {
        this._idProducto = ++Producto.contadorProductos; // Inicializamos _idProducto solo una vez
        this._nombre = nombre;
        this._precio = precio;
    }

    // Getter para acceder a _idProducto
    get idProducto() {
        return this._idProducto;
    }

    get nombre() {
        return this._nombre;
    }

    set nombre(nombre) {
        this._nombre = nombre;
    }

    get precio() {
        return this._precio;
    }

    set precio(precio) {
        this._precio = precio;
    }

    toString() {
        return `idProducto: ${this._idProducto}, nombre: ${this._nombre}, precio: $${this._precio}`;
    }
} // Fin de la clase Producto

class Orden {
    static contadorOrdenes = 0;
    static getMAX_PRODUCTOS() { //Simula una constante
        return 5;
    }

    constructor() {
        this._idOrden = ++Orden.contadorOrdenes;
        this._productos = [];
        this._contadorProductosAgregados = 0;
    }

    // Cambiamos el nombre del getter para evitar conflictos
    get idOrden() {
        return this._idOrden;
    }

    agregarProducto(producto) {
        if (this._productos.length < Orden.getMAX_PRODUCTOS()) {
            this._productos.push(producto); // Agregar el producto al array
        } else {
            console.log("No se pueden agregar más productos");
        }
    }

    calcularTotal() {
        let totalVenta = 0;
        for (let producto of this._productos) {
            totalVenta += producto.precio;
        }
        return totalVenta;
    }

    mostrarOrden() {
        let productosOrden = "";
        for (let producto of this._productos) {
            productosOrden += '\n{'+ producto.toString()+'}';
        }
        console.log(`Orden: ${this.idOrden}, Total: $${this.calcularTotal()}, Productos: ${productosOrden}`);
    }
} // Fin de la clase Orden

// Ejemplo de uso
let producto1 = new Producto("Pantalon", 200);
let producto2 = new Producto("Camisa", 150);
let producto3 = new Producto("Cinturon", 50);
let orden1 = new Orden();
let orden2 = new Orden();
orden1.agregarProducto(producto1);
orden1.agregarProducto(producto2);
orden1.agregarProducto(producto3);
orden1.agregarProducto(producto1);
orden1.agregarProducto(producto2);
orden2.agregarProducto(producto3);
orden1.mostrarOrden();
orden2.mostrarOrden();

