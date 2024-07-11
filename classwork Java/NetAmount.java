import java.util.Scanner;

public class NetAmount{
	public static void main(String...args){
	Scanner input = new Scanner(System.in);

		System.out.println("PROGRAM THAT COMPUTES THE NET AMOUNT OF A BANK ACCOUNT BASED ON TRANSACTION LOG");


		String options = """

			OPTIONS\n
			1: Deposit
			2: Withdraw
			3: Get Balance

					""";

		
		int deposit = 0;
		int balance = 0;
		int condition = 1;
		int entry = 0;

		while(condition == 1){

			System.out.println(options);

			System.out.println("SELECT ONE OPTION TRO PROCEED");
			entry = input.nextInt();

			
			switch(entry){
				case 1: 
					System.out.print("Amount to be deposited: ");
					int amount = input.nextInt();
					balance += amount;
					System.out.println("You have deposited "+amount+ "and your balance is "+balance);
					break;
				case 2: 
					System.out.print("Amount to withdraw: ");
					int withdraw = input.nextInt();
					balance = balance - withdraw;

					if(balance == 0)System.out.println("Insufficient balance");
					if(withdraw > balance)System.out.println("Insufficient balance");
					if(withdraw < 0)System.out.println("Insufficient balance");
					System.out.println("You have withdrawn "+withdraw);
					break;
				case 3:
					int current_balance = balance;
					System.out.printf("Current balance = %d", current_balance);
					break;
				default:
					System.out.println("INVALID SELECTION");

			}

			System.out.println("\nDo you wish to continue? Press 1 or -1 to terminate: \n");
			condition = input.nextInt();

		}


	}

}