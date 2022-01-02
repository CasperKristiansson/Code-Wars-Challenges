# https://www.codewars.com/kata/54ba84be607a92aa900000f1/train/python

def is_isogram(string):
    string = string.lower()
    for letter in string:
        if letter in (string[:string.index(letter)] + string[string.index(letter) + 1:]):
            return False
        
    return True
    