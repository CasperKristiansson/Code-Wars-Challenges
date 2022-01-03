# https://www.codewars.com/kata/5541f58a944b85ce6d00006a/train/python

def productFib(prod):
    first = 0
    second = 1
    
    while(first * second <= prod):
        if(first * second == prod):
            return [first, second, True]
        temp = second
        second += first
        first = temp
    
    return [first, second, False]
    