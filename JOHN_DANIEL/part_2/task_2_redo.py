user_input = input("Enter sentence: ")
letter = 0
digit = 0
char = 0
for character in user_input:
	if character >='a' and character<="z":
		letter += 1
	if character >= '0' and character <= '9':
		digit += 1
print(f'Digits: {digit}  Letter: {letter}  Characters: {char}')