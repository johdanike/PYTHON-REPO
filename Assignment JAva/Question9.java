import java.util.Scanner;

public class Question9{
	public static void main(String...args){
	Scanner input = new Scanner(System.in);

	int num1 = 0;
	int num2 = 0;
	int num3 = 0;
	int num4 = 0;
	int num5 = 0;
	
	System.out.print("Enter the five digit integer: ");
	int number = input.nextInt();

		for(int loops = 1; loops <= 5; loops++){

			if(loops == 5)num5 = number / 1 % 10;
			if(loops == 4)num4 = number / 10 % 10;
			if(loops == 3)num3 = number / 100 % 10;
			if(loops == 2)num2 = number / 1000 % 10;
			if(loops == 1)num1= number / 10000 % 10;

		}
		
			System.out.print(num1,"",num2,"",num3,"",num4,"",num5);
	}
}