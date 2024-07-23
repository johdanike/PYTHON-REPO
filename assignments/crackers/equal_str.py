def equal_str(stringA, stringB):

	for letter1 in stringA:
		for letter2 in stringB:
			if len(set(stringA)) == len(set(stringB)):
				return "True"
			else:
				return "False"

print(equal_str("ant", "golk"))
	