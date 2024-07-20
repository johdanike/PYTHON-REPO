import java.util.Scanner;

public class CarTax{
	public static void main(String...args){
	Scanner input = new Scanner(System.in);
		
		System.out.print("This program calculates the tax on cars");

		//int flag = -1;
		double tax = 0;

		//while(flag != -1){
			System.out.print("How much is the car worth? : ");	
			double carPrice = input.nextInt();

			if(carPrice < 1_000_000){
				 tax = carPrice * (10 / 100);
			}

			if(carPrice > 1_000_000 && carPrice < 3_000_000){
				 tax = carPrice * (15/ 100);
			}

			if(carPrice > 3_000_000 && carPrice < 5_000_000){
				 tax = carPrice * (20 / 100);
			}

			if(carPrice > 5_000_000){
				 tax = carPrice * (25 / 100);
			}


			System.out.print("Your tax on your car that cost "+tax);
			
			//System.out.print("Press 1 to continue or -1 to exit: ");	
			//flag = input.nextInt();


		//}
	
		
	}
}