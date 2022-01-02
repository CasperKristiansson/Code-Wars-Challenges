# https://www.codewars.com/kata/5659c6d896bc135c4c00021e/train/python

def next_smaller(n):    
    for number in range(n - 1, -1, -1):
        if(len(str(number)) != len(str(n))):
            break
        
        temp = str(n)
        for number_string in str(number):
            if number_string not in temp:
                break
            temp = temp.replace(number_string, '', 1)
        else:
            return number
            
    return -1

print(next_smaller(1234567908))
