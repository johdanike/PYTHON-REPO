def equal_strings(string1, string2):
	if len(string1) == len(string2) and set(string1) == set(string2):
		return "True"
	else:
		return "False"


print(equal_strings("love", "evol"))