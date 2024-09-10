for asterisks in range(1,11):
	print(f"{asterisks * '*'} {'*' * (10 - asterisks)} {'*' * (10 - asterisks) + ''} {(10 - asterisks) * '*'}")