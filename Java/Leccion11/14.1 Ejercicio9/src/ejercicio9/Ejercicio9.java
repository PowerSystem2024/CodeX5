
package ejercicio9;

/*
Ejercicio 7: Crear una matriz "marco" de tamaño 5x5: todos sus elementos
deben ser o salvo los de los bordes que deben ser 1. Mostrarla.
*/

public class Ejercicio9 {
    public static void main(String[] args) {
        int matriz [][] = new int [5][5];
        
        System.out.println("Rellenando la matriz: ");
        for (int i=0;i<5;i++) {
            for (int j=0;j<5;j++) {
                if (i==0 || i==4) {
                    matriz [i][j] = 1;
                }
                else if(j==0 || j==4) {
                    matriz [i][j] = 1;
                }
                else{
                    matriz [i][j] = 0;//No hace falta porque siempre empiezan en 0
                } 
            }
        }
        System.out.println("La matriz es: ");
        for (int i=0;i<5;i++) {
            for (int j=0;j<5;j++) {
                System.out.print(matriz[i][j]+" ");
            }
            System.out.println("") ;
        }
        System.out.println("") ;
    }   
        

}
