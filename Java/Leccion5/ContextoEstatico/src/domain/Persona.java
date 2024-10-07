
package domain;

public class Persona {

    //Cargamos atributos
    private int idPersona;
    private static int contadorPersona;
    private String nombre;
    
    //CONSTRUCTOR
    public Persona(String nombre){
        this.nombre = nombre;
        //Incrementar el contador por cada objeto nuevo
        Persona.contadorPersona++; //No utilizar el operador this
        //Vamos asignar un nuevo valor a la variable idPersona
        this.idPersona = Persona.contadorPersona;
        
    }
    //Getter and Setter
    public static int getContadorPersona() {
        return contadorPersona;
    }

    public static void setContadorPersona(int aContadorPersona) {
        contadorPersona = aContadorPersona;
    }
    
    public int getIdPersona() {
        return this.idPersona;
    }

    public void setIdPersona(int idPersona) {
        this.idPersona = idPersona;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    @Override
    public String toString() {
        return "Persona{" + "idPersona=" + idPersona + ", nombre=" + nombre + '}';
    }
    
    
}
