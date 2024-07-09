name = input("Enter your name to continue: ")
password = input("Input password to login: ")

number_of_character = len(password)


#if(len(password) > 0):
	#print("* " * number_of_character)


#print("*" * number_of_character)



#for asterisks in range(number_of_character):
#	print("* " , end="")


count = number_of_character
while(count > 0):
	print("* ", end="" )
	count-=1