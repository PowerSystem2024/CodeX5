
package test;

import dominio.Persona;

public class PersonaPrueba {
    public static void main(String[] args) {
        Persona persona1 = new Persona("Osvaldo", 57.000, false);
        System.out.println("persona1 = " + persona1);
        System.out.println("persona1 su nombre es: "+persona1.getNombre());
        //Modificar a traves de los metodos
        persona1.setNombre("Juan Ignacion");
        //persona1.nombre = "Juan Ignacio"; //Ya no se puede utitlizar
        //System.out.println("Nombre es: "+persona1.nombre);//Error
        System.out.println("persona1 con su nombre modificado es: "+persona1.getNombre());
        System.out.println("Su  sueldo es: "+persona1.getSueldo());
        System.out.println("persona1 para obtener el booleano: "+persona1.isEliminado());
        
        
        //Tarea: Crear otro objeto de tipo persona asignar valores de manera inicial
        //e imprimir, luego modificar sus valores e imprimir
        Persona persona2 = new Persona("Emilia", 1000000.00, false);
        System.out.println("PERSONA2: VALORES INICIALES");
        System.out.println("persona2 nombre: "+persona2.getNombre());
        System.out.println("persona2 sueldo: "+persona2.getSueldo());
        System.out.println("persona2 booleano: "+persona2.isEliminado());
        
        System.out.println("PERSONA2: VALORES MODIFICADOS");
        persona2.setNombre("Bautista");
        persona2.setSueldo(3000000.00);
        persona2.setEliminado(true);
        System.out.println("persona2 nombre: "+persona2.getNombre());
        System.out.println("persona2 sueldo: "+persona2.getSueldo());
        System.out.println("persona2 booleano: "+persona2.isEliminado());
        
        
        System.out.println("persona1 = " + persona1);
        
    }
}
