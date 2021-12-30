# Not completed, https://www.codewars.com/kata/55c6126177c9441a570000cc/train/python

def order_weight(strng):
    string = strng.split()
    
    for index in range(1, len(string)):
        currentPosition = index
        current_value = string[index]

        while currentPosition > 0 and sum_digits(string[currentPosition - 1]) >= sum_digits(current_value):
            if(sum_digits(string[currentPosition - 1]) != sum_digits(current_value)):
                string[currentPosition] = string[currentPosition - 1]
                currentPosition -= 1
            else:
                if(sort_alpha(current_value, string[currentPosition - 1])):
                    string[currentPosition] = string[currentPosition - 1]
                    currentPosition -= 1
                else:
                    break
        
        string[currentPosition] = current_value
            
    return ' '.join(string)

def sort_alpha(number1, number2):
    for number_one, number_two in zip(number1, number2):
        if(number_one > number_two):
            return False
        elif(number_one < number_two):
            return True
            
    if(len(str(number1)) > len(str(number2))):
        return False
         
    return True

def sum_digits(number):
    current_value = 0
    for digit in str(number):
        current_value += int(digit)
    return current_value