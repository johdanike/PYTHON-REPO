

def sorted_by_john(*parameters):
    for index in range(len(parameters)):
        for compare in range(len(parameters)):
            if parameters[index] > parameters[compare]:
                parameters[compare] = parameters[index] ^ parameters[compare]
                parameters[index] = parameters[compare] ^ parameters[index]
                parameters[compare] = parameters[index] ^ parameters[compare]
    return parameters

result = sorted_by_john("sorted", "orsedt")
print(f"Sorted list: {result}\n")

