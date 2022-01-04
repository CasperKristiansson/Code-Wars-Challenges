def get_count(sentence):
    return sum(letter in ('a', 'e', 'i', 'o', 'u') for letter in sentence)
    