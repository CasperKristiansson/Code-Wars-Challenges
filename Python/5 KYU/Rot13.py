# https://www.codewars.com/kata/530e15517bc88ac656000716/train/python

def rot13(message):
    string = []
    for letter in message:
        if(ord(letter) <= 122 and ord(letter) >= 65):
            letter = ord(letter) + 13
            if(letter >= 110 and letter > 122 or letter < 110 and letter > 90):
                letter -= 26
            string.append(chr(letter))
        else:
            string.append(letter)

    return ''.join(string)

