import java.util.Scanner;

public class Question7{
	public static void main(String...args){
	Scanner input = new Scanner(System.in);

	System.out.print("What is your problem? \n");
	String problem = input.nextInt();

	System.out.print("\nHave you had this problem before? Yes or No: ");
	String diagnosis = input.nextInt();

	if(diagnosis == "yes") System.out.print("\nWell, you have it again");	
	if(diagnosis == "no") System.out.print("\nWell, you have it now");

	System.out.print("\n\nI think this conversation will convince the user of the intelligence of the computer because of the rationality behind the jugdement. The computer is able to run some comparison and pass judgement rationally");	

	}

}

