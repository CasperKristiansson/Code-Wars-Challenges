# https://www.codewars.com/kata/5264d2b162488dc400000001/train/python

def spin_words(sentence):
    sentence = sentence.split()
    for index, word in enumerate(sentence):
        if(len(word) >= 5):
            sentence[index] = word[::-1]
    
    return ' '.join(sentence)
