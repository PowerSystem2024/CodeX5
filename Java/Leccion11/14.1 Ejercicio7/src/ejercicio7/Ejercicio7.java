
package ejercicio7;

import java.util.Scanner;



/*
Ejercicio 15: Leer 10 enteros ordenados crecientemente.Leer N y buscarlo en la
tabla. Se debe mostrar la posición en que se encuentra. Si no está, indicarlo
con un mensaje.
*/
public class Ejercicio7 {
    public static void main(String[] args){
    Scanner entrada = new Scanner(System.in);       
    int arreglo [] = new int [10];
    boolean creciente = true;
    int numero, numero2=0;
    
    System.out.println("Llenar el arreglo: ");
    do {
            for (int i=0;i<10;i++) {
                System.out.print (i+". Digite un numero: ");
                arreglo [i] = entrada.nextInt();
            }
            
            for (int i=0;i<9;i++) {
                if (arreglo [i] < arreglo[i+1]) {
                       creciente = true;
                }
                if (arreglo [i] > arreglo [i+1]) {
                    creciente = false;
                    break;
            }
            
    }
            if (creciente == false) {
                System.out.println("\nEl arreglo esta desordenado,vuelve a digitar");
            }
    
        } while (creciente == false);
            System.out.print("\nDigite un numero para buscar en el arreglo: ");
   
            numero = entrada.nextInt();
            
            int i=0;
            while (i<10 && arreglo [i]<numero) {
                i++;
            }
            if (i==10) {
                System.out.println("\nNumero no encontrado");
            }
            else{
                if (arreglo [i] == numero) {
                    System.out.println("\nNumero encontrado en la posicion: "+i);                }
                else{
                    System.out.println("Numero no encontrado");
                }
                System.out.println();
            }
    }
    
}


            

