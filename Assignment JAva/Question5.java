import java.util.Scanner;

public class Question2{
	public static void main(String...args){
	Scanner input = new Scanner(System.in);
		
		System.out.print("Enter first integers, and I will tell you the relationships they satisfy");
		int numberOne = input.nextInt();

		System.out.print("Enter second integer, and I will tell you the relationships they satisfy");
		int numberTwo = input.nextInt();

		if(numberOne <= numberTwo)System.out.print("Number1, 'is less than or equal to', Number2");
		else if(numberOne >= numberTwo)System.out.print("Number1, 'is greater than or equal to', Number2");
		else System.out.print("Number1, 'is not equal to', Number2");

		
		
		
		
	}


}


