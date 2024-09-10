
#
# def count_words(word):
#     global unique_set
#     new_list = []
#     for letter in word:
#         new_list.append(letter)
#         unique_set = set(new_list)
#     # counts = {letter:word.count(letter) for letter in word}
#         new_list[letter] = [letter]
#
#     return unique_set
#     # return counts
# value = (count_words("banana"))
# print(value)


def new_dict(words):
    new_dict = {}
    for letter in words:
        new_dict[letter.lower()] = words.count(letter.lower())
    return new_dict

result = new_dict("balablublublu")
print(result)

# def char_counter(wordz):
#     new_dict = ['a','c','d','e','f','g','h','i','j']
#     counter = 0
#     for letter in new_dict:
#         if letter == set.():
#             counter = counter + 1
#     return counter

# answer = char_counter(result)
# print(answer)

# def new(words):
#     new_dict = {}
#     counter = 0
#     for letter in words:
#         if letter == words.isalpha():
#             counter = counter+1
#             new_dict[letter] = counter
#     return new_dict
#
# print(new("banana"))


first = A[0]
second = A[1]
sec_first = B[-2]
sec_second = B[-3]
temp2 = ""
#
# for index in range(len(A)):
#     for index2 in range(len(B)):
#         if A[index] == B[index2]:
#             A[0] ^= B[-3]
#             A[1] ^= B[-2]
# return A+B

temp1 = ""
for index in range(1):
    temp1 += A[index]
    temp1 += A[index + 1]

print(temp1)

for index in range(1):
    temp2 += B[index]
    temp2 += B[index + 1]

print(temp2)

# for index in range(len(A)):
#     if A[index] == first:

first_word = A.split(',')
print(first_word)

