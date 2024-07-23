import java.util.Scanner;

public class PersonalIncomeTax{
	public static void main(String...args){
	Scanner input = new Scanner(System.in);

		String choice = """	0: Single filer;
					1: Married filing jointly;
					2: Married filing separately;
					3: Head of household;
								""";


		System.out.print("Enter filing stasus:");
		int option = input.nextInt();

		System.out.print("Enter taxable income:");
		int taxableIncome = input.nextInt();


		int tax = 0;
		int taxRate10 = 10 / 100;
		int taxRate15 = 15 / 100;
		int taxRate25 = 25 / 100;
		int taxRate28 = 28 / 100;
		int taxRate33 = 33 / 100;
		int taxRate35 = 35 / 100;


		
		switch(choice){
			case "0":
				if(taxableIncome >= 0 && taxableIncome <= 8350)tax = taxableIncome * taxRate10;
				else if(taxableIncome >= 8351 && taxableIncome <= 33950)tax = taxableIncome * taxRate15;
				else if(taxableIncome >= 33951 && taxableIncome <= 82250)tax = taxableIncome * taxRate25;
				else if(taxableIncome >= 82251 && taxableIncome <= 171550)tax = taxableIncome * taxRate28;
				else if(taxableIncome >= 171551 && taxableIncome <= 372950)tax = taxableIncome * taxRate33;
				else if(taxableIncome >= 372951)tax = taxableIncome * taxRate35;

	
			case "1":
				if(taxableIncome >= 0 && taxableIncome <= 16700)tax = taxableIncome * taxRate10;
				else if(taxableIncome >= 16701 && taxableIncome <= 67900)tax = taxableIncome * taxRate15;
				else if(taxableIncome >= 67901 && taxableIncome <= 137050)tax = taxableIncome * taxRate25;
				else if(taxableIncome >= 137051 && taxableIncome <= 208850)tax = taxableIncome * taxRate28;
				else if(taxableIncome >= 208851 && taxableIncome <= 372950)tax = taxableIncome * taxRate33;
				else if(taxableIncome >= 372951)tax = taxableIncome * taxRate35;


			case "2":
				if(taxableIncome >= 0 && taxable_income <= 8350)tax = taxableIncome * taxRate10;
				else if(taxableIncome >= 8351 && taxable_income <= 33950)tax = taxableIncome * taxRate15;
				else if(taxableIncome >= 33951 && taxable_income <= 68525)tax = taxableIncome * taxRate25;
				else if(taxableIncome >= 68526 && taxableIncome <= 104425)tax = taxableIncome * taxRate28;
				else if(taxableIncome >= 104426 && taxableIncome <= 186375)tax = taxableIncome * taxRate33;
				else if(taxableIncome >= 186476)&& = taxableIncome * taxRate35;

			case "3":
				if(taxableIncome >= 0 && taxableIncome <= 11950)tax = taxableIncome * taxRate10;
				else if(taxableIncome >= 11951 && taxableIncome <= 45500)tax = taxableIncome * taxRate15;
				else if(taxableIncome >= 45501 && taxableIncome <= 117450)tax = taxableIncome * taxRate25;
				else if(taxableIncome >= 117451 && taxableIncome <= 190200)tax = taxableIncome * taxRate28;
				else if(taxableIncome >= 190201 && taxableIncome <= 372950)tax = taxableIncome * taxRate33;
				else if(taxableIncome >= 372951)tax = taxable_income * taxRate35;


			
		}

			System.out.printf("The tax for %d", tax);
		
	}
}