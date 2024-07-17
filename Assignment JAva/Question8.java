import java.util.Scanner;

public class Question8{
	public static void main(String...args){
	Scanner input = new Scanner(System.in);

	int sum = 0;
	int product = 0;
	int average = 0;
	int largestNum = 0;
	int smallestNum = 0;
	int num1 = 0; 
	int num2 = 0;
	int num3 = 0;
	int num4 = 0;


	System.out.print("Arithmetic, Smallest and Largest");

		for(int integers = 1; integers <= 4; integers++){
			System.out.printf("\nEnter (%d) number: ", integers);
			int number = input.nextInt();

			if(integers == 1)num1 = number;
			if(integers == 2)num2 = number;
			if(integers == 3)num3 = number;
			if(integers == 4)num4 = number;
		
			if(num1 > num2 && num1 > num3 && num1 > num4)largestNum = num1;
			else if(num1 < num2 && num1 < num3 && num1 < num4)smallestNum = num1;

			if(num2 > num1 && num2 > num3 && num2 > num4)largestNum = num2;
			else if(num2 < num1 && num2 < num3 && num2 < num4)smallestNum = num2;

			if(num3 > num1 && num3 > num2 && num3 > num4)largestNum = num3;
			else if(num3 < num1 && num3 < num2 && num3 < num4)smallestNum = num3;

			if(num4 > num1 && num4 > num2 && num4 > num3)largestNum = num4;
			else if(num4 < num1 && num4 < num2 && num4 < num3)smallestNum = num4;

			
			sum += number;
			average = sum / 4;
			product = num1 * num2 * num3 * num4;

		}
	
		System.out.printf("%nThe sum of the four integers is: %d",sum);
		System.out.printf("%nThe product of the four integers is: %d",product);
		System.out.printf("%nThe average of the four integers is: %d",average);
		System.out.printf("%nThe largest of the four integers is: %d",largestNum);
		System.out.printf("%nThe smallest of the four integers is: %d",smallestNum);
		

		
		
	}
}









