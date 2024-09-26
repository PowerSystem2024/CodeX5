/*
Ejercicio 12: Pedir un numero y calcular su factorial
Hacerlo con las dos clases Scanner y JOptionPane
 */
package ciclos12;

import javax.swing.*;
import java.util.Scanner;

public class Ciclos12 {
    public static void main(String[] args) {
        //Scanner entrada = new Scanner(System.in);
        long factorial = 1;
        //System.out.println("Digite un numero: ");
        int numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        for(int i=1 ; i<=numero ; i++){
            factorial *= i;
        }
        System.out.println("\n El factorial del numero ingresado es: "+factorial);
        JOptionPane.showMessageDialog(null,"\n El factorial del numero ingresado es: "+factorial);

    }

}