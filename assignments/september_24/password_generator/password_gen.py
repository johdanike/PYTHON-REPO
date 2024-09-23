import random
import string
from string import ascii_uppercase, ascii_lowercase


def random_password_gen():
    characters = "/.@!#$%_&*"
    collection = []
    for values in range(4):
        collection.append(random.choice(ascii_uppercase))
        collection.append(random.choice(ascii_lowercase))
        collection.append(random.choice(string.digits))
        collection.append(random.choice(characters))
    return ''.join(collection)

print(random_password_gen())