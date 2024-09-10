from september_2024.task2 import result


def char_police(word):
    new_word_list = []
    for letter in word:
        new_word_list.append(letter)

    return new_word_list


value = char_police('he,ll.o')
print(value)

def new_output(argument):
    new_string = " "
    for  index in range(len(argument)):
        if argument[index].isalpha():
            new_string += argument[index]

    return new_string


result = new_output('he,ll.o')
# print(result)

def array(word):
    for letter in word:
        if letter.isalpha():
            continue
        word.remove(letter)
        # word = str(word)
    return word

output = array(char_police('he,ll.o'))
print(output)