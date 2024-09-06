def biggest_odd(numbers):
    maximum = 0
    for number in numbers:
        if int(number) > maximum and int(number) % 2 != 0:
            maximum = int(number)

    return maximum
result = biggest_odd("23956")
print(f"Biggest odd is: {result}")


def big_odd(parameters):
    maximum = int(max([n for n in parameters if int(n)% 2 != 0]))
    return maximum
result = big_odd("23956")
print(f"Biggest odd is: {result}")

def biggiie(numbers):
    maximum = 0
    for number in numbers:
        if int(number) > maximum and int(number) % 2 == 1:
            maximum = int(number)
    return maximum

result = biggiie("23956")
print(f"Biggest odd is: {result}")