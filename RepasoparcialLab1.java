import java.util.Scanner;
public class EjerciciosTP5 {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        double number, numbertwo,lastdigitone,lastdigittwo;
        System.out.println("Ingrese el numero");
        number=sc.nextInt();
        System.out.println("Ingrese el segundo numero");
        numbertwo=sc.nextInt();
        lastdigitone=number%10;
        lastdigittwo=numbertwo%10;
        if(lastdigitone==lastdigittwo){
            System.out.println("La dos ultimas cifras de los numeros ingresados son iguales");
        }
    }
}
import java.util.Scanner;
public class EjerciciosTP5 {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int number, digit1, digit2, iterable;
        iterable = 0;
        while (iterable == 0) {
            System.out.println("Ingrese un numero");
            number = sc.nextInt();
            if (number > 99 && number < 1000) {
                digit1 = number / 100;
                digit2 = number % 10;
                if (digit1 == digit2) {
                    System.out.println("Es capicua");
                } else {
                    System.out.println("No es capicua");
                }
                iterable = 1;
            } else System.out.println("El numero ingresado no es de 3 cifras");
        }
    }
}
