package caja;


public class PruebaCaja {
    public static void main(String[] args) { //Método main
        //Variables locales
        int medidaAncho = 3; //Valores ingresados en código duro
        int medidaAlto = 2;
        int medidaProf = 6;
        Caja cajal = new Caja(); //Instanciamos el objeto, constructor vacio
        cajal. ancho = medidaAncho; //Le pasamos los valores al objeto
        cajal.alto = medidaAlto;
        cajal.profundo = medidaProf;
        int resultado = cajal.calcularVolumen(); //Llamamos al método
        //Primer resultado
        System.out.println("resultado volumen de caja 1:" + resultado);

        Caja caja2 = new Caja(2, 4, 6); //Llamamos al constructor 2 con nuevos argumento
        //Llamamos con el nuevo objeto al método para un nuevo calculo
        System.out.println("resultado volumen de caja 2:" + caja2.calcularVolumen());

    }
}
