print("Enter any word and get the number of vowels and consonants in it")

word = input("Enter your word to begin: ")

count_consonant = ""
count_vowel = ""
for word_count in word:
	if word_count.lower() in ['a', 'e', 'i', 'o', 'u']:
		count_vowel += word_count
	else:
		count_consonant += word_count


print(f"The number of vowels in {word} is = {len(set(count_vowel))} " )
print(f"The number of consonants in {word} is = {len(set(count_consonant))} " )

			
		
		
		