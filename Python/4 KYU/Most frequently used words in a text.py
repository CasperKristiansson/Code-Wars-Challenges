# https://www.codewars.com/kata/51e056fe544cf36c410000fb/train/python

def top_3_words(text):
    new_text = ''
    for character in text:
        if character.isalpha() or character == ' ' or character == "'":
            new_text += character.lower()
        else:
            new_text += ' '
    new_text = new_text.split()

    counts = {}
    for i in new_text:
        if(i != len(i) * "'"):
            counts[i] = counts.get(i, 0) + 1

    return sorted(counts, key=counts.get, reverse=True)[:3]
