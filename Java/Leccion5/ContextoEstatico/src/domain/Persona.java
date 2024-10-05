package domain;

public class Persona {
    //cargamos los atributos
    private int idPersona;
    private static int contadorPersona;
    private String nombre;

    public int getIdPersona() {
        return this.idPersona;
    }

    public void setIdPersona(int idPersona) {
        this.idPersona = idPersona;
    }

    public static int getContadorPersona() {
        return contadorPersona;
    }

    public static void setContadorPersona(int contadorPersona) {
        Persona.contadorPersona = contadorPersona;
    }

    public String getNombre() {
        return this.nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    //Constructor
    public Persona(String nombre){
        this.nombre = nombre;
        // incrementar el contador por cada objeto nuevo
        Persona.contadorPersona++; // no usar operador this
        this.idPersona = Persona.contadorPersona;

    }

    @Override
    public String toString() {
        return "Persona{" +
                "idPersona=" + idPersona +
                ", nombre='" + nombre + '\'' +
                '}';
    }
}
