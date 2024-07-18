import java.util.Random;
import java.util.Scanner;

public class GuessTheNumber{
	public static void main(String...args){
	Scanner input = new Scanner(System.in);

		Random rand = new Random();
		int computer = rand.nextInt(1, 10);

		System.out.println("Let's play a game. \nGuess any number between 1 to 1000 with the fewest guesses");
		

		String flag = "";

	while(!flag.equalsIgnoreCase("no")){

		int userInput = 0;
		int counter = 0;

		while(userInput != computer){
			System.out.println("Enter your guess: ");
			userInput = input.nextInt();
			
			if(userInput < computer)System.out.println("Too low! Try Again");
			else if(userInput > computer)System.out.println("Too High! Try Again");

			if(userInput == computer && counter <= 10){
				System.out.println("Congratulations. You Guessed The Number");
				System.out.printf("\nYou got it at %d attempts. You Rock!!!!", counter);
			}
			else if(userInput == computer && counter > 10)System.out.printf("You got it at %d attempts. It took too long to get it!", counter);
			counter++;
		}

	System.out.print("\nPress yes to continue or no to exit: ");
	flag = input.next();
	}


	}
}