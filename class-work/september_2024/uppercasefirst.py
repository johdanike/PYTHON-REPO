

def uppercasefirst(word):
    global arr
    upper = ""
    lower = ""
    for letter in word:
        if letter.isupper():
            upper += letter
        if letter.islower() :
            lower += letter
            arr = upper + lower
    return arr

value = uppercasefirst('cHaRACterS')
print(value)