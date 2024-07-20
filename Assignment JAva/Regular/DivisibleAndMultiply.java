public class DivisibleAndMultiply{
	public static void main(String...args){
		int counter = 0;
		for(int numbers = 4200; numbers >= 770; numbers--){
			if(numbers % 7 == 0 && numbers % 5 != 0)System.out.print(numbers+",");
			counter++;
		}
			System.out.print("\nThe total number is "+counter);

	}
}