
package ar.com.codesystem.ventas.test;

import ar.com.codesystem.ventas.*;

public class VentasTest {
    public static void main(String[] args) {
        Producto producto1 = new Producto ("Pantalon", 9500.00);
        Producto producto2 = new Producto ("Campera", 29900.00);
        Producto producto3 = new Producto("Camisa", 7800.00);
        Producto producto4 = new Producto("Remera", 3500.00);
        Producto producto5 = new Producto("Zapatos", 12500.00);
        Producto producto6 = new Producto("Gorro", 1500.00);
        Producto producto7 = new Producto("Guantes", 1200.00);
        Producto producto8 = new Producto("Bufanda", 1800.00);
        Producto producto9 = new Producto("Jeans", 8900.00);
        Producto producto10 = new Producto("Cinturon", 2200.00);
        Producto producto11 = new Producto("Saco", 14500.00);
        Producto producto12 = new Producto("Chaleco", 10500.00);
        
        Orden orden1 = new Orden ();
        //Agregamos productos al arreglo 
        orden1.agregarProducto (producto1);
        orden1.agregarProducto (producto2);
        orden1.agregarProducto(producto3);
        orden1.agregarProducto(producto4);
        orden1.agregarProducto(producto5);
        orden1.agregarProducto(producto6);
        orden1.agregarProducto(producto7);
        orden1.agregarProducto(producto8);
        orden1.agregarProducto(producto9);
        orden1.agregarProducto(producto10);
        orden1.agregarProducto(producto11);
        orden1.agregarProducto(producto12);
        orden1.mostrarOrden ();
        
        //Tarea:
        //Crear mas objetos de tipo Producto (minimo 10) (TAREA HECHA)
        //Crear mas objetos de tipo Orden (minimo 2)
        
        // Crear más objetos de tipo Orden y agregar productos
        Orden orden2 = new Orden();
        orden2.agregarProducto(producto1);
        orden2.agregarProducto(producto4);
        orden2.agregarProducto(producto7);
        orden2.agregarProducto(producto9);
        orden2.agregarProducto(producto10);
        orden2.mostrarOrden();

        Orden orden3 = new Orden();
        orden3.agregarProducto(producto2);
        orden3.agregarProducto(producto3);
        orden3.agregarProducto(producto5);
        orden3.agregarProducto(producto8);
        orden3.agregarProducto(producto11);
        orden3.mostrarOrden();
    }
}
