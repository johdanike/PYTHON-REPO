import java.util.Scanner;

public class ValidatingUserinput{
	public static void main(String...args){
	Scanner input = new Scanner(System.in);

		passes = 0 ;
		failures = 0 ;

		student in range(10):
		result = int(input('Enter result (1=pass, 2=fail): '))

		if result == 1:
			passes = passes + 1
		else:
			failures = failures + 1

		print('Passed:', passes)
		print('Failed:', failures)

		if passes > 8:
			print('Bonus to instructor')


	}
}

