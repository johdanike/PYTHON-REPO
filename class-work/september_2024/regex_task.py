import re

def email_validity_checker(email):
    var = 'yes' if re.fullmatch(r"[a-z]*\d+@{1}g{1}m{1}a{1}i{1}l{1}.{1}c{1}o{1}m{1}", email) else 'no'
    if var == "yes":
        return True
    else:
        return False

email_address = input("Enter email address: \n")

email_address_value = email_validity_checker(email_address)
print(email_address_value)