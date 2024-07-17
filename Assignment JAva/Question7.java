import java.util.Scanner;

public class Question7{
	public static void main(String...args){
	Scanner input = new Scanner(System.in);


   	System.out.printf("%8s%8s%8s%n", "Number", "Square", "Cube");

      		for (int num = 0; num <=6; num++){
        		int square = num * num;
        		int cube = num * num * num;

			

       			System.out.printf("%8d%8d%8d%n", num, square, cube);  
		}
	}
}

