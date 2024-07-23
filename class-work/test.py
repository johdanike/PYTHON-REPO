def greet(name):
	print(f"hi {name} ")


#greet("Daniel", "Hamedani")


def get_greeting(name):
	return f"hi {name}"

message = get_greeting('Daniel')
file = open('content.txt', 'w')
filr.write(message)

