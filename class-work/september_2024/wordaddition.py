def word_plus_ce(word_1, word_2 = "ce"):
    global new_word
    word_1 = word_1.lower()
    word_2 = word_2.lower()
    if len(word_1) % 2 == 0:
        half_1 = len(word_1) // 2
        half_2 = len(word_1) // 2
        word_a = word_1[:half_1]
        word_b = word_1[half_2:]

        new_word = word_a + word_2 + word_b
    else:
        new_word = word_1 + word_2
    return new_word

result = word_plus_ce("envvsb")
print(result)
