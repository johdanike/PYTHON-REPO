#prompt for data in type string - any word
#Check for number of vowels and consonants in the word



print("Enter any word and get the number of vowels and consonants in it")

name = input("Enter your name to begin: ")

flag = ""
counter_vowels = ""
counter_consonants = ""
vowel_list = 'aeiou'
vowel_list = list(vowel_list)


while(flag != ("no")):

	word = input("Enter word: ")
	for char in  word:
		if char in vowel_list:
			counter_vowels +=char  
		else:
			counter_consonants += char

	counter_vowels = set(counter_vowels)
	counter_consonants = set(counter_consonants)

	print(f"\n\n{name}, The number of consonants in {word} is = {len(counter_consonants)}\nThe number of vowels in {word} is = {len(counter_vowels)}" )


	flag = input("Do yo want to comtinue? Yes or no?: \n ")
	counter_vowels = ""
	counter_consonants = ""


		