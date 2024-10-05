package test;
import dominio.Persona;
public class PersonaPrueba {
    public static void main(String[] args) {
        Persona persona1 = new Persona(" Osvaldo", 57.000, false);
        // Modificar a traves de los metodos
        persona1.setNombre(" Juan Ignacio");
        //persona1.nombre=" Juan Ignacio";//Ya no se puede utilizar
        System.out.println("persona1 con su nombre modificado: " + persona1.getNombre());
        System.out.println("persona1 el resultado para el sueldo: " + persona1.getSueldo());
        System.out.println("persona1 para obtener el booleano: " + persona1.isEliminado());
        //Tarea: crear otro objeto de tipo Persona, asignar valores de manera inicial
        // y imprimier luego modificar sus valores y volver a imprimir
        Persona persona2 = new Persona( "Karen", 90.000, true);
        System.out.println("persona2 con su nombre modificado: " + persona2.getNombre());
        System.out.println("persona2 el resultado para el sueldo: " + persona2.getSueldo());
        System.out.println("persona2 para obtener el booleano: " + persona2.isEliminado());
        persona2.setSueldo(15.000);
        persona2.setEliminado(false);
        System.out.println("persona2 con su nombre modificado: " + persona2.getNombre());
        System.out.println("persona2 el resultado para el sueldo: " + persona2.getSueldo());
        System.out.println("persona2 para obtener el booleano: " + persona2.isEliminado());
        System.out.println("persona1: "+ persona1.toString());
    }
}
