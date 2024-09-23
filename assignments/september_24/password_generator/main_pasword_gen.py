class password_generator_main:
    def __init__(self):


        def convert_strings_to_ascii(input1):
            temp = []
            for letters in input1:
                # print(ord(letters))
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
            # print(temp)
            return temp

        def generate_password_method(array):

            strings_to_ascii = convert_strings_to_ascii(input("Enter a string: "))
            encrypted = encrypt_ascii(strings_to_ascii)
            back_to_string_2 = convert_encrypted_ascii_back_to_string(encrypted)
            return back_to_string_2

generator = password_generator_main()
var = __name__ == '__main_pasword_gen'


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
#



