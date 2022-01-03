# https://www.codewars.com/kata/5552101f47fc5178b1000050/train/python

def dig_pow(n, p):
    total = 0
    for number in str(n):
        total += int(number) ** p
        p += 1
    
    if(total % n == 0):
        return total / n;
    
    return -1
    