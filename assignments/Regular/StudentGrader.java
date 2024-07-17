import java.util.Scanner;

public class StudentGrader{
	public static void main(String...args){

	Scanner input = new Scanner(System.in);

	System.out.println("School Score Grade");

		int pass = 0;
		int fail = 0;
		final int passMark = 45;
	
		for(int loop = 1; loop < 16; loop++){

			System.out.printf("Enter (%d) score: ", loop);
			int score = input.nextInt();

			if(score < passMark)fail++;
			if(score > passMark)pass++;

		}

			System.out.println("The total that passed = "+pass);
			System.out.println("The total that failed = "+fail);

	}
}