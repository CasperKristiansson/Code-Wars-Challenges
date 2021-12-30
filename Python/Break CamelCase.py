# https://www.codewars.com/kata/5208f99aee097e6552000148/train/python

def solution(s):
    i = 0
    while i < len(s):
        if(s[i].isupper()):
            s = s[:i] + " " + s[i:]
            i += 1
        i += 1
    return s
