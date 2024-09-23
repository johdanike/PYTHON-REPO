# word = input("Enter your favorite word: ")


def convert_strings_to_ascii(input1):
    temp = []
    for letters in input1:
        temp.append(ord(letters))
    return temp

def encrypt_ascii(input2):
    temp = []
    for letters in input2:
        letters += 2
        temp.append(letters)
    return temp

def convert_encrypted_ascii_back_to_string(input2):
    temp = ""
    for elements in input2:
        temp += chr(elements)
        # print(temp)
    return temp

# strings_to_ascii = convert_encrypted_ascii_back_to_string(encrypt_ascii(convert_strings_to_ascii('abc')))
# print(strings_to_ascii)
#
# strings_to_ascii = convert_strings_to_ascii(input("Enter a string: "))
# print(strings_to_ascii)
#
# encrypted = encrypt_ascii(strings_to_ascii)
# print(encrypted)
#
# back_to_string = convert_encrypted_ascii_back_to_string(encrypted)
# print(back_to_string)




