# https://www.codewars.com/kata/541c8630095125aba6000c00/train/python

def digital_root(n):
    total = 0
    
    while True:
        for num in str(n):
            total += int(num)
        
        if len(str(total)) == 1:
            break

        n = total
        total = 0
    
    return total
