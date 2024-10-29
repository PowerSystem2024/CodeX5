
package test;

/**
 *
 * @author anaca
 */
public class TestArreglos {
    public static void main(String[] args) { //lado derechointanciamos un objeto de tipo objet
        int edades[] = new int [3]; //El lado izq declaramos la variable
        System.out.println("edades = " + edades);   
        
        edades [0] = 17;
        System.out.println("edades 0 = " + edades [0]);
        
        edades [1] = 22;
        System.out.println("edades 1 = " + edades [1]);
        
        edades [2] = 18;
        System.out.println("edades 0 = " + edades [2]);
        
        edades [3] = 7; //Fuera de rango, error en un tiempo de ejecucuion
        
        for(int i = 0; i < edades.length; i++){
            System.out.println("edades y sus elementos "+i+": "+edades[i]);
        }
        
    }
}
