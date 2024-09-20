# no_of_times = int(input('How many numbers do you want to input? '))
indice = 1

# def numbs_to_list_and_tuples():
#     the_tuples = ()
#     the_list = []
#     value = ""
#     for number in range(1, no_of_times+1):
#         value = input(f'Input {number} \n Enter a number: ')
#         the_list.append(value)
#         the_tuples += (value,)
#     return f'{the_list}\n{the_tuples}'
#
# print(numbs_to_list_and_tuples())
#
# def numbs_list_tuples():
#     value = input("Enter numbers: ")
#     value = value.split(',')
#     the_tuples = tuple(value)
#     return f'{value}\n{the_tuples}'
# print(numbs_list_tuples())

# def numbs_to_list_and_tuples_2(numValue,*numb):
#     the_tuples = ()
#     the_list = []
#     value = ""
#     for number in numValue:
#         the_list.append(number)
#         the_tuples += (number,)
#     return f'{the_list}\n{the_tuples}'
#
# print(numbs_to_list_and_tuples_2(23,56,76,34,98))

def numbs_list_tuples_2(*value):
    value = value.split(',')
    the_tuples = tuple(value)
    return f'{value}\n{the_tuples}'
print(numbs_list_tuples_2(23,56,76,34,98))

