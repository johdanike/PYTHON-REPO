"""PROGRAM THAT ACCEPTS A SENTENCE AND CALCULATES THE NUMBER OF LETTERS AND DIGITS"""
"""PSEUDOCODE"""
#Prompt user to input sentence and store in user_input
#Using a for loop, walk through the length of user_input, check for characters and digits 
#Output result

"""Execution"""
digits = []
letters = []
sentence = []
dig_letters = 0
dig_number = 0

alphabets = ["a","A",'b','B', 'c','C', 'd','D','e',"E", 'f','F','g', 'G', 'h','H','i','I','j','J','k','K','l','L','m','M','n','N','o','O','p','P','q','Q','r','R','s','S','t','T','w','W','x','X','y','Y','z', 'Z']

numbers = ['1','2','3','4','5','6','7','8','9','0']


user_input = input("Enter sentence: ")
sentence += user_input

for char in sentence:
	for index in numbers:
		if char == index:
			digits += [index]
			dig_number += 1
	for character in alphabets:
		if char == character:
			letters += [character]
			dig_letters += 1

print(f"LETTERS: {letters}   DIGITS: {digits}")
print(f"LETTERS: {dig_letters}   DIGITS: {dig_number}")

#print(sentence)
		
	