# https://www.codewars.com/kata/55c45be3b2079eccff00010f/train/python

def order(sentence):
    words = sentence.split()
    result = words.copy()
    
    for word in words:
        for letter in word:
            if (letter.isdigit()):
                result[int(letter) - 1] = word
    
    return ' '.join(result)
    